# Review trực quan các ảnh JFF trả lại

Nguồn do Anh cung cấp: thư mục `C:\Users\pc\Desktop\BDD11,BDD14,BDD18`. Đã lưu nguyên file PNG trong `peer_images/`, đủ BDD11/14/18/24/25. Phản hồi nguyên văn được lưu tại `peer_feedback_original.md`.

Các ảnh hiển thị tiêu đề “JFF annotation with AI assist” và “JFF acceptance confirmed by Pham Hoang Anh”, với vùng vẽ khớp trực quan bộ AI dựng trước đó. Theo Anh, JFF đã review/chấp nhận bộ này và trả lại các ảnh. Không coi các ảnh là chứng cứ về một lượt blind độc lập: trợ lý đã tiếp xúc gold khi dựng nhãn.

Ảnh có thanh tiêu đề cao 56 px; không dùng tọa độ của preview làm tọa độ ảnh gốc. Xanh lá biểu diễn direct, xanh dương biểu diễn alternative. Màu hiển thị không chứng minh attribute/tag thật trong CVAT.

| Ảnh / gold decision | Quan sát | Kết luận trong phạm vi ảnh |
|---|---|---|
| BDD11 d1 | Vùng xanh lá ở phía ego, bên phải đường giữa | Phù hợp trực quan; biên giao lộ chưa đo pixel |
| BDD11 d2 | Vùng đi qua crosswalk, chừa xe đỗ và sidewalk | Phù hợp trực quan |
| BDD11 d3 | Không có vùng xanh dương | Phù hợp với không vẽ alternative; chưa kiểm enum XML |
| BDD14 d1 | Direct dừng sau xe bạc | Phù hợp trực quan |
| BDD14 d2 | Có alternative phía trái | Phù hợp trực quan |
| BDD14 d3 | Biên phải dừng phía trong vạch trắng ngoài cùng | Không thấy lấn shoulder rõ; chưa đo tolerance |
| BDD18 d1 | Có direct ngắn ở phần đường gần còn nhìn thấy | Phù hợp cách xử lý bảo thủ |
| BDD18 d2 | Không có sidebar/tag/reason trong PNG | Không thể xác minh image_escalate từ ảnh |
| BDD18 d3 | Vùng vẽ chừa mui xe và xe đỗ | Phù hợp trực quan |
| BDD24 d1 | Direct dừng trước xe trắng | Phù hợp trực quan |
| BDD24 d2 | Vùng vẽ chừa phần tuyết chất đống | Phù hợp trực quan; biên tuyết cần kiểm pixel nếu chấm geometry |
| BDD24 d3 | Không có vùng xanh dương | Phù hợp với không vẽ alternative |
| BDD25 d1 | Direct dừng ở phần xa trước traffic/truck | Phù hợp quy tắc dừng bảo thủ; hướng lane ego vẫn cần thận trọng |
| BDD25 d2 | Có alternative hai bên | Phù hợp trực quan |
| BDD25 d3 | Polygon chừa truck/taxi, không kéo tới horizon | Phù hợp trực quan; chưa đo biên sát xe |

Đây là review định tính, không chuyển các dòng trên thành correct=1 tự động. Gold là bảng expected decisions, không phải mask tham chiếu, nên không thể khẳng định IoU=1 hoặc “khít gold” bằng số đo.

## Đánh giá chuyển giao

- Peer feedback: guideline rõ, không báo lỗi nghiêm trọng; đề nghị tăng tính trực quan.
- Owner response: guideline v3 bổ sung bảng tra nhanh, giữ nguyên schema.
- D/C/G: chưa có phép chấm định lượng đầy đủ từ export độc lập và geometry reference.
- I: chưa có xác nhận số câu hỏi trong blind window. Clarification log chỉ có header không được hiểu là 0 câu hỏi.
- GTS: không tính trong hồ sơ này. Bộ AI được chấp nhận có ích cho review nhưng không đủ chứng minh independence.

Không sửa gold hoặc sample pack sau freeze. Không tự đổi tolerance hoặc chấm toàn bộ PASS vì tổng thể ảnh tương tự.
