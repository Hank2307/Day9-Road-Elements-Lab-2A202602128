# Problem statement + downstream contract

## Bài toán

Gắn polygon vùng ego vehicle có thể di chuyển hợp lệ trong ảnh BDD100K và phân biệt `direct` (path hiện tại/có
priority) với `alternative` (vùng có thể tiếp cận hợp lệ nhưng không phải path hiện tại), nhất là tại intersection,
merge, curb, island và occlusion.

## Downstream contract

1. **User:** Nhóm phát triển/QA mô hình nhận thức không gian lái và lập kế hoạch đường đi cho xe hỗ trợ lái/tự hành.
2. **Output:** Polygon `drivable_area`; attribute `areaType=direct|alternative`; checkbox `needs_review`. Không tạo
   polygon `background`.
3. **Critical failure:** Include sidewalk/median/island/vật cản hoặc vùng không có right-of-way vào `direct`; bỏ sót
   `direct` gần ego/intersection; hoặc gán sai `direct`/`alternative`.
4. **Escalation:** Annotator vẽ phần có bằng chứng, bật `needs_review`; QA owner xem ảnh gốc. Rule chưa đủ được ghi
   thành guideline gap để sửa ở version tiếp theo, không tự đoán.

## Scope

- **Label:** Mặt đường nhìn thấy mà ego đi hợp lệ; `direct` theo lane/hướng/right-of-way hiện tại; `alternative` có
  thể tiếp cận hợp lệ bằng chuyển lane/rẽ/merge; crosswalk trên mặt đường; vùng rời dùng polygon riêng.
- **Ignore:** Sidewalk, curb, median, island, vegetation, barrier, vật cản, private/non-road surface, vùng bị cấm,
  background và phần sau occlusion/horizon không đủ bằng chứng.
- **Geometry:** Bám curb, road edge, island hoặc lane division; sai lệch khoảng ≤5 px tại boundary rõ. Không yêu cầu
  pixel-perfect nhưng không cắt vùng excluded, tự giao, nối giả vùng rời hay extrapolate quá vùng quan sát được.

## Output chấm được

Blind test chấm từ export CVAT: sự hiện diện/số polygon; vùng excluded không có polygon; `areaType`; boundary và
tách vùng; `needs_review=true` khi không đủ bằng chứng.

## Dữ liệu và giới hạn

Chỉ dùng 26 ảnh trong `data/bdd100k/`: 3–5 `example`, 5–8 `calibration`, 4–5 `blind`, không trùng split. Dữ liệu ít,
không phủ mọi tình huống; bài dùng polygon trong khi GT là region/mask nên không kỳ vọng trùng từng pixel. Ảnh độc
lập, không dùng temporal tracking.
