# Phân công thành viên — Drivable Area Guideline Challenge

File này hướng dẫn công việc chi tiết cho **Tống Thanh Danh**, **Lê Đức Mạnh** và **Chu Thái Hoà**. Chủ đề của nhóm là **Drivable Area**.

## Mục tiêu chung

Nhóm cần xây dựng một hệ thống annotation mà nhóm khác có thể sử dụng mà không cần nghe giải thích trực tiếp:

1. Xác định rõ vùng nào được xem là drivable area.
2. Viết guideline đủ rõ để người lạ làm theo.
3. Biến guideline thành ontology và bộ label dùng được trong CVAT.
4. Calibration độc lập để tìm quy tắc còn mơ hồ.
5. Viết và freeze gold decision trước khi gửi blind test.
6. Chấm kết quả của nhóm peer và sửa guideline lên v3.

## Quy ước làm việc chung

- Mỗi file chỉ có **một người sửa chính**. Người khác review bằng comment hoặc nhắn người phụ trách, không cùng sửa một lúc.
- Trước khi sửa: chạy `git pull`.
- Hoàn thành một phần rõ ràng thì commit nhỏ và push ngay.
- Không tự thêm quy tắc chỉ bằng lời nói. Mọi quyết định phải xuất hiện trong guideline, ontology hoặc escalation rule.
- Nếu có Git/CVAT/Docker error quá 3 phút, báo Team Leader hoặc Lab Coach.
- Mọi người cập nhật checkbox trong `TEAM_PROGRESS_DRIVABLE_AREA.md`.
- Trước khi làm riêng, cả nhóm phải chốt bốn vấn đề:
  - Có label shoulder/emergency lane không?
  - Parking area có phải drivable area không?
  - Có suy luận vùng bị phương tiện che khuất không?
  - Có label `alternative` drivable area hay chỉ vùng trực tiếp của ego vehicle?

---

# 1. Danh — Guideline Lead

## Trách nhiệm chính

Danh chịu trách nhiệm biến các quyết định của nhóm thành quy tắc viết rõ ràng, nhất quán và có thể kiểm thử. File chính:

- `project/02_guideline.md`
- `project/08_revision_log.md`
- Phối hợp điền `project/06_calibration_report.csv` sau calibration
- Phối hợp phân tích `project/07_blind_handoff/peer_feedback.md` sau blind test

## Việc cần làm ngay — Guideline v1

### Bước 1: Đọc đầu vào

- [ ] Đọc `project/01_problem_statement.md` sau khi Team Leader hoàn thiện bản nháp.
- [ ] Đọc ontology đề xuất của Mạnh để bảo đảm tên label/attribute trong guideline giống hệt CVAT.
- [ ] Xem các ảnh example và calibration do Hoà đề xuất.
- [ ] Ghi lại các trường hợp có thể khiến hai annotator vẽ khác nhau.

### Bước 2: Viết đủ 10 mục trong `02_guideline.md`

- [ ] **Objective và scope:** guideline phục vụ bài toán gì, giới hạn trong ảnh BDD nào.
- [ ] **Annotation unit:** một polygon đại diện cho đối tượng/vùng nào; khi nào tách thành nhiều polygon.
- [ ] **Geometry rule:** polygon bắt đầu/kết thúc ở đâu, bám curb/road edge thế nào, mức độ chi tiết cần thiết.
- [ ] **Taxonomy:** giải thích từng label và attribute bằng đúng tên trong ontology.
- [ ] **Inclusion:** liệt kê rõ các bề mặt được label.
- [ ] **Exclusion:** sidewalk, median, traffic island, vegetation, barrier và các vùng không được phép lái xử lý thế nào.
- [ ] **Visibility/occlusion:** chỉ vẽ phần nhìn thấy hay suy luận sau xe/vật cản; xử lý vùng bị che một phần.
- [ ] **Ambiguity/escalation:** khi nào dùng `unknown`, `needs_review` hoặc `image_escalate`.
- [ ] **Temporal rule:** ghi rõ không dùng temporal tracking vì bài dùng ảnh BDD độc lập.
- [ ] **Examples/common mistakes:** giải thích bằng `sample_id`; không phụ thuộc vào lời nói hoặc ảnh chỉ có trên CVAT cá nhân.

### Các câu hỏi bắt buộc guideline phải trả lời

