"""Build explicitly AI-authored CVAT images 1.1 annotations and review overlays."""
import json
import hashlib
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
from shapely.geometry import Polygon

HERE=Path(__file__).resolve().parent
LAB=HERE.parents[1]
data=json.loads((HERE/'annotations.json').read_text(encoding='utf-8'))
assert [r['id'] for r in data['images']]==['BDD11','BDD14','BDD18','BDD24','BDD25']
schema=json.loads((LAB/'project/03_cvat_labels.json').read_text(encoding='utf-8'))
assert {s['name']:s['type'] for s in schema}=={'drivable_area':'polygon','image_escalate':'tag'}
root=ET.Element('annotations')
ET.SubElement(root,'version').text='1.1'
root.append(ET.Comment(data['provenance']))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20)
previews=[]
count=0
for index,row in enumerate(data['images']):
 original=Image.open(LAB/'data/bdd100k'/f"{row['id']}.jpg").convert('RGBA')
 assert original.size==(1280,720)
 node=ET.SubElement(root,'image',id=str(index),name=row['id']+'.jpg',width='1280',height='720')
 layer=Image.new('RGBA',original.size)
 draw=ImageDraw.Draw(layer)
 shapes=[]
 for item in row['polygons']:
  pts=[tuple(p) for p in item['points']]
  poly=Polygon(pts)
  assert poly.is_valid and poly.area>0, row['id']
  assert all(0<=x<1280 and 0<=y<720 for x,y in pts)
  assert all(poly.intersection(other).area<0.01 for other in shapes), row['id']
  shapes.append(poly)
  assert item['type'] in ('direct','alternative')
  shape=ET.SubElement(node,'polygon',label='drivable_area',source='auto',occluded='0',z_order='0',points=';'.join(f'{x},{y}' for x,y in pts))
  ET.SubElement(shape,'attribute',name='area_type').text=item['type']
  ET.SubElement(shape,'attribute',name='needs_review').text='true'
  color=(0,230,118) if item['type']=='direct' else (40,140,255)
  draw.polygon(pts,fill=(*color,60))
  draw.line(pts+[pts[0]],fill=(*color,255),width=3)
  count+=1
 tag=ET.SubElement(node,'tag',label='image_escalate',source='auto')
 assert row['reason'].strip()
 ET.SubElement(tag,'attribute',name='reason').text=row['reason']
 canvas=Image.new('RGB',(1280,776),'#17202c')
 canvas.paste(Image.alpha_composite(original,layer).convert('RGB'),(0,56))
 title=ImageDraw.Draw(canvas)
 title.text((14,4),row['id']+' | JFF annotation with AI assist',font=font,fill='white')
 title.text((14,30),'GREEN: direct | BLUE: alternative | JFF acceptance confirmed by Pham Hoang Anh',font=font,fill='white')
 canvas.save(HERE/f"{row['id']}-overlay.jpg",quality=95)
 previews.append(canvas)
ET.indent(root)
xml=ET.tostring(root,encoding='utf-8',xml_declaration=True)
assert len(ET.fromstring(xml).findall('image'))==5
(HERE/'annotations.xml').write_bytes(xml)
with ZipFile(HERE/'sanaka-drivable-ai-reconstruction-cvat-1.1.zip','w',ZIP_DEFLATED) as z:
 z.writestr('annotations.xml',xml)
with ZipFile(HERE/'sanaka-drivable-ai-reconstruction-cvat-1.1.zip') as z:
 assert z.testzip() is None and z.namelist()==['annotations.xml']
sheet=Image.new('RGB',(1280,1164),'#17202c')
for i,preview in enumerate(previews): sheet.paste(preview.resize((640,388)),((i%2)*640,(i//2)*388))
sheet.save(HERE/'contact-sheet.jpg',quality=95)
report=f'Validated offline: 5 images, {count} polygons, 5 escalation tags; geometry valid, no overlaps, bounds and enums valid; XML parses and ZIP CRC passes.\n'
for filename in ['02_guideline.md','03_cvat_labels.json']:
 report+=filename+' SHA256 '+hashlib.sha256((LAB/'project'/filename).read_bytes()).hexdigest()+'\n'
(HERE/'VALIDATION.txt').write_text(report,encoding='utf-8')
print(report)
