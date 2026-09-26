# Đề xuất chọn ảnh BDD — Drivable Area

> Bản đề xuất hỗ trợ Chu Thái Hoà. Chưa thay đổi `project/sample_pack.csv`. Team Leader và Guideline Lead cần duyệt trước khi Hoà chép các dòng được chọn vào file chính.

## Tóm tắt phương án

- **Example:** 5 ảnh — minh hoạ từ dễ đến khó.
- **Calibration:** 8 ảnh — cố ý chọn các ca có thể làm bốn annotator bất đồng.
- **Blind:** 5 ảnh — chưa xuất hiện ở hai split trên; đủ `normal`, ≥2 `edge`, ≥1 `critical`, ≥1 `ambiguity`.
- **Reserve/unused:** 8 ảnh — giữ dự phòng, không ghi vào `sample_pack.csv` ở phương án hiện tại.

Tổng số ảnh được dùng: **18/26**. Không cần ép cả 26 ảnh vào sample pack; quá nhiều ảnh sẽ làm calibration và blind test vượt time-box.

## Mô tả và phân nhóm toàn bộ 26 ảnh

| Ảnh | Nội dung chính liên quan Drivable Area | Nhóm đề xuất | Vì sao |
|---|---|---|---|
| BDD01 | Highway nhiều làn, nhánh exit bên phải, vùng gore kẻ chéo và barrier | `example` | Ví dụ rõ về split/exit: asphalt ở gore không đồng nghĩa drivable; phân biệt path direct và nhánh alternative. |
| BDD02 | Giao lộ đô thị, crosswalk lớn, nhiều làn, bus/taxi và xe đỗ che biên | `example` | Minh hoạ intersection, crosswalk và occlusion trong bối cảnh dễ hiểu. |
| BDD03 | Highway sáng, lane marking và road edge rõ, guardrail hai bên | `example` | Ca normal đơn giản để minh hoạ polygon direct và alternative trước khi xem ca khó. |
| BDD04 | Đường dân cư, xe đỗ hai bên, driveway/sidewalk và scooter sát curb | `calibration` | Dễ bất đồng về parking edge, curb và phần đường bị xe đỗ che. |
| BDD05 | Đường công nghiệp, vùng kẻ chéo/gore bên phải, lối nhập/tách và barrel | `calibration` | Kiểm tra functional area thay vì tô toàn asphalt; merge/gore dễ phân loại khác nhau. |
| BDD06 | Highway cong nhiều làn, barrier, biên rõ và ít tình huống đặc biệt | `reserve` | Hữu ích nhưng trùng chức năng với BDD03/BDD14; giữ làm ảnh thay thế. |
| BDD07 | Giao lộ dân cư, crosswalk, xe chạy/đỗ dày và biên curb bị che | `calibration` | Kiểm tra intersection, direct/alternative và không extrapolate qua occlusion. |
| BDD08 | Highway nhiều làn với mật độ xe cao, barrier trái và xe che lane phải | `reserve` | Ca occlusion highway tốt nhưng bị trùng với BDD09/BDD14 về loại cảnh. |
| BDD09 | Highway cong, hai xe lớn che phần xa, shoulder/road edge rõ | `reserve` | Có thể thay BDD08; chưa đa dạng bằng các calibration case đã chọn. |
| BDD10 | Đường đô thị dốc, parking lanes hai bên, xe đỗ dày | `example` | Minh hoạ rõ khác biệt giữa travel lane, parking area và sidewalk. |
| BDD11 | Giao lộ dân cư với crosswalk, người đi bộ và xe đỗ sát hai phía | `blind` | Edge case vừa phải: peer phải áp dụng rule crosswalk, curb và occlusion mà không thấy trước. |
| BDD12 | Giao lộ/đoạn phố nhiều làn, crosswalk, van che horizon, lối vào trạm xăng | `calibration` | Geometry khá rõ; dùng để đo quy tắc crosswalk/access road và giới hạn polygon sau van, không coi là ambiguity chính. |
| BDD13 | Đường đô thị hẹp, xe đối diện/xe tải/pickup che phần lớn mặt đường | `calibration` | Kiểm tra không extrapolate quá xa và xử lý vùng direct bị occlusion nặng. |
| BDD14 | Highway nhiều làn, boundary rõ, xe phía trước nhưng ít ambiguity | `blind` | Ảnh `normal` cho blind set; kiểm tra peer có áp dụng đúng rule cơ bản. |
| BDD15 | Đại lộ đô thị nhiều làn, curb/parking bên phải, lane marking rõ | `reserve` | Ca tốt nhưng nội dung đã được BDD10 và BDD20 kiểm tra kỹ hơn. |
| BDD16 | Đường cong dưới cầu, ánh sáng thay đổi, barrier và vùng kẻ chéo | `example` | Minh hoạ boundary vật lý, vùng cấm kẻ chéo và không tô asphalt ngoài functional area. |
| BDD17 | Phố đô thị trời mưa, mặt đường phản sáng, marking mờ và xe đỗ | `calibration` | Không rõ có region alternative riêng hay chỉ direct; dùng để đo bất đồng, nhưng giữ split vì calibration đã bắt đầu. |
| BDD18 | Phố ban đêm, crosswalk, xe đỗ và boundary xa khó thấy | `blind` | Edge + ambiguity + low visibility; đo escalation và giới hạn extrapolation. |
| BDD19 | Đường nhiều làn, curb/lay-by bên phải và xe phía trước | `reserve` | Có thể thay ảnh highway normal nhưng ít ambiguity hơn các ca được chọn. |
| BDD20 | Đường dân cư, parking lanes được kẻ rõ, xe đỗ/driveway/cone hai bên | `calibration` | Kiểm tra parking area có là alternative hay ignore; boundary rõ để thảo luận semantic. |
| BDD21 | Đường cong với physical road edge bên phải và tín hiệu giao thông ở xa | `reserve` | Chi tiết không đủ rõ để khẳng định sidewalk/intersection; giữ dự phòng thay vì đưa vào split sau khi calibration đã bắt đầu. |
| BDD22 | Highway lúc chạng vạng, horizon xa, marking tương đối rõ | `reserve` | Low-light highway nhưng ít edge case; giữ thay BDD14 nếu muốn đa dạng ánh sáng. |
| BDD23 | Đường dân cư có tuyết và xe đỗ hai bên | `calibration` | Review nhóm đánh giá đây là ca calibration yếu; vẫn giữ để không làm mất hiệu lực export đã hoàn thành, chỉ test contrast/tuyết nhẹ. |
| BDD24 | Phố hẹp có tuyết, snowbank lấn đường và nhiều xe phía trước/hai bên | `blind` | Ca critical: sai boundary gần ego có thể include snowbank/curb hoặc bỏ mất path hợp lệ; không mô tả có bus che. |
| BDD25 | Đại lộ chạng vạng/mặt đường ướt, nhiều làn, truck/taxi che biên xa | `blind` | Có ích cho geometry/occlusion/low visibility nhưng không coi là critical mạnh bằng BDD17/BDD18/BDD24. |
| BDD26 | Phố ban đêm, island/curb trái và xe ở bên phải, boundary tối | `reserve` | Ảnh night khó tốt nhưng blind đã có BDD18; giữ để thay nếu BDD18 quá tối. |