- [ ] Vùng ego vehicle đang chạy có được label toàn bộ tới cuối ảnh không?
- [ ] Vạch kẻ đường có chia polygon hay polygon đi xuyên qua vạch?
- [ ] Làn ngược chiều có được xem là drivable hay không?
- [ ] Shoulder, emergency lane và parking bay xử lý thế nào?
- [ ] Intersection không còn lane boundary thì xác định biên bằng gì?
- [ ] Vùng sau xe tải/xe buýt bị che có được suy luận không?
- [ ] Curb thấp, đường vào nhà hoặc bề mặt nhìn giống đường xử lý thế nào?
- [ ] Ảnh tối, mưa, tuyết hoặc boundary mờ cần bao nhiêu bằng chứng để label?
- [ ] Polygon chạm biên ảnh được kết thúc như thế nào?
- [ ] Khi không đủ bằng chứng, annotator phải chọn gì trong CVAT?

### Bàn giao v1

- [ ] Xoá toàn bộ `TODO` thuộc phần guideline.
- [ ] Đổi dòng `Version:` thành `v1`.
- [ ] Kiểm tra mọi label/attribute viết giống hệt `03_cvat_labels.json`.
- [ ] Nhờ một thành viên đọc guideline mà không nghe giải thích, sau đó ghi lại chỗ họ hiểu sai.
- [ ] Sửa các chỗ chưa rõ và báo Team Leader review.
- [ ] Commit và push guideline v1.

## Việc sau calibration — Guideline v2

- [ ] Đọc kết quả `06_calibration_measure.csv`.
- [ ] Cùng nhóm chọn ít nhất ba bất đồng lớn nhất.
- [ ] Phân loại từng bất đồng: `guideline_gap`, `data_ambiguity` hoặc `execution_error`.
- [ ] Không giải quyết bằng “cả nhóm thống nhất miệng”; phải thêm rule, example hoặc escalation path.
- [ ] Cập nhật guideline thành `v2`.
- [ ] Ghi thay đổi v2 vào `08_revision_log.md`, nêu bằng chứng calibration cụ thể.
- [ ] Kiểm tra guideline v2 khớp với ontology trước khi freeze.

## Việc sau blind test — Guideline v3

- [ ] Đọc toàn bộ câu hỏi trong `clarification_log.csv`.
- [ ] Đọc `transfer_score.csv` và năm câu peer feedback.
- [ ] Xác định peer sai do guideline thiếu, dữ liệu mơ hồ, thực hiện sai hay gold sai.
- [ ] Chỉ sửa guideline khi có bằng chứng từ blind test.
- [ ] Đổi version thành `v3`.
- [ ] Ghi thay đổi v3 vào `08_revision_log.md`.
- [ ] Kiểm tra guideline cuối không còn `TODO`.

## Definition of Done của Danh

- Guideline có đủ 10 mục, version lần lượt đi qua v1 → v2 → v3.
- Mọi rule có thể thực hiện và kiểm tra trong CVAT.
- Không còn hidden rule chỉ được giải thích bằng miệng.
- Mọi thay đổi v2/v3 có bằng chứng calibration hoặc blind test.

---

# 2. Mạnh — Ontology & CVAT Lead

## Trách nhiệm chính

Mạnh chịu trách nhiệm biến bài toán và guideline thành cấu hình CVAT chạy được. File chính:

- `project/03_ontology_and_cvat_setup.md`
- `project/03_cvat_labels.json`
- Thiết lập và kiểm thử task CVAT calibration
- Hỗ trợ cả nhóm xử lý lỗi kỹ thuật CVAT

## Việc cần làm ngay — Thiết kế ontology

### Bước 1: Đồng bộ với problem statement và guideline

- [ ] Đọc `01_problem_statement.md` và bản nháp guideline.
- [ ] Với mỗi quyết định annotator cần đưa ra, xác định cách biểu diễn nhìn thấy được trong CVAT/export.
- [ ] Không thêm class/attribute nếu downstream contract không cần.
- [ ] Không dùng default mang ý nghĩa thật nếu annotator bắt buộc phải chọn.

### Ontology tối thiểu cần đánh giá

Đây là đề xuất ban đầu; chỉ giữ nếu cả nhóm đồng ý:

