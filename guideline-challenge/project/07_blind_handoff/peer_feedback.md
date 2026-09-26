# Peer feedback + owner response

- **Nhóm peer:** Just For Fun
- **Người label blind:** Nhóm peer không cung cấp tên cá nhân
- **Nguồn:** `C:\Users\pc\Downloads\PEER_FEEDBACK.md`, nhận ngày 2026-09-26
- **Bản lưu trong repo:** [feedback nguyên văn](peer_feedback_original.md); [5 ảnh được cung cấp](peer_images/); [review trực quan](visual_review.md). Các câu trả lời dưới đây là bản tóm tắt, giữ nguyên bản nguồn để đối chiếu.
- **Tình trạng export:** Anh xác nhận nhãn peer nhìn chung giống gold về semantic và cấu trúc vùng; một số boundary/point lệch vài pixel. Export CVAT không được lưu trong repo nên nhận xét này không dùng để tính GTS chính thức.
- **Bổ sung xác nhận:** Anh đã review bộ dựng lại và xác nhận Just For Fun đã chấp nhận bộ này. Tên mô tả: **JFF annotation with AI assist — reviewed and accepted by Just For Fun**. File tại `../../ai_drafts/blind_drivable_reconstruction/` được sinh offline bằng AI, không phải export tải từ task của JFF; đã có tiếp xúc gold nên không dùng làm bằng chứng blind độc lập hoặc tính GTS độc lập.

## 1. Peer trả lời

### Rule rõ nhất / giúp quyết định nhanh nhất

Phần phân biệt `direct`, `alternative` và background rõ ràng. Các rule về vạch vàng, vạch trắng, vỉa hè, gore, làn xe đạp và làn ngược chiều giúp xác định nhanh vùng vẽ/bỏ. Rule dừng `direct` trước xe, không kéo polygon vào vùng không nhìn thấy và checklist cuối guideline cũng hữu ích.

### Rule mơ hồ hoặc phải tự suy diễn

Các rule chính khá rõ. Giao lộ, vạch trắng liền và vùng bị che vẫn cần quan sát tổng thể, nhưng `needs_review`, `image_escalate` và rule không đoán chiều đi giúp xử lý mà không gây ảnh hưởng lớn.

### Sample khiến guideline “vỡ”

Không phát hiện sample nào làm guideline bị vỡ. Các ví dụ BDD01, BDD04, BDD10 và BDD17 bao phủ nhiều tình huống và hỗ trợ áp dụng rule.

### Attribute/default dễ gây thao tác sai

`area_type = __undefined__` có thể bị bỏ quên khi thao tác nhanh. Guideline đã giải thích rõ đây là trạng thái chưa chọn và checklist trước export giúp giảm lỗi.

### Một thay đổi cụ thể giúp annotator mới ít hỏi hơn

Nên tăng tính trực quan cho các case dễ nhầm: alternative với background trên mặt đường rộng; parking với bike lane/buffer; direct/alternative tại giao lộ; và khi nào dùng `needs_review` hay `image_escalate`. Đây là cải tiến nhỏ, không phải thiếu rule nghiêm trọng.

## 2. Owner phân loại

| Feedback / quan sát | Nguyên nhân | Xử lý | Bằng chứng |
|---|---|---|---|
| Một số case phức tạp cần quan sát tổng thể | data ambiguity | Giữ escalation path hiện tại; không đổi semantic | Peer feedback câu 2 |
| `__undefined__` có thể bị bỏ quên | execution error | Giữ default để QA phát hiện; nhấn lại checklist trước export | Peer feedback câu 4; guideline mục 4 và 10 |
| Cần trình bày trực quan hơn 4 case dễ nhầm | guideline gap nhỏ về khả năng tra cứu | Accept + revise: thêm bảng tra nhanh trong guideline v3 | Peer feedback câu 5 |
| Semantic/cấu trúc nhìn chung khớp gold nhưng boundary/point lệch nhẹ | minor geometry variation | Chấp nhận nếu trong tolerance; ngoài tolerance thì rework theo QA plan | Xác nhận của Anh sau khi xem kết quả peer; không có export để đo lại |

## Kết luận

Guideline được peer đánh giá tốt, không phát hiện lỗi nghiêm trọng hoặc sample làm guideline vỡ. Revision v3 tập trung tăng tính trực quan và khả năng tra cứu; không thay đổi ontology hay gold đã freeze.
