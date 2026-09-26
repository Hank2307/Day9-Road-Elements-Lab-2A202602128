# Bàn giao Guideline Challenge — sanaka

Chủ đề: Drivable Area. Nhóm peer: Just For Fun. Guideline hiện tại: v3; phiên bản freeze: v2.

## Nội dung đã hoàn thiện

- Team, downstream contract, guideline v3 và ontology/schema CVAT.
- Sample pack, thư viện edge cases, QA plan, calibration report và bằng chứng so sánh hiện có.
- Gold freeze có 15 decisions; gold/sample pack còn nguyên theo tag gold-freeze.
- Feedback JFF nguyên văn, owner response, 5 PNG do Team Leader cung cấp và review trực quan từng gold decision.
- Bộ CVAT images 1.1 AI-assisted được JFF chấp nhận theo xác nhận của Anh, lưu tại `../ai_drafts/blind_drivable_reconstruction/`; nguồn AI được ghi rõ.

## Giới hạn cần người chấm biết

Chỉ có export calibration độc lập của Mạnh trong repo; bản so sánh còn lại là AI-assisted được nhóm review. Không có đủ export độc lập của toàn bộ thành viên hoặc calibration_measure theo quy trình đầy đủ.

JFF cung cấp 5 câu trả lời và 5 ảnh có nhãn qua Team Leader, không có export XML/ZIP từ task của họ. Ảnh tương ứng bộ AI được họ chấp nhận. Không có phép đo GTS độc lập; không tạo transfer_score hoặc export peer giả để vượt gate. Xem `07_blind_handoff/visual_review.md`.

`lab9.py status/check`: G1–G4 đạt kiểm tra cơ học; G5 còn thiếu peer export/transfer_score; G6 còn thiếu GTS hợp lệ. Không sửa tool để bỏ các điều kiện này. Câu Lab Coach “chỉ cần hoàn thành guideline challenge” được ghi nhận, nhưng không tự diễn giải thành miễn G5/G6.

Đây là hồ sơ nộp với dữ liệu có sẵn và giới hạn công khai, không phải khẳng định hoàn thành toàn bộ quy trình blind. Các thành viên/peer hiện không cung cấp thêm dữ liệu; xin người chấm đánh giá phần specification, feedback/revision và bằng chứng hiện có.

## Đường dẫn đọc nhanh

1. `02_guideline.md` và `03_cvat_labels.json`.
2. `06_calibration_report.csv`, `06_offline_review_evidence.md`.
3. `07_blind_handoff/peer_feedback_original.md`, `peer_feedback.md`, `visual_review.md`, `peer_images/`.
4. `08_revision_log.md`, `05_qa_plan.md`, `09_cvat_export_or_task_reference.txt`.

Không gửi toàn bộ gói nộp owner này cho peer trước một lượt blind mới vì có gold. Blind-pack v2 đã phát hành giữ nguyên; guideline v3 là bản sau feedback.