| Thành phần | Kiểu | Mục đích đề xuất |
|---|---|---|
| `drivable_area` | Polygon | Geometry chính của vùng đi được |
| `relation_to_ego` | Select | `__undefined__`, `direct`, `alternative`, `unknown` |
| `needs_review` | Checkbox | Escalate một polygon/object |
| `image_escalate` | Tag | Escalate toàn bộ ảnh |

- [ ] Xác nhận nhóm có thật sự cần `relation_to_ego` hay nên dùng class/rule khác.
- [ ] Xác nhận `IGNORE` là không vẽ hay cần label riêng.
- [ ] Xác nhận `UNKNOWN` áp dụng cho attribute nào.
- [ ] Xác nhận checkbox và image tag xuất hiện rõ trong export.

### Bước 2: Hoàn thiện ontology table

Trong `03_ontology_and_cvat_setup.md`, mỗi thành phần cần có:

- [ ] Tên chính xác.
- [ ] Geometry type.
- [ ] Class hay attribute.
- [ ] Danh sách allowed values.
- [ ] Default value.
- [ ] Mutable hay immutable.
- [ ] Lý do tồn tại và downstream use.

Vì bài dùng ảnh độc lập, attribute thường không cần thay đổi theo track. Nếu dùng `__undefined__`, đặt nó đầu danh sách và làm default để phát hiện trường hợp quên gán.

## Tạo `03_cvat_labels.json`

- [ ] Chuyển ontology table sang JSON Raw format của CVAT.
- [ ] Kiểm tra tên label/attribute giống hoàn toàn trong guideline.
- [ ] Kiểm tra geometry đúng là polygon/tag theo thiết kế.
- [ ] Kiểm tra mọi `default_value` nằm trong `values`.
- [ ] Checkbox dùng default `"false"` và `values: ["false"]`.
- [ ] Validate JSON trước khi dán vào CVAT:

```text
py -m json.tool project/03_cvat_labels.json
```

- [ ] Gửi JSON cho Danh review tên và ý nghĩa.
- [ ] Commit và push ontology + JSON sau khi nhóm chốt.

## Dựng task CVAT calibration

Chỉ thực hiện sau khi Hoà hoàn thiện calibration split:

- [ ] Chạy `py lab9.py pack calibration`.
- [ ] Kiểm tra ảnh đã được gom vào `build/calibration/`.
- [ ] Tạo task với tên `ten-nhom-calib-manh`.
- [ ] Dán toàn bộ `03_cvat_labels.json` vào tab **Raw**.
- [ ] Mở tab **Constructor** và kiểm tra từng label/attribute.
- [ ] Upload toàn bộ ảnh trong `build/calibration/`.
- [ ] Giữ sorting method là lexicographical.
- [ ] Dán toàn bộ `02_guideline.md` v1 vào phần **Guide** của task.
- [ ] Mở Job và thử vẽ polygon, gán attribute, tag ảnh, save và export thử.

## Setup test

- [ ] Nhờ một thành viên không trực tiếp dựng task mở task hoặc tự tạo task bằng cùng JSON.
- [ ] Không giải thích miệng trước khi họ thử.
- [ ] Kiểm tra họ có biết chọn tool, label, attribute và escalation hay không.
- [ ] Ghi kết quả setup test vào `03_ontology_and_cvat_setup.md`.
- [ ] Nếu schema sai, sửa JSON trước khi calibration chính thức và yêu cầu mọi người tạo lại task bằng schema cuối.

## Hỗ trợ calibration và peer review

- [ ] Xác nhận cả bốn task calibration dùng cùng JSON, guideline và bộ ảnh.
- [ ] Hướng dẫn thao tác CVAT kỹ thuật nhưng không thống nhất đáp án domain trước khi export.
- [ ] Kiểm tra mọi người lưu bằng `Ctrl+S`.
- [ ] Kiểm tra export dùng **CVAT for images 1.1** và tắt **Save images**.
- [ ] Khi nhận export peer, hỗ trợ tạo review task và upload annotations để cả nhóm xem geometry.

## Definition of Done của Mạnh

- Ontology table và JSON khớp hoàn toàn.
- JSON hợp lệ và tạo task CVAT không lỗi.
- Mọi quyết định LABEL/IGNORE/UNKNOWN/ESCALATE có cách biểu diễn rõ.
- Một thành viên khác vượt qua setup test mà không cần Mạnh giải thích domain rule.

---

# 3. Chu Thái Hoà — Data & Edge-case Lead / Gold Keeper

