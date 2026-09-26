# Peer feedback từ nhóm review

Nhóm đã đọc guideline và xem các ví dụ minh họa. Nhìn chung guideline được trình bày khá đầy đủ, có cấu trúc rõ ràng và có thể sử dụng độc lập trong quá trình gán nhãn. Các quy tắc về phạm vi nhãn, geometry, trường hợp bị che và cách xử lý ảnh không chắc chắn được mô tả cụ thể, giúp annotator có cơ sở để đưa ra quyết định nhất quán.

## 1. Rule nào rõ nhất / giúp quyết định nhanh nhất?

Phần phân biệt `direct`, `alternative` và `background` được trình bày rõ, đặc biệt các quy tắc liên quan đến vạch vàng, vạch trắng, vỉa hè, gore, làn xe đạp và làn ngược chiều giúp annotator nhanh chóng xác định vùng nào cần vẽ và vùng nào cần bỏ qua.

Ngoài ra, quy tắc **dừng `direct` trước xe phía trước**, không kéo polygon vào vùng không còn nhìn thấy và không nối polygon xuyên qua vật che cũng khá trực quan. Checklist cuối guideline giúp kiểm tra lại các lỗi thường gặp trước khi Save/Export.

## 2. Rule nào mơ hồ hoặc phải tự suy diễn?

Nhìn chung các rule chính khá rõ và ít phải tự suy diễn. Một số tình huống phức tạp như giao lộ, làn có vạch trắng liền hoặc vùng đường bị che vẫn cần người annotator quan sát tổng thể để xác định chính xác.

Tuy nhiên guideline đã có cơ chế `needs_review` và `image_escalate` cho các trường hợp chưa đủ bằng chứng, vì vậy những tình huống này không gây ảnh hưởng lớn đến quá trình gán nhãn. Quy tắc **không đoán chiều đi khi chưa đủ bằng chứng** cũng giúp hạn chế việc annotator tự đưa ra quyết định rủi ro.

## 3. Sample nào khiến guideline “vỡ”?

Không phát hiện sample nào khiến guideline bị “vỡ”. Các tình huống được đề cập trong phần examples khá đa dạng, bao gồm cao tốc nhiều làn, đường phố có xe đỗ, làn xe đạp, trời mưa và ảnh có vật che.

Các ví dụ BDD01, BDD04, BDD10 và BDD17 cũng giúp minh họa trực tiếp cách áp dụng các rule trong những trường hợp khác nhau.

## 4. Attribute/default nào trong CVAT dễ gây thao tác sai?

`area_type = __undefined__` là điểm annotator có thể dễ bỏ quên nếu thao tác nhanh. Tuy nhiên guideline đã giải thích khá rõ rằng `__undefined__` có nghĩa là **chưa chọn**, không phải một trạng thái “không biết”.

Việc có checklist yêu cầu kiểm tra tất cả polygon trước khi export cũng giúp giảm khả năng bỏ sót lỗi này.

## 5. Một thay đổi cụ thể giúp annotator mới ít hỏi hơn?

Guideline hiện tại đã khá đầy đủ. Nếu tiếp tục cải thiện, có thể bổ sung thêm một vài hình minh họa trực quan cho các trường hợp dễ nhầm nhất, chẳng hạn:

* `alternative` với background khi mặt đường rộng nhưng không có bằng chứng rõ về làn.
* Làn đỗ xe và làn xe đạp/buffer.
* Cách xử lý `direct` và `alternative` tại giao lộ.
* Trường hợp nào dùng `needs_review` và trường hợp nào phải `image_escalate`.

Việc bổ sung các ví dụ này sẽ giúp annotator mới hình dung nhanh hơn thay vì phải đọc nhiều rule trước khi quyết định. Hiện guideline đã có phần examples và calibration nên đây chủ yếu là cải tiến về tính trực quan, không phải thiếu rule quan trọng.

## Kết luận

* **Mức đánh giá chung:** Tốt, guideline khá rõ ràng và có tính thực hành cao.
* **Lỗi nghiêm trọng:** Không phát hiện.
* **Điểm mạnh:** Rule được tổ chức theo từng nhóm rõ ràng, có nhiều tình huống cụ thể và có cơ chế xử lý ambiguity.
* **Vấn đề nhỏ:** Một số case phức tạp vẫn cần quan sát tổng thể, đặc biệt ở giao lộ và vùng bị che.
* **Đề xuất:** Có thể chấp nhận guideline hiện tại để sử dụng; ở revision tiếp theo nên tăng thêm một số hình minh họa cho các case dễ nhầm để annotator mới thao tác nhanh và đồng nhất hơn.
