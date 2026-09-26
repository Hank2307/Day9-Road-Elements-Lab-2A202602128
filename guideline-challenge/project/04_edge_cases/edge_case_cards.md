# Edge-case library

Tối thiểu **8 card**, khuyến nghị 10–12. Một edge case tốt là case mà hai annotator hợp lý có thể làm khác nhau nếu
guideline chưa rõ. Tám ảnh dễ có label rõ ràng không được tính là edge-case library.

Cần có đủ độ đa dạng: occlusion / truncation / small-far · ambiguous semantics · conflicting road elements · **một case
critical-risk** · **một case guideline cho phép escalation**.

File này là kho nội bộ của nhóm, **không gửi cho peer**. Card dùng ảnh example/calibration thì chép rule + ví dụ sang
`02_guideline.md` (mục 7 và 9) để peer đọc được. Card về ảnh blind chỉ nằm ở đây, và decision của nó phải có trong
`gold_decisions.csv` trước `make freeze`.

`make status` đếm số dòng `CASE ID:` đã điền (đã thay placeholder). Các decision dưới đây là proposal nội bộ theo
scope đã khóa; trước freeze phải đối chiếu lại với guideline v2 và schema CVAT cuối.

---

CASE ID: DA-01
Sample: BDD01
Scene: Highway có nhánh exit và vùng gore kẻ chéo bên phải
Observation: Vùng gore có cùng texture asphalt nhưng bị vạch chéo tách khỏi lane hợp lệ.
Decision: IGNORE gore; LABEL các lane có thể đi bằng polygon riêng theo semantic.
Expected: Không có polygon trên vùng kẻ chéo; path ego hiện tại là `areaType=direct`; nhánh exit chỉ là
`areaType=alternative` nếu ego có thể chuyển vào hợp lệ.
Rationale: Functional area và right-of-way quan trọng hơn màu bề mặt; include gore tạo free-space nguy hiểm.
Common mistake: Tô toàn bộ asphalt và nối lane chính với nhánh exit qua vùng gore.
Diversity: conflict / merge-split / critical-boundary

---

CASE ID: DA-02
Sample: BDD02
Scene: Giao lộ đô thị có crosswalk lớn và nhiều phương tiện
Observation: Crosswalk phủ ngang phần mặt đường hợp lệ; bus và taxi che một phần boundary phía xa.
Decision: LABEL phần crosswalk thuộc path đường; không extrapolate polygon qua vùng bị xe che khi mất bằng chứng.
Expected: Polygon `drivable_area` đi qua phần crosswalk thuộc lane; `areaType` theo path direct/alternative; vùng
không chắc sau phương tiện dùng `needs_review` thay vì đoán.
Rationale: Crosswalk thay đổi ưu tiên với người đi bộ nhưng vẫn là mặt đường phương tiện đi qua khi hợp lệ.
Common mistake: Cắt polygon tại mọi vạch trắng hoặc tô xuyên qua bus/taxi tới boundary không nhìn thấy.
Diversity: intersection / occlusion / ambiguity

---

CASE ID: DA-03
Sample: BDD10
Scene: Đường đô thị dốc với parking lanes và xe đỗ dày hai bên
Observation: Vạch trắng tách travel lane khỏi vùng đỗ xe; nhiều đoạn parking surface bị xe che.
Decision: LABEL travel lane; vùng parking chỉ là `alternative` khi hợp pháp tiếp cận và còn nhìn thấy; không vẽ
xuyên qua xe đỗ.
Expected: `direct` phủ travel lane của ego; polygon parking hợp lệ nếu có phải tách riêng và mang
`areaType=alternative`; sidewalk/curb bị ignore.
Rationale: Parking surface không phải priority path hiện tại và occluded ground không đủ bằng chứng geometry.
Common mistake: Gộp parking lane vào direct hoặc suy diễn mặt đường dưới toàn bộ hàng xe đỗ.
Diversity: conflict / parking / occlusion

---

CASE ID: DA-04
Sample: BDD16
Scene: Đường cong dưới cầu có barrier và vùng kẻ chéo
Observation: Ánh sáng thay đổi mạnh; asphalt sát barrier bị đánh dấu kẻ chéo không dành cho lưu thông.
Decision: IGNORE vùng kẻ chéo và phía ngoài physical boundary; LABEL lane hợp lệ theo đường cong.
Expected: Polygon bám lane marking/barrier nhìn thấy, không tự cắt; `direct` và `alternative` không overlap.
Rationale: Geometry sai gần barrier có thể dạy mô hình lập path vào vùng cấm/nguy hiểm.
Common mistake: Tô tới sát tường vì cùng là asphalt hoặc dùng quá ít điểm làm polygon cắt qua đường cong.
Diversity: low_visibility / curve / critical-boundary

---

CASE ID: DA-05
Sample: BDD04
Scene: Đường dân cư có driveway, curb, scooter và xe đỗ hai bên
Observation: Xe đỗ che road edge; driveway và sidewalk có texture gần giống mặt đường.
Decision: LABEL phần road surface nhìn thấy; IGNORE sidewalk/private driveway ngoài corridor; ESCALATE boundary
không thể xác định sau occlusion.
Expected: Polygon dừng tại evidence cuối cùng; `needs_review=true` nếu curb/road edge không đủ rõ.
Rationale: Extrapolation không kiểm soát có thể include sidewalk/private space vào free-space.
Common mistake: Nối polygon xuyên qua xe đỗ hoặc chạy polygon lên driveway/sidewalk.
Diversity: occlusion / ambiguity / escalation

