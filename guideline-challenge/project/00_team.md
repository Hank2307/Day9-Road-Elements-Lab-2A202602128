# Team

Điền trước phút 15. Thay mọi placeholder; còn sót thì `make status` báo ở gate G1.

- **Team:** sanaka
- **Nhóm peer test bài của mình:** Just For Fun (JFF), theo xác nhận của Team Leader
- **Nhóm mình test bài của:** Just For Fun (JFF), Traffic light state + ego relevance
- **Problem family:** Drivable area — phân biệt vùng `direct` và `alternative` theo khả năng di chuyển hợp lệ của ego vehicle
- **Nguồn ảnh:** `bdd100k` — chỉ dùng ảnh có sẵn trong `data/bdd100k/`

| Thành viên | MSSV | GitHub | Vai trò chính | File phụ trách |
|---|---:|---|---|---|
| Phạm Hoàng Anh | 02299 | `Hank2307` | Team Leader · integration · QA | `00_team.md`, `01_problem_statement.md`, `05_qa_plan.md`, `07_blind_handoff/`, kiểm tra gate và nộp bài |
| Tống Thanh Danh | 02128 | `thanhdanh11-test` | Guideline Lead | `02_guideline.md`, `06_calibration_report.csv`, `08_revision_log.md` |
| Lê Đức Mạnh | 02122 | `ManhLD424` | Ontology & CVAT Lead | `03_ontology_and_cvat_setup.md`, `03_cvat_labels.json`, `09_cvat_export_or_task_reference.txt` |
| Chu Thái Hoà | 02083 | `chuthaihoa-ai` | Data & Edge-case Lead · Gold Keeper | `sample_pack.csv`, `04_edge_cases/` |

Gợi ý chia vai (nhóm 2–3 người thì gộp): **spec owner** (`01`, `02`), **CVAT owner** (`03_*`, `sample_pack.csv`,
`09`), **gold owner** (`04_edge_cases/`), **QA owner** (`05`, `06`, `07_blind_handoff/`). Mỗi file một người sửa
chính để tránh xung đột git. Calibration thì mọi người cùng label.
