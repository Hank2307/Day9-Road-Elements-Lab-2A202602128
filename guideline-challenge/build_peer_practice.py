"""Package examples only; never expose reserved blind images or gold."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib

base = Path(__file__).resolve().parent
out = base / 'handoff' / 'sanaka-practice-v1.zip'
out.parent.mkdir(exist_ok=True)
readme = '''# sanaka — thử guideline v1 (KHÔNG phải blind test chính thức)

Gói này dùng 5 ảnh example: BDD03, BDD01, BDD02, BDD10, BDD16.
Chưa freeze gold/chưa hoàn tất calibration. Không dùng kết quả để tính GTS.
Không đọc repo owner hoặc xin gold. Bộ blind riêng chưa được gửi.

1. Đọc 02_guideline.md; assets/examples giữ nguyên đường dẫn để xem minh hoạ.
2. Tạo task CVAT mới, dán toàn bộ 03_cvat_labels.json vào Raw.
3. Upload 5 ảnh trong images/, gắn guideline và kiểm tra ảnh minh hoạ hiển thị.
4. Label theo guideline: Polygon Shape, area_type direct/alternative; không để __undefined__.
5. Không đoán khi thiếu bằng chứng: dùng needs_review/image_escalate + reason theo guideline.
6. Save, export CVAT for images 1.1, tắt Save images; gửi ZIP và feedback cho sanaka.

Ghi thời gian và nguyên văn câu hỏi khi gặp rule chưa rõ. Owner không giải thích thêm domain rule trong lượt thử.

## Feedback gửi lại
1. Bạn có hiểu label gì/không label gì chỉ từ guideline không? Chỗ nào chưa rõ?
2. Rule hoặc ví dụ nào khó áp dụng? Ghi mã ảnh và mục guideline.
3. Có tình huống guideline chưa bao phủ không?
4. Công cụ/attribute/escalation có rõ và dùng được không?
5. Bạn đề nghị thay đổi gì để annotator mới làm độc lập được?

Gửi lại: export ZIP + feedback + danh sách câu hỏi (hoặc xác nhận không có câu hỏi).
Đây là rehearsal/usability test; không thay thế blind handoff sau freeze.
'''
files = {'02_guideline.md': base/'project/02_guideline.md',
         '03_cvat_labels.json': base/'project/03_cvat_labels.json'}
for sid in ('BDD03','BDD01','BDD02','BDD10','BDD16'):
    files[f'images/{sid}.jpg'] = base/f'data/bdd100k/{sid}.jpg'
for sid in ('BDD01','BDD04','BDD10','BDD17'):
    name = f'assets/examples/{sid}-annotated.png'
    files[name] = base/'project'/name
with ZipFile(out, 'w', ZIP_DEFLATED) as archive:
    for name,path in files.items(): archive.write(path,name)
    archive.writestr('PEER_README.md',readme)
with ZipFile(out) as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == set(files)|{'PEER_README.md'}
    assert len([n for n in archive.namelist() if n.startswith('images/')]) == 5
    assert all(s not in n for n in archive.namelist() for s in ['gold','BDD11','BDD14','BDD18','BDD24','BDD25'])
print(out)
print('Verified allowlist, CRC, 5 examples, 4 referenced illustrations; no gold/blind files.')
print('SHA256:',hashlib.sha256(out.read_bytes()).hexdigest())
