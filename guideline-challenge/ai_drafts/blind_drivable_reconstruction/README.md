# Bộ Drivable Area dựng lại bằng AI

Đúng bộ 5 ảnh sanaka: BDD11, BDD14, BDD18, BDD24, BDD25. Nhãn được tạo offline để owner kiểm tra, chưa có review của người dùng hoặc kiểm thử import trực tiếp trên CVAT.

Đây không phải file nhận từ Just For Fun và không tái tạo chính xác bài họ đã vẽ. Trợ lý đã xem gold trong quá trình chuẩn bị lab nên bộ này không phải blind test độc lập. Không đưa vào project/07_blind_handoff/peer_output hoặc dùng để báo điểm peer/GTS.

## Sử dụng

Tạo task với đúng 5 ảnh gốc và project/03_cvat_labels.json. Chọn Upload annotations → CVAT for images 1.1 → sanaka-drivable-ai-reconstruction-cvat-1.1.zip. ZIP chứa annotations.xml, không kèm ảnh.

Xem contact-sheet.jpg hoặc từng overlay trước khi import. Xanh lá là direct, xanh dương là alternative. Mọi polygon giữ needs_review=true; tag image_escalate mô tả uncertainty của từng ảnh. Giải quyết từng câu hỏi sau review trước khi coi là nhãn hoàn tất.

- BDD11: corridor ego qua crosswalk; kiểm tra biên trái nội suy tại giao lộ.
- BDD14: direct trước xe bạc; alternative hai bên; kiểm tra mảnh xa và boundary shoulder.
- BDD18: chỉ giữ phần ego gần còn nhìn thấy; hướng/làn xa cần escalation.
- BDD24: chừa xe trước và snowbank; biên mặt đường ướt/tuyết cần kiểm tra.
- BDD25: direct trước truck và các phần alternative nhìn thấy; kiểm tra hướng ego, biên làn và footprint taxi.

Kiểm tra hình học không chứng minh semantic đúng hoặc đạt tolerance pixel. VALIDATION.txt ghi kiểm tra offline và hash guideline/schema lúc dựng. Không chỉnh gold, freeze hay sample split.

Tái tạo bằng Anaconda base: chạy build.py trong thư mục này. Chỉnh annotations.json nếu cần sửa tọa độ rồi chạy lại.
