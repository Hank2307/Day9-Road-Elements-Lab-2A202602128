# Revision log

Guideline v1 = bản nháp đầu; v2 = sau calibration nội bộ; v3 = sau blind handoff. Mỗi lần tăng `Version` trong
`02_guideline.md`, thêm một hoặc nhiều dòng vào bảng: đổi gì và vì sao, kèm bằng chứng (sample_id, dòng
calibration report, câu hỏi trong clarification log, feedback của peer).

Cột Version ghi dạng `v1`, `v2`, `v3` — `make status` tìm dòng bảng có `v2` và dòng có `v3`.

| Version | Đổi gì | Vì sao | Bằng chứng |
|---|---|---|---|
| v1 | Chốt ontology drivable_area với area_type direct/alternative và escalation | Tạo bản guideline đầu để calibration | 02_guideline.md và 03_cvat_labels.json |
| v2 | Làm rõ gore; không suy ra alternative từ asphalt/driveway; phân biệt bike-buffer với parking; nhắc dừng polygon trước xe | Export Mạnh và bản consensus được cả nhóm review khác đáng kể ở các vùng này | 06_calibration_report.csv: BDD05 BDD12 BDD20 BDD07 BDD23 |
| v3 | Thêm bảng tra nhanh cho 4 case dễ nhầm và nhắc semantic đúng không miễn kiểm geometry | Peer đánh giá guideline tốt nhưng đề nghị tăng ví dụ trực quan; kết quả nhìn chung khớp gold và lệch nhẹ vài pixel/point | 07_blind_handoff/peer_feedback.md; xác nhận của Anh ngày 2026-09-26 |