## Trách nhiệm chính

Hoà chịu trách nhiệm chọn ảnh có mục đích, thiết kế edge case và quản lý gold freeze. File chính:

- `project/sample_pack.csv`
- `project/04_edge_cases/edge_case_cards.md`
- `project/04_edge_cases/gold_decisions.csv`
- Là **người duy nhất** chạy lệnh `freeze` hoặc `--refreeze`

## Việc cần làm ngay — Khảo sát dữ liệu

- [ ] Chạy:

```text
py lab9.py samples --source bdd100k
```

- [ ] Mở và xem toàn bộ 26 ảnh trong `data/bdd100k/` ở kích thước gốc.
- [ ] Với mỗi ảnh đáng chú ý, ghi nhanh:
  - Boundary rõ hay mơ hồ.
  - Có curb/sidewalk/shoulder/parking/intersection không.
  - Có occlusion không.
  - Có low visibility hoặc ảnh negative không.
  - Rule nào của guideline có thể được kiểm thử bằng ảnh đó.

## Hoàn thiện `sample_pack.csv`

Mỗi ảnh chỉ được nằm trong một split:

### Example: 3–5 ảnh

- [ ] Chọn ảnh giúp giải thích rule cơ bản và rule khó trong guideline.
- [ ] Không dùng toàn ảnh dễ; cần ít nhất một ví dụ về boundary/edge case.

### Calibration: 5–8 ảnh

- [ ] Chọn ảnh có khả năng khiến các thành viên hiểu khác nhau.
- [ ] Bao gồm cả ảnh bình thường và ảnh khó.
- [ ] Ưu tiên curb, shoulder, parking, intersection, occlusion hoặc boundary mờ.

### Blind: 4–5 ảnh

- [ ] Chọn ảnh chưa xuất hiện trong example/calibration.
- [ ] Có ít nhất một ảnh tag `normal`.
- [ ] Có ít nhất hai ảnh tag `edge`.
- [ ] Có ít nhất một ảnh tag `critical`.
- [ ] Nếu chọn năm ảnh, có ít nhất một ảnh tag `ambiguity`.
- [ ] Mỗi dòng có `reason` giải thích ảnh đang kiểm thử rule nào.
- [ ] Các tag hợp lệ được ngăn cách bằng dấu chấm phẩy, ví dụ `edge;occlusion`.

Sau khi chia ảnh:

- [ ] Gửi danh sách cho Danh kiểm tra khả năng viết guideline/example.
- [ ] Gửi calibration split cho Mạnh để dựng CVAT.
- [ ] Nhờ cả nhóm review blind set nhưng tuyệt đối không gửi cho peer trước handoff.
- [ ] Commit và push `sample_pack.csv`.

## Viết edge-case cards

- [ ] Bắt đầu `project/04_edge_cases/edge_case_cards.md` ngay khi xem ảnh.
- [ ] Mỗi card phải có sample cụ thể, ambiguity, các lựa chọn có thể xảy ra, expected rule và lý do.
- [ ] Có ít nhất một case critical.
- [ ] Có ít nhất một case cần escalation.
- [ ] Có ít nhất tám card trước khi nộp.
- [ ] Edge-case cards là tài liệu nội bộ; không đưa vào blind pack và không cho peer xem trước khi test xong.

Các case drivable area nên cân nhắc:

- Shoulder hoặc emergency lane nhìn giống làn chính.
- Parking bay nối trực tiếp với mặt đường.
- Intersection không có lane boundary.
- Xe lớn che khuất phần lớn road surface.
- Curb thấp hoặc sidewalk có màu giống mặt đường.
- Median/traffic island nhỏ.
- Bóng tối, tuyết, nước hoặc shadow che boundary.
- Đường vào nhà/private driveway.
- Vùng chạm mép ảnh.
- Alternative route/làn bên cạnh không dành trực tiếp cho ego vehicle.

## Viết `gold_decisions.csv`

Chỉ viết bản cuối sau calibration và sau khi guideline đã lên v2:

- [ ] Mở từng ảnh blind ở kích thước gốc.
- [ ] Viết ít nhất 10 decision.
- [ ] Mỗi ảnh blind có ít nhất một decision.
- [ ] Có ít nhất hai decision severity `critical`.
- [ ] Có ít nhất một decision geometry với `expected` bắt đầu chính xác bằng `geometry:`.
- [ ] Expected phải đủ cụ thể để nhìn export peer là chấm được đúng/sai.
- [ ] Kiểm tra kỹ các decision dạng “không có vùng X” để tránh gold bỏ sót.
- [ ] Gửi gold cho nhóm review nội bộ trước khi freeze; tuyệt đối không gửi cho peer.

