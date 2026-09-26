# Drivable Area — Topic Reference

> Tài liệu tham chiếu nội bộ do Team Leader cung cấp. Dùng tài liệu này để giữ scope nhất quán khi hỗ trợ nhóm viết problem statement, guideline, ontology, edge cases và QA.
>
> **Ràng buộc của lab hiện tại:** chỉ dùng ảnh đã có trong `data/`. Phần “tải sample có ground truth” bên dưới là kiến thức tham khảo; không đưa ảnh tải ngoài vào `sample_pack.csv` trừ khi Lab Coach cho phép rõ ràng.

## Định nghĩa cốt lõi

Drivable area là **polygon mô tả không gian ego có thể đi theo rule**, không phải “tô hết asphalt”.

Việc xác định vùng đi được phải dựa trên chức năng giao thông, hướng di chuyển, right-of-way, curb, island, sidewalk và vật cản; không chỉ dựa trên màu hoặc texture của bề mặt.

## 1. Hệ lớp tham chiếu từ BDD100K

BDD100K sử dụng ba lớp `direct`, `alternative` và `background`:

| Class | Ý nghĩa vận hành | Rule cho bài tập |
|---|---|---|
| `direct` | Current ego driving area / priority | Polygon vùng ego có thể đi trực tiếp theo lane và hướng hợp lệ hiện tại; ưu tiên boundary quan sát được. |
| `alternative` | Other accessible lane/area | Polygon riêng cho vùng có thể tiếp cận bằng chuyển lane hoặc lựa chọn hợp lệ khác nhưng không phải path hiện tại. |
| `background` | Không tính trong BDD evaluation | Không cần tạo polygon `background` trong CVAT practice. |

### Diễn giải direct và alternative

- `direct`: vùng xe hiện đang đi hoặc có priority/right-of-way để tiếp tục đi.
- `alternative`: lane hoặc vùng xe chưa đi hiện tại nhưng có thể tiếp cận hợp lệ, ví dụ bằng chuyển lane.
- Không gộp `direct` và `alternative` chỉ để tạo polygon đẹp hoặc đơn giản hơn.

## 2. Quy tắc polygon — quy ước lớp học

### Functional area, not color

- Không tô toàn bộ vùng có texture asphalt.
- Xét curb, island, sidewalk, hướng giao thông, right-of-way và vật cản theo SOP.
- Bề mặt trông giống đường chưa đủ để kết luận là drivable area.

### Direct và alternative

- Nếu schema biểu diễn cả hai loại, phải tách thành các region rõ ràng.
- Tránh overlap không chủ đích giữa `direct` và `alternative`.
- Vẽ `direct` trước, sau đó mới vẽ `alternative`.

### Intersection và merge

Intersection và merge là các vùng cần decision log nhiều nhất. Guideline của nhóm phải quy định rõ:

- Crosswalk ảnh hưởng đến polygon thế nào.
- Turn lane được xem là `direct`, `alternative` hay excluded trong từng điều kiện.
- Merge lane được chuyển từ `alternative` sang `direct` theo rule nào.
- Waiting zone hoặc vùng chờ được label thế nào.
- Boundary được xác định thế nào khi lane marking biến mất.

### Occlusion và horizon

- Không kéo polygon sâu vào vùng không còn quan sát được, trừ khi guideline cho phép extrapolation rõ ràng.
- Nếu cho phép extrapolation, guideline phải nêu điều kiện, giới hạn và cách đánh dấu uncertainty.

### Disconnected regions

- Tạo nhiều polygon nếu các vùng hợp lệ tách rời nhau.
- Không tạo polygon self-intersecting để giả lập hole hoặc nối các vùng rời rạc.
- Nếu bài toán thật sự cần hole hoặc pixel-perfect mask, nên chuyển sang mask workflow thay vì ép vào polygon workflow.

## 3. Schema CVAT đề xuất

### Label và attributes

- Label: `drivable_area`
- Geometry: polygon
- Attribute: `areaType`
  - `__undefined__`
  - `direct`
  - `alternative`
- Attribute tùy chọn cho lớp học: `needs_review`
- Có thể thêm image-level tag nếu nhóm cần escalate toàn ảnh.

`__undefined__` nên là default nếu muốn phát hiện annotator quên chọn `areaType`. Không dùng `direct` làm default vì có thể tạo lỗi semantic âm thầm.

### Thao tác CVAT

1. Chọn **Polygon → Shape → `drivable_area`**.
2. Click các điểm theo physical/logical boundary.
3. Tránh đặt quá nhiều điểm trên đoạn thẳng.
4. Giảm opacity vừa đủ để nhìn thấy lane marking và curb bên dưới khi chỉnh boundary.
5. Vẽ các polygon `direct` trước.
6. Vẽ các polygon `alternative` sau.
7. Kiểm tra và loại bỏ overlap không chủ đích.