---

CASE ID: DA-06
Sample: BDD05
Scene: Đường công nghiệp có merge và vùng gore rộng bên phải
Observation: Nhánh bên phải và vùng kẻ chéo tạo nhiều bề mặt asphalt nhưng chức năng khác nhau.
Decision: IGNORE gore; LABEL lane ego là direct và lane có thể nhập hợp lệ là alternative bằng polygon tách biệt.
Expected: Không overlap ngoài chủ đích; không dùng một polygon lớn phủ cả travel lane và vùng kẻ chéo.
Rationale: Direct-vs-alternative accuracy là output semantic chính của task.
Common mistake: Phân loại mọi vùng bên phải là alternative dù bị vạch chéo cấm đi.
Diversity: merge / conflict / semantic

---

CASE ID: DA-07
Sample: BDD12
Scene: Giao lộ nhiều làn với crosswalk, van lớn và lối vào trạm xăng
Observation: Van che horizon; lối vào cơ sở tư nhân nối trực tiếp với mặt đường.
Decision: LABEL các lane/crosswalk nhìn thấy; không tự coi driveway trạm xăng là alternative; ESCALATE nếu rule
về access road chưa đủ phân xử.
Expected: Polygon chính bám lane nhìn thấy và dừng khi mất evidence sau van; object mơ hồ có `needs_review=true`.
Rationale: Task đo vùng road network hợp lệ cho ego, không phải mọi bề mặt xe có thể vật lý chạy vào.
Common mistake: Tô lối trạm xăng chỉ vì cùng asphalt hoặc kéo polygon tới horizon qua van.
Diversity: intersection / occlusion / ambiguity / escalation

---

CASE ID: DA-08
Sample: BDD13
Scene: Phố hẹp với xe tải, pickup và xe ngược chiều che phần lớn mặt đường
Observation: Direct path gần ego nhìn thấy nhưng vùng xa bị phương tiện che nặng.
Decision: LABEL vùng direct có bằng chứng; không extrapolate xuyên qua nhiều phương tiện.
Expected: Polygon không phủ footprint của xe/vật cản và không suy diễn boundary xa; dùng `needs_review` khi phần
direct còn lại không đủ xác định.
Rationale: Include vùng bị chiếm bởi vật cản gần ego là critical failure cho path planning.
Common mistake: Vẽ một polygon lớn từ mép ảnh đến horizon phủ luôn các phương tiện.
Diversity: occlusion / critical / escalation

---

CASE ID: DA-09
Sample: BDD17
Scene: Phố đô thị trời mưa với reflection, marking mờ và xe đỗ
Observation: Nước và phản sáng làm giảm contrast của lane/curb nhưng một phần boundary vẫn quan sát được.
Decision: LABEL theo evidence nhìn thấy; ESCALATE đoạn boundary không đủ tin cậy thay vì dựa vào màu asphalt.
Expected: Polygon bám marking/curb còn thấy; `needs_review=true` nếu boundary quan trọng chỉ được suy đoán.
Rationale: Low visibility dễ tạo geometry drift dù IoU tổng thể vẫn cao.
Common mistake: Dùng reflection làm boundary hoặc kéo thẳng polygon qua đoạn marking mất hoàn toàn.
Diversity: low_visibility / rain / ambiguity / escalation

---

CASE ID: DA-10
Sample: BDD20
Scene: Đường dân cư có parking lanes được kẻ rõ và driveway hai bên
Observation: Parking lane liên tục với road surface nhưng không phải priority path của ego.
Decision: LABEL travel lane là direct; parking lane chỉ là alternative khi hợp pháp và quan sát được.
Expected: Direct và alternative là các polygon riêng, không overlap; xe đỗ và sidewalk không nằm trong polygon.
Rationale: Tách semantic giúp downstream không coi vùng đỗ xe là path ưu tiên.
Common mistake: Gộp từ centerline đến curb thành một direct polygon duy nhất.
Diversity: semantic conflict / parking / direct-vs-alternative

---

CASE ID: DA-11
Sample: BDD18
Scene: Giao lộ ban đêm với crosswalk và xe đỗ hai bên
Observation: Boundary xa, curb và lane marking có độ tin cậy thấp do thiếu sáng.
Decision: LABEL phần chắc chắn; ESCALATE thay vì extrapolate tới horizon.
Expected: Polygon chỉ theo boundary còn nhìn thấy; `needs_review=true` cho object không đủ evidence.
Rationale: Blind case kiểm tra guideline có đường thoát rõ khi annotator không thể resolve bằng ảnh.
Common mistake: Vẽ theo “hình dung con đường” thay vì evidence hoặc bỏ toàn bộ ảnh dù phần gần ego vẫn rõ.
Diversity: blind / low_visibility / ambiguity / escalation

---

CASE ID: DA-12
Sample: BDD24
Scene: Phố hẹp có tuyết, snowbank lấn mặt đường, bus và xe che boundary
Observation: Snowbank thu hẹp vùng đi được gần ego; phần xa bị traffic che gần như hoàn toàn.
Decision: IGNORE snowbank/curb và vật cản; LABEL chỉ phần road surface nhìn thấy còn hợp lệ.
Expected: Direct polygon không cắt vào snowbank hay vehicle footprint; boundary mơ hồ cần `needs_review=true`.
Rationale: Sai boundary gần ego là critical failure vì mô hình có thể lập path vào snowbank hoặc curb.
Common mistake: Dùng road width thông thường để suy diễn qua snowbank và phương tiện.
Diversity: blind / critical / occlusion / low_visibility

---