## Split đề xuất chi tiết

### Example — 5 ảnh

| Ảnh | Tags | Rule minh hoạ |
|---|---|---|
| BDD03 | `normal` | Direct/alternative trên highway có boundary rõ. |
| BDD01 | `edge;conflict` | Exit split và gore: asphalt không mặc định là drivable. |
| BDD02 | `edge;occlusion` | Intersection, crosswalk và vehicle occlusion. |
| BDD10 | `edge;conflict` | Travel lane so với parking lane/curb. |
| BDD16 | `edge;low_visibility` | Vùng kẻ chéo và physical boundary dưới cầu. |

### Calibration — 8 ảnh

| Ảnh | Tags | Rule cần đo bất đồng |
|---|---|---|
| BDD04 | `edge;occlusion;conflict` | Parking/driveway/curb và extrapolation sau xe đỗ. |
| BDD05 | `edge;conflict` | Merge/gore và functional area. |
| BDD07 | `edge;occlusion` | Giao lộ và boundary bị xe che. |
| BDD12 | `edge;occlusion` | Crosswalk, lối access và giới hạn polygon sau van; geometry nhìn chung rõ. |
| BDD13 | `edge;occlusion;critical` | Direct path bị che nặng bởi nhiều xe. |
| BDD17 | `edge;ambiguity;low_visibility` | Có đủ bằng chứng cho alternative hay chỉ direct trong cảnh mưa. |
| BDD20 | `edge;conflict` | Parking lane là alternative hay ignore. |
| BDD23 | `edge;low_visibility` | Tuyết nhẹ và xe đỗ ảnh hưởng boundary contrast; ca calibration yếu được giữ để đồng bộ export đã làm. |