## 4. Peer QC

Reviewer ưu tiên tìm ba nhóm lỗi:

1. Sidewalk, median hoặc traffic island bị include.
2. Turn lane hoặc alternative lane hợp lệ bị bỏ sót.
3. Polygon bị extrapolate quá xa khỏi vùng còn quan sát được.

Ngoài ra cần kiểm tra:

- Sai `areaType` giữa `direct` và `alternative`.
- Polygon gần ego vehicle có critical boundary error.
- Các vùng rời nhau bị nối bằng polygon không hợp lệ.
- Boundary tại intersection/merge không tuân theo guideline.

## 5. Ground-truth comparison

- Có thể so polygon với BDD drivable mask bằng overlay alpha hoặc IoU trực quan.
- Không kỳ vọng polygon của bài tập trùng boundary từng pixel với mask ground truth.
- Cần xem cả overlap tổng thể và lỗi boundary cục bộ.
- Ground truth là bằng chứng tham khảo, không thay thế rule đã viết và freeze của nhóm.

## 6. Metric luyện tập đề xuất

| Metric | Dùng để đánh giá |
|---|---|
| Mask/region IoU | Mức overlap tổng thể với ground truth. |
| Boundary error / visual boundary audit | Sai curb, island, crosswalk hoặc boundary cục bộ dù IoU tổng vẫn cao. |
| Direct-vs-alternative accuracy | Lỗi semantic của `areaType`. |
| Critical boundary error count | Lỗi gần ego vehicle hoặc intersection có hậu quả downstream lớn. |

## 7. Sample-set tham khảo

Một practice set đầy đủ có thể gồm 12–15 ảnh:

- Ít nhất 4 ảnh intersection/merge.
- Ít nhất 2 ảnh có island/median.
- Ít nhất 2 ảnh có parked vehicles/occlusion.
- Ít nhất 2 ảnh night/rain nếu dữ liệu có.

Trong lab hiện tại, phải ánh xạ các mục tiêu này vào ba split từ bộ ảnh BDD có sẵn:

- `example`: 3–5 ảnh.
- `calibration`: 5–8 ảnh.
- `blind`: 4–5 ảnh chưa xuất hiện trong hai split trên.

Blind set vẫn phải đáp ứng tag theo lab: ít nhất một `normal`, hai `edge`, một `critical`, và nếu dùng năm ảnh thì có một `ambiguity`.

## 8. Nguồn dữ liệu và tài liệu tham khảo

### Nguồn chuẩn

- BDD100K data portal: 100K Images và Drivable Area annotations.
- Official preparation documentation liệt kê cặp dữ liệu này cho task drivable area.

### Nguồn nhẹ tham khảo

- FiftyOne mirror `dgural/bdd100k` có field drivable dạng Segmentation và media validation.
- Có thể dùng `max_samples` để lấy một batch nhỏ trong bài tập khác; không dùng ảnh tải thêm cho lab hiện tại nếu chưa được cho phép.

### Links

- [BDD100K drivable-area format](https://github.com/bdd100k/bdd100k/blob/master/doc/source/format.rst)
- [BDD100K paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yu_BDD100K_A_Diverse_Driving_Dataset_for_Heterogeneous_Multitask_Learning_CVPR_2020_paper.pdf)
- [BDD100K data portal](https://bdd-data.berkeley.edu/)
- [CVAT Academy — Polygon and Polyline Annotation](https://www.cvat.ai/academy/polygon-and-polyline-annotation)
- [CVAT documentation — Shapes](https://docs.cvat.ai/docs/annotation/manual-annotation/shapes/)

## 9. Những quyết định nhóm vẫn phải chốt

Tài liệu tham chiếu này chưa tự động trở thành guideline. Nhóm vẫn phải ghi quyết định cụ thể vào `project/02_guideline.md`:

- “Direct path” kéo dài tới đâu trong intersection?
- Làn cùng hướng bên cạnh luôn là `alternative`, hay chỉ khi ego có thể chuyển lane hợp lệ?
- Turn lane có được label nếu ego hiện không ở làn đó?
- Crosswalk có nằm trong polygon hay tách boundary?
- Shoulder và emergency lane được exclude hay `alternative`?
- Parking bay/parking lot được exclude hay `alternative`?
- Có extrapolate qua parked vehicle/occlusion không?
- Boundary tại horizon dừng ở bằng chứng nhìn thấy nào?
- `needs_review` được bật trong điều kiện cụ thể nào?
- Khi nào escalate toàn ảnh thay vì một polygon?

Các câu trả lời phải nhất quán giữa problem statement, guideline, ontology table, CVAT JSON, edge-case cards, QA plan và gold decisions.
