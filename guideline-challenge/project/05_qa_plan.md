# QA plan + quality gates

Không được viết "reviewer kiểm tra lại". Phải có sampling, metric, threshold và action khi fail. Thay mọi placeholder
mới là xong (gate G6).

## Flow

Guideline → Calibration → Production → Self-QC → Review → Rework → Quality Gate. Ghi cụ thể cho project của nhóm:

- **Ai review, review bao nhiêu:** Anh chịu trách nhiệm bàn giao; Danh review semantic/rule; Mạnh kiểm schema/export; Hoà kiểm geometry và coverage. Review 100% bộ calibration và blind vì bộ nhỏ.
- **Chọn sample theo rule nào:** kiểm trước các ảnh critical, occlusion, low_visibility và mọi needs_review/image_escalate, sau đó kiểm toàn bộ ảnh còn lại.
- **Issue được ghi ở đâu, đóng thế nào:** decision log đi kèm calibration report ghi mã ảnh, polygon/tag, rule, severity, bằng chứng, người sửa và kết quả kiểm lại. Reviewer khác người sửa xác nhận resolved hoặc accepted-escalation có lý do; không xoá cờ hàng loạt vì review chung.
- **Khi phát hiện guideline gap thì update và version ra sao:** Danh viết rule, Anh duyệt; v2 dựa trên calibration thực, v3 dựa trên blind thực. Giữ export gốc. Bản AI-assisted/consensus lưu riêng, không giả lập bài độc lập. Chỉ người giữ gold freeze; không sửa gold/split sau freeze.

## Defect severity

Nhóm được đổi mapping nếu downstream contract khác, nhưng phải giải thích và chốt trước khi QA.

| Severity | Định nghĩa cho project này | Ví dụ | Action mặc định |
|---|---|---|---|
| Critical | Vùng đi sai có hậu quả downstream lớn | Include làn ngược chiều, sidewalk/island, thân xe; nối qua vật che | Chặn bàn giao; sửa và kiểm mọi ảnh tương tự |
| Major | Sai semantic hoặc thiếu quyết định bắt buộc | Sai direct/alternative, thiếu attribute/escalation | Rework và review lại |
| Minor | Sai biên cục bộ không tạo critical | Vượt tolerance hoặc biên răng cưa | Sửa và kiểm lại |
| Question | Không đủ bằng chứng/rule | Không rõ quyền tiếp cận hoặc hướng làn | Không vẽ vùng nghi vấn; tag reason; Danh/Anh phân xử hoặc giữ escalation |

## Metrics

| Metric | Cách tính | Vì sao phù hợp với bài toán |
|---|---|---|
| Coverage | Số ảnh có quyết định hợp lệ / số ảnh yêu cầu; mục tiêu 100% | Không bỏ ảnh âm thầm |
| Schema validity | Object/tag đúng schema / tổng; mục tiêu 100%, không __undefined__ | Export dùng được |
| Geometry validity | Polygon trong khung, không tự cắt/overlap ngoài chủ đích / tổng; mục tiêu 100% | Tránh lỗi kỹ thuật |
| Boundary audit | Theo guideline: ≤10 px nửa dưới, ≤20 px nửa trên, ≤30 px đoạn nối giao lộ | Kiểm biên riêng, không che lỗi bằng IoU |
| Semantic audit | Polygon đã được reviewer xác nhận area_type / tổng; mục tiêu 100% hoặc escalation có quyết định | Phân biệt direct/alternative |
| Escalation closure | Cờ resolved hoặc accepted-escalation có lý do / tổng cờ; mục tiêu 100% | Không mất uncertainty |

Metric high-risk tách riêng: số critical còn mở phải bằng 0. IoU chỉ báo cáo khi có reference phù hợp; overlap giữa hai annotator không phải GT accuracy.

## Quality gate

Threshold là đề xuất của nhóm, không phải chuẩn ngành. Giải thích trade-off cost/risk.

```text
PASS if:
  Đủ ảnh; schema/geometry hợp lệ; không còn defect mở; mọi uncertainty đã có quyết định ghi lại.
REWORK if: Còn lỗi sửa được, thiếu ảnh/attributes hoặc chưa kiểm lại.
REJECT / ESCALATE if: Critical chưa xử lý, không đủ bằng chứng quyền đi, export không đọc được hoặc nguồn gốc không phù hợp mục đích đánh giá.
```

Trade-off: review 100% tốn công hơn sampling nhưng phù hợp bộ nhỏ; ưu tiên tránh false-positive đường đi hơn tô kín vùng thiếu bằng chứng. Đây là threshold đề xuất cho lab, không phải chuẩn an toàn xe tự hành hoặc kết quả đã đo đạt.

## Bằng chứng hiện tại

Theo xác nhận của Anh, cả nhóm đã duyệt 8 ảnh, import CVAT và đối chiếu với thành viên khác. Chưa có export cuối sau review và log quyết định từng issue trong workspace. Xác nhận review chung không chứng minh từng cờ uncertainty đã được giải quyết.