### Blind — 5 ảnh

| Ảnh | Tags | Rule đang test |
|---|---|---|
| BDD14 | `normal` | Rule cơ bản trên highway có boundary rõ. |
| BDD11 | `edge;occlusion` | Crosswalk, curb và parked vehicles tại intersection. |
| BDD18 | `edge;critical;ambiguity;low_visibility` | Night boundary, crosswalk và escalation khi thiếu bằng chứng. |
| BDD24 | `edge;critical;occlusion;low_visibility` | Snowbank, xe đỗ và critical boundary gần ego. |
| BDD25 | `edge;occlusion;low_visibility` | Geometry trong traffic dày trên mặt đường ướt; không coi là critical chính. |

### Reserve/unused — 8 ảnh

`BDD06`, `BDD08`, `BDD09`, `BDD15`, `BDD19`, `BDD21`, `BDD22`, `BDD26`.

Không ghi các ảnh này vào `sample_pack.csv` trừ khi nhóm quyết định thay một ảnh đã chọn.

## CSV sẵn để Hoà chép sau khi nhóm duyệt

```csv
sample_id,split,tags,reason
BDD03,example,normal,Highway rõ để minh hoạ direct và alternative theo lane marking
BDD01,example,edge;conflict,Exit split và gore kiểm tra functional area thay vì tô toàn asphalt
BDD02,example,edge;occlusion,Intersection và crosswalk minh hoạ boundary qua vùng bị xe che
BDD10,example,edge;conflict,Phân biệt travel lane với parking lane và curb
BDD16,example,edge;low_visibility,Vùng kẻ chéo và barrier dưới cầu minh hoạ physical boundary
BDD04,calibration,edge;occlusion;conflict,Đo bất đồng về parking driveway curb và extrapolation sau xe đỗ
BDD05,calibration,edge;conflict,Đo bất đồng tại merge và vùng gore kẻ chéo
BDD07,calibration,edge;occlusion,Đo bất đồng boundary tại giao lộ có xe chạy và xe đỗ
BDD12,calibration,edge;occlusion,Đo geometry crosswalk lối access và giới hạn polygon khi van che phía trước
BDD13,calibration,edge;occlusion;critical,Direct path bị che nặng bởi xe tải và xe con
BDD17,calibration,edge;ambiguity;low_visibility,Đo có đủ bằng chứng tạo alternative hay chỉ có direct trong cảnh mưa
BDD20,calibration,edge;conflict,Đo semantic parking lane là alternative hay ignore
BDD23,calibration,edge;low_visibility,Đo ảnh hưởng tuyết nhẹ và xe đỗ tới boundary contrast
BDD14,blind,normal,Kiểm tra rule cơ bản trên highway có boundary rõ
BDD11,blind,edge;occlusion,Kiểm tra crosswalk curb và parked vehicles tại intersection
BDD18,blind,edge;critical;ambiguity;low_visibility,Kiểm tra night boundary và escalation khi thiếu bằng chứng
BDD24,blind,edge;critical;occlusion;low_visibility,Kiểm tra snowbank xe đỗ và critical boundary gần ego
BDD25,blind,edge;occlusion;low_visibility,Kiểm tra geometry trong traffic dày trên mặt đường ướt mà không coi đây là critical chính
```

## Những quyết định phải chốt trước khi dùng phương án này

1. Parking lane/parking bay được xem là `alternative` hay `ignore`?
2. Crosswalk nằm trong polygon drivable hay tạo ngắt geometry?
3. Gore/hatched area luôn ignore hay có exception?
4. Có extrapolate qua xe đỗ/xe tải không? Đề xuất hiện tại: không extrapolate quá phần boundary còn quan sát được.
5. Shoulder/emergency lane là `alternative` hay ignore?

Danh cần ghi các câu trả lời vào guideline v1; Mạnh phải bảo đảm schema đủ để biểu diễn quyết định; sau đó Hoà mới chốt `sample_pack.csv`.
