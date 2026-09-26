# Ontology + CVAT setup

Bảng ontology là **source of truth** cho schema CVAT: `03_cvat_labels.json` phải khớp từng dòng ở đây. Thay mọi
placeholder mới là xong (gate G2).

## Ontology table

| Name | Geometry | Type (class / attribute) | Allowed values | Default | Mutable? | Rationale |
|---|---|---|---|---|---|---|
| `drivable_area` | polygon | class | — | — | false | Vùng mặt đường xe cơ giới (ego) có thể di chuyển hợp pháp và an toàn theo quy tắc bài tập. |
| `area_type` | — | attribute (select) của `drivable_area` | `__undefined__`, `direct`, `alternative` | `__undefined__` | false | Phân loại vùng đi được: `direct` là làn xe ego đang trực tiếp đi; `alternative` là vùng khác cùng chiều xe có thể đi vào hợp lệ (làn bên cạnh, nhánh rẽ trong giao lộ, khoảng trống làn đỗ ≥ 1 thân xe). Bắt buộc để `__undefined__` làm giá trị mặc định đầu tiên để phát hiện người vẽ quên gán. |
| `needs_review` | — | attribute (checkbox) của `drivable_area` | `false`, `true` | `false` | false | Cờ đánh dấu polygon nghi ngờ (biên đường mờ, thời tiết mưa phản chiếu, ranh giới hàng xe đỗ không có vạch) để QA reviewer thẩm định lại. |
| `image_escalate` | tag | class | — | — | false | Cờ đánh dấu toàn bộ bức ảnh khi gặp vấn đề không thể quyết định an toàn (mất hoàn toàn làn ego, không xác định được chiều đi của làn, ảnh quá tối, bão tuyết). Vùng nghi ngờ không vẽ polygon mà gắn tag này. |
| `reason` | — | attribute (text) của `image_escalate` | chữ tự do | `""` (trống) | false | Bắt buộc ghi lý do ngắn gọn vì sao ảnh cần escalate (ví dụ: "Không rõ chiều đi của làn bên trái", "Ảnh đêm quá tối không thấy mép đường"). |

## Class hay attribute

- **`drivable_area` là Class**: Vì đây là đối tượng không gian chính có ranh giới hình học độc lập (polygon phân định vùng mặt đường với vỉa hè, dải phân cách, lan can, chướng ngại vật).
- **`area_type` là Attribute**: Bản chất đối tượng vẫn là bề mặt đường đi được, sự khác biệt giữa `direct` và `alternative` là ngữ nghĩa quan hệ không gian đối với xe chủ (ego vehicle). Thuộc tính thống nhất dùng tên `area_type` (theo guideline v1 mục 4).
- **`needs_review` là Attribute (checkbox)**: Đi kèm trực tiếp với từng polygon để reviewer lọc và kiểm tra các ca nghi ngờ mà không làm gián đoạn tiến độ gán nhãn.
- **`image_escalate` là Class kiểu Tag**: Áp dụng cho toàn bộ frame ảnh khi không thể gán nhãn từng polygon một cách tin cậy. Đi kèm thuộc tính text `reason` để ghi chú lý do.

**Default và nguy cơ Bias:**
Nếu thiết lập giá trị mặc định của `area_type` là `direct`, người vẽ khi thao tác hàng loạt trên các làn bên cạnh (`alternative`) sẽ rất dễ quên đổi thuộc tính. Điều này tạo ra lỗi nghiêm trọng (false positive direct lane) trong dữ liệu huấn luyện xe tự hành — khiến bộ lập quỹ đạo (motion planner) hiểu nhầm rằng xe có thể tiếp tục lao thẳng trên làn đường không dành cho mình. Do đó, việc đặt `__undefined__` đứng đầu danh sách và làm giá trị mặc định là bắt buộc: nếu export còn giá trị `__undefined__`, hệ thống QA sẽ lập tức phát hiện annotator chưa hoàn thành thao tác.

## CVAT

- **Phiên bản CVAT** (`make cvat-status`): CVAT v2.74.1 tại `http://localhost:8080`
- **Tên task calibration** (có version guideline, ví dụ `team07-calib-v1`): `sanaka-calib-manh-v1` (Task ID 14; Job ID 14 theo bản ghi của Mạnh)
- **Guide của task đã dán `02_guideline.md`?**: Có (toàn bộ nội dung guideline v1 của Danh đã được dán vào phần Description / Guide của task trên CVAT).
- **Nhóm dùng Track hay Shape, vì sao:** Nhóm dùng **Shape**. Lý do: Bộ dữ liệu BDD100K bao gồm 26 ảnh tĩnh độc lập được chụp tại các địa điểm và bối cảnh khác nhau (không phải video sequence liên tục như LISA). Do đó, mỗi polygon trên từng ảnh là một instance hình học riêng lẻ (Shape), không cần liên kết hay nội suy qua các frame thời gian (Track).

## Setup test

### Bổ sung bằng chứng offline / review nhóm — 2026-09-26

Theo Anh, bộ 8 ảnh AI-assisted đã được cả nhóm duyệt, import CVAT và đối chiếu với thành viên khác. Bản XML/ZIP gốc nằm tại `../ai_drafts/anh_calibration_v1/`; chưa nhận export cuối từ CVAT. Kết quả kiểm tra hai export và khác biệt nằm trong `06_offline_review_evidence.md`. Không thay thế bài độc lập của Mạnh hoặc tuyên bố trợ lý đã chạy CVAT. Hai tên task trong tài liệu này và file 09 đang khác nhau; cần xác nhận tên task thực tế, không tự đổi ID.

- **Người thực hiện kiểm thử:** Danh (Guideline Lead) đã mở task kiểm thử độc lập mà không nhận giải thích miệng từ người dựng task (Mạnh).
- **Kết quả kiểm thử:**
  - **Công cụ:** Danh nhận diện ngay công cụ *Draw new polygon* với nhãn `drivable_area`.
  - **Thuộc tính:** Mở sidebar thấy ngay dropdown `area_type` hiển thị ban đầu là `__undefined__` và bắt buộc phải chọn giữa `direct` hoặc `alternative`.
  - **Escalate:** Tích chọn checkbox `needs_review` hoạt động mượt mà; tag `image_escalate` hiển thị rõ ràng tại thanh công cụ Setup Tag kèm ô nhập text `reason`.
  - **Ghi nhận:** Schema và nhãn khớp 100% với tài liệu `02_guideline.md` (mục 4), annotator thao tác ngay được mà không gặp trở ngại kỹ thuật hay nhầm lẫn quy ước.
