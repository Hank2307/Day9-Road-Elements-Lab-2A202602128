# Hướng dẫn Mạnh — Pull dữ liệu và bắt đầu calibration

Vai trò: **Ontology & CVAT Lead**  
Người thực hiện: **Lê Đức Mạnh — 02122 — `ManhLD424`**

## Quy trình đúng

```text
Pull sample pack
→ Danh hoàn thành guideline v1
→ Mạnh hoàn thành và validate schema
→ cả nhóm xác nhận dùng cùng guideline/schema
→ bắt đầu calibration độc lập
```

Không bắt đầu label chỉ vì đã pull được phần của Hoà. Nếu guideline hoặc JSON chưa chốt, kết quả của bốn người sẽ
không cùng điều kiện và calibration không còn ý nghĩa.

## 1. Bảo vệ thay đổi local

Tại thư mục gốc repository, kiểm tra:

```text
git status
```

Nếu đã sửa ontology hoặc JSON nhưng chưa commit:

```text
git add guideline-challenge/project/03_ontology_and_cvat_setup.md
git add guideline-challenge/project/03_cvat_labels.json
git commit -m "Draft CVAT ontology and labels"
```

Không dùng `git reset`, không xoá file và không ghi đè thay đổi local.

## 2. Pull phần sample và edge cases

Tại thư mục gốc repository:

```text
git pull --rebase origin main
```

Commit phần Data/Edge-case cần nhận được:

```text
23f9561 Complete drivable-area sample and edge cases
```

Kiểm tra ba file:

- `guideline-challenge/project/sample_pack.csv`
- `guideline-challenge/project/04_edge_cases/edge_case_cards.md`
- `guideline-challenge/BDD_IMAGE_SELECTION_RECOMMENDATION.md`

Nếu Git báo conflict, dừng lại và báo Team Leader. Không tự chọn một version rồi xoá version còn lại.

## 3. Chờ và pull guideline v1 của Danh

Chưa dựng task calibration cho tới khi Danh push:

```text
guideline-challenge/project/02_guideline.md
```

Guideline phải:

- Có `Version: v1`.
- Không còn `TODO`.
- Chốt rõ `direct` và `alternative`.
- Chốt parking lane/parking bay.
- Chốt crosswalk.
- Chốt gore/hatched area.
- Chốt shoulder/emergency lane.
- Chốt giới hạn extrapolation qua occlusion/horizon.

Khi Danh báo đã push:

```text
git pull --rebase origin main
```

## 4. Hoàn thiện CVAT schema

Schema phải khớp chính xác với guideline:

- Label `drivable_area`.
- Geometry `polygon`.
- Attribute `areaType`, kiểu select:
  - `__undefined__`
  - `direct`
  - `alternative`
- Default của `areaType`: `__undefined__`.
- Attribute `needs_review`, kiểu checkbox, default `false`.
- Không tạo polygon `background`.
- Dùng **Shape**, không dùng Track vì đây là ảnh độc lập.

Hoàn thiện:

- `project/03_ontology_and_cvat_setup.md`
- `project/03_cvat_labels.json`

Trong thư mục `guideline-challenge/`, validate JSON:

```text
py -m json.tool project/03_cvat_labels.json
```

Lệnh không báo lỗi mới được chuyển sang bước tiếp theo.

## 5. Tạo bộ calibration

Trong thư mục `guideline-challenge/`:

```text
py lab9.py pack calibration
```

Kết quả phải có thư mục:

```text
build/calibration/
```

với đúng 8 ảnh:

- BDD04
- BDD05
- BDD07
- BDD12
- BDD13
- BDD17
- BDD20
- BDD23

Nếu thiếu hoặc thừa ảnh, dừng lại và báo Team Leader.

## 6. Tạo task CVAT riêng

1. Mở CVAT → **Tasks → + → Create a new task**.
2. Đặt tên `sanaka-calib-manh-v1`.
3. Trong phần Labels, mở tab **Raw**.
4. Dán toàn bộ `project/03_cvat_labels.json`.
5. Mở tab **Constructor** và kiểm tra đủ label/attribute.
6. Upload toàn bộ ảnh trong `build/calibration/`.
7. Giữ sorting method là **lexicographical**.
8. Submit và mở Job.
9. Dán toàn bộ guideline v1 vào phần **Guide** của task.
10. Thử:
    - Vẽ polygon.
    - Chọn `areaType=direct` hoặc `alternative`.
    - Bật/tắt `needs_review`.
    - Lưu bằng `Ctrl+S`.
    - Export thử bằng **CVAT for images 1.1**, tắt **Save images**.

Ghi vào `03_ontology_and_cvat_setup.md`:

- Phiên bản CVAT.
- Tên task.
- Đã dán Guide hay chưa.
- Vì sao dùng Shape thay vì Track.
- Kết quả setup test của một thành viên khác.

## 7. Checkpoint trước calibration

Chỉ bắt đầu label khi Team Leader xác nhận cả bốn người dùng:

- Cùng Git commit.
- Cùng `02_guideline.md` v1.
- Cùng `03_cvat_labels.json`.
- Cùng 8 ảnh calibration.

Nếu một người dùng schema hoặc guideline khác, dừng và đồng bộ lại trước khi vẽ.

## 8. Calibration độc lập

- Label toàn bộ 8 ảnh.
- Không xem màn hình hoặc annotation của người khác.
- Không thảo luận đáp án domain trước khi cả bốn người export.
- Có thể hỗ trợ lỗi kỹ thuật CVAT, nhưng không chốt hộ `direct`/`alternative`.
- Gán đầy đủ `areaType`; không để `__undefined__` ngoài trường hợp guideline cho phép.
- Lưu bằng `Ctrl+S`.

Khi xong:

1. Export **CVAT for images 1.1**.
2. Tắt **Save images**.
3. Đặt tên file `manh.zip`.
4. Đưa file vào:

```text
project/06_calibration_exports/manh.zip
```

Không xem export của thành viên khác trước khi file của mình đã hoàn tất.

## 9. Đầu ra Mạnh cần bàn giao

- [ ] `03_ontology_and_cvat_setup.md` hoàn chỉnh, không còn `TODO`.
- [ ] `03_cvat_labels.json` hợp lệ và khớp guideline v1.
- [ ] Task `sanaka-calib-manh-v1` hoạt động.
- [ ] Setup test đã được ghi lại.
- [ ] `manh.zip` chứa annotation độc lập của đủ 8 ảnh.
- [ ] Commit và push các file source do Mạnh phụ trách.
- [ ] Gửi commit hash cho Team Leader.

## Cách báo hoàn thành

```text
Mạnh — Ontology & CVAT
- Guideline commit đang dùng:
- Schema commit:
- JSON validation: PASS/FAIL
- Task CVAT:
- Setup test:
- Calibration export:
- Vướng mắc còn lại:
```
