"""Render deterministic annotation overlays and CVAT XML; never alter originals."""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED
from PIL import Image, ImageDraw, ImageFont
from shapely.geometry import Polygon

HERE = Path(__file__).resolve().parent
LAB = HERE.parents[1]
data = json.loads((HERE / 'annotations.json').read_text(encoding='utf-8'))
expected = ['BDD04', 'BDD05', 'BDD07', 'BDD12', 'BDD13', 'BDD17', 'BDD20', 'BDD23']
assert [row['id'] for row in data['images']] == expected
root = ET.Element('annotations')
ET.SubElement(root, 'version').text = '1.1'
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 22)
small = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 17)
previews = []
notes = ['# Review bản nháp AI — Anh / sanaka', '',
         '**Không phải calibration độc lập, không phải GT. Chưa được người duyệt.**', '',
         'Xanh lá = direct; xanh dương = alternative. Mọi polygon có needs_review=true.',
         'Ảnh gốc không bị sửa. Tọa độ XML/JSON dùng ảnh gốc 1280×720; thanh tiêu đề chỉ nằm trong ảnh preview.', '',
         '## Kiểm tra từng ảnh', '']
for index, row in enumerate(data['images']):
    original = Image.open(LAB / 'data' / 'bdd100k' / (row['id'] + '.jpg')).convert('RGBA')
    assert original.size == (1280, 720)
    layer = Image.new('RGBA', original.size)
    draw = ImageDraw.Draw(layer)
    node = ET.SubElement(root, 'image', id=str(index), name=row['id']+'.jpg', width='1280', height='720')
    geometries = []
    for number, item in enumerate(row['polygons'], 1):
        points = [tuple(p) for p in item['points']]
        assert all(0 <= x < 1280 and 0 <= y < 720 for x, y in points)
        shape = Polygon(points)
        assert shape.is_valid and shape.area > 0, row['id']
        assert all(shape.intersection(other).area < 0.01 for other in geometries), row['id']
        geometries.append(shape)
        assert item['type'] in ('direct', 'alternative')
        color = (0, 230, 118) if item['type'] == 'direct' else (40, 140, 255)
        draw.polygon(points, fill=(*color, 65))
        draw.line(points + [points[0]], fill=(*color, 255), width=3)
        for x, y in points:
            draw.ellipse((x-2, y-2, x+2, y+2), fill=(255, 190, 40, 255))
        polygon = ET.SubElement(node, 'polygon', label='drivable_area', source='auto', occluded='0', z_order='0', points=';'.join(f'{x},{y}' for x,y in points))
        ET.SubElement(polygon, 'attribute', name='area_type').text = item['type']
        ET.SubElement(polygon, 'attribute', name='needs_review').text = 'true'
    if row['escalation']:
        tag = ET.SubElement(node, 'tag', label='image_escalate', source='auto')
        ET.SubElement(tag, 'attribute', name='reason').text = row['escalation']
    preview = Image.new('RGB', (1280, 776), '#17202c')
    preview.paste(Image.alpha_composite(original, layer).convert('RGB'), (0, 56))
    title = ImageDraw.Draw(preview)
    title.text((16, 5), row['id']+' | AI DRAFT - HUMAN REVIEW REQUIRED', font=font, fill='white')
    title.text((16, 32), 'GREEN: direct | BLUE: alternative | vertices: review | original coordinates: 1280 x 720', font=small, fill='#d7dde5')
    preview.save(HERE / (row['id']+'-overlay.png'))
    previews.append(preview)
    notes += [f"### {row['id']}", '', f"![{row['id']}]({row['id']}-overlay.png)", '', row['review'], '',
              ('Escalation: '+row['escalation']) if row['escalation'] else 'Không có image_escalate; vẫn cần duyệt polygon.', '',
              '- [ ] Đã kiểm tra boundary, direct/alternative, vật che và mui xe.',
              '- [ ] Đã sửa/giải quyết needs_review và escalation trên CVAT.', '']
ET.indent(root)
ET.ElementTree(root).write(HERE / 'annotations.xml', encoding='utf-8', xml_declaration=True)
parsed = ET.parse(HERE / 'annotations.xml')
assert len(parsed.findall('image')) == 8
with ZipFile(HERE / 'anh-ai-draft-cvat.zip', 'w', ZIP_DEFLATED) as archive:
    archive.write(HERE / 'annotations.xml', 'annotations.xml')
sheet = Image.new('RGB', (1280, 1552), '#17202c')
for i, preview in enumerate(previews):
    sheet.paste(preview.resize((640, 388)), ((i % 2)*640, (i // 2)*388))
sheet.save(HERE / 'contact-sheet.jpg', quality=95)
notes += ['## Import / bàn giao', '',
          '1. Tạo task mới với 8 ảnh gốc và toàn bộ project/03_cvat_labels.json; không import vào task calibration độc lập đang có.',
          '2. Upload annotations, chọn CVAT for images 1.1, dùng anh-ai-draft-cvat.zip (bên trong có annotations.xml).',
          '3. Review từng ảnh theo checklist, chỉnh polygon/attributes và Save.',
          '4. Nếu export lại, ghi rõ AI-assisted; không thay thế anh.zip độc lập một cách âm thầm.', '',
          'Đã kiểm tra offline: đủ 8 ảnh, polygon hợp lệ/không tự cắt, nằm trong ảnh, không overlap, enum hợp lệ và XML đọc được.',
          'Chưa kiểm thử import trên CVAT đang chạy; chưa so GT hay đo IoU; kiểm tra hình học không chứng minh nhãn đúng.', '',
          '## Nguồn và tái tạo', '', data['provenance'], '',
          'Không sử dụng export thành viên khác hoặc mask gold. Các quyết định vẫn có thể sai và cần người duyệt.', '']
for name in ['02_guideline.md', '03_cvat_labels.json']:
    digest = hashlib.sha256((LAB / 'project' / name).read_bytes()).hexdigest()
    notes.append(f'- SHA256 {name}: `{digest}`')
notes += ['', 'Chạy lại build.py bằng Anaconda base sau khi sửa annotations.json.']
(HERE / 'REVIEW.md').write_text('\n'.join(notes)+'\n', encoding='utf-8')
print('Validated 8 images;', sum(len(r['polygons']) for r in data['images']), 'polygons. XML, ZIP, 8 overlays, contact sheet and REVIEW.md generated.')
