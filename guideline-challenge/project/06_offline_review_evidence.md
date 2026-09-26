# Bằng chứng review offline — 2026-09-26

## Nguồn và trạng thái

Anh xác nhận cả nhóm đã review/pass 8 ảnh AI-assisted, đã import CVAT và đối chiếu bài thành viên khác. Đây là xác nhận của người dùng, không phải thao tác CVAT do trợ lý thực hiện. Chưa nhận export cuối sau review hoặc quyết định từng khác biệt.

Đã đọc `06_calibration_exports/manh.zip` và `../ai_drafts/anh_calibration_v1/anh-ai-draft-cvat.zip`. Không sửa hai file. Bản AI là nguồn được nhóm review, không phải bài calibration độc lập thứ hai.

## Kiểm tra đã chạy

- Hai ZIP đọc được, CRC không lỗi; mỗi ZIP có một annotations.xml đọc được.
- Cả hai đủ BDD04, BDD05, BDD07, BDD12, BDD13, BDD17, BDD20, BDD23.
- Polygon kiểm tra hợp lệ theo Shapely, trong khung 1280×720, không overlap diện tích >1 px²; label drivable_area và area_type thuộc direct/alternative.
- Đây là kiểm tra cấu trúc/hình học, không chứng minh semantic đúng, chưa phải kiểm đầy đủ mọi metadata CVAT.
- Mạnh: 15 polygon, 10 needs_review=true, 0 tag escalation. AI: 11 polygon, 11 needs_review=true, 5 tag escalation. Không tự xoá các cờ này.

## So sánh vùng

IoU tính trên union polygon theo từng area_type, tọa độ liên tục. Không phải accuracy với GT; N/A nghĩa cả hai không vẽ loại vùng đó.

| Ảnh | Direct IoU | Alternative IoU |
|---|---|---|
| BDD04 | 0.9151 | N/A |
| BDD05 | 0.4359 | 0.0000 |
| BDD07 | 0.3281 | 0.0620 |
| BDD12 | 0.1647 | 0.0000 |
| BDD13 | 0.2031 | N/A |
| BDD17 | 0.7822 | 0.3928 |
| BDD20 | 0.0228 | 0.0000 |
| BDD23 | 0.5316 | 0.0000 |

Ưu tiên lấy quyết định đã chốt cho BDD20, BDD12, BDD07; kiểm thêm BDD13. Không suy ra ai đúng từ IoU. Không tự tạo diagnosis/rule change để đủ 3 dòng calibration.

## Cần bổ sung để hoàn tất

1. Export CVAT cuối sau review (hoặc xác nhận không chỉnh bất kỳ polygon/attribute/tag nào).
2. Quyết định cụ thể cho các bất đồng: mã ảnh, chọn cách nào, lý do/rule, cờ nào được giữ hoặc giải quyết.
3. Các export độc lập còn lại nếu có. Không tạo file mang tên thành viên bằng cách sao chép AI output.
4. Tên nhóm peer; sau handoff cần export, clarification log và feedback thật để chấm GTS và viết v3.

G1/G2 đạt kiểm tra cơ học. G3 thiếu report; G4 chưa freeze; G5 thiếu peer output; G6 chưa v3. Không nâng version, freeze hoặc đánh dấu hoàn tất các bước chưa có bằng chứng.