## Freeze — chỉ Hoà thực hiện

Trước khi freeze:

- [ ] Guideline đã là v2.
- [ ] `03_cvat_labels.json` đã chốt.
- [ ] `sample_pack.csv` đã chốt.
- [ ] Gold đủ số lượng và severity.
- [ ] Chưa gửi blind package cho peer.

Sau đó chạy:

```text
py lab9.py freeze
git push --follow-tags
```

- [ ] Báo cả nhóm chạy `git pull` và `git fetch --tags --force`.
- [ ] Sau freeze, không sửa `gold_decisions.csv` hoặc `sample_pack.csv`.
- [ ] Nếu thật sự phải sửa trước handoff và chưa nhận bài peer, báo cả nhóm trước rồi chỉ Hoà chạy:

```text
py lab9.py freeze --refreeze
```

- [ ] Push tag mới và yêu cầu mọi người force-fetch tag lại.
- [ ] Không refreeze sau khi đã nhận bài peer.

## Handoff và chấm peer

- [ ] Kiểm tra blind pack không chứa gold hoặc edge-case cards.
- [ ] Khi nhận peer export, hỗ trợ đối chiếu từng gold decision với ảnh gốc.
- [ ] Nếu gold sai mà peer làm đúng theo ảnh, không sửa gold; ghi note bắt đầu bằng `gold sai:`.
- [ ] Cùng nhóm phân tích nguyên nhân các decision sai.

## Definition of Done của Hoà

- Sample pack đúng số lượng, không trùng split và mỗi ảnh có mục đích rõ.
- Blind set đủ `normal`, `edge`, `critical` và `ambiguity` khi cần.
- Có ít nhất tám edge-case cards.
- Gold có ≥10 decision, ≥2 critical và ≥1 geometry decision.
- Chỉ một lịch sử freeze hợp lệ và gold/sample pack không bị sửa sau freeze.

---

# 4. Công việc bắt buộc của cả Danh, Mạnh và Hoà

## Calibration độc lập

Mỗi người phải tự làm toàn bộ calibration; không chia ảnh cho nhau.

- [ ] Tự tạo một task CVAT trên máy mình bằng cùng schema, guideline v1 và ảnh calibration.
- [ ] Tự label tất cả ảnh, không nhìn màn hình hoặc kết quả của người khác.
- [ ] Không thảo luận cách xử lý case mơ hồ trước khi tất cả đã export.
- [ ] Gán đầy đủ attribute; không để `__undefined__` ngoài trường hợp guideline cho phép.
- [ ] Lưu bằng `Ctrl+S`.
- [ ] Export **CVAT for images 1.1**, tắt **Save images**.
- [ ] Đặt file theo tên, ví dụ `danh.zip`, `manh.zip`, `hoang.zip`.
- [ ] Đưa file vào `project/06_calibration_exports/`.

## Blind test cho nhóm khác

- [ ] Đọc `PEER_README.md` trước.
- [ ] Tạo task bằng đúng ảnh, JSON và guideline của nhóm owner.
- [ ] Label theo đúng chữ trong guideline; không đoán ý tác giả.
- [ ] Ghi lại nguyên văn chỗ phải hỏi hoặc không hiểu.
- [ ] Export và trả lời đủ năm câu feedback.

## Review cuối

- [ ] Review guideline v3.
- [ ] Kiểm tra file mình phụ trách không còn `TODO`.
- [ ] Kiểm tra tên label/attribute nhất quán giữa guideline, ontology, JSON và gold.
- [ ] Cập nhật tiến độ trong `TEAM_PROGRESS_DRIVABLE_AREA.md`.
- [ ] Báo Team Leader khi phần việc đã sẵn sàng để chạy `status`/`check`.

## Cách báo hoàn thành

Mỗi người gửi một cập nhật ngắn theo mẫu:

```text
[Tên] — [File/phần việc]
- Đã xong:
- Cần người review:
- Quyết định còn chờ nhóm chốt:
- Commit mới nhất:
- Bước tiếp theo:
```
