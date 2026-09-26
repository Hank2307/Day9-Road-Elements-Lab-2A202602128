# Team Progress Tracker — Drivable Area Guideline Challenge

## Cập nhật 2026-09-26 — ưu tiên hơn checklist lịch sử bên dưới

- [x] Anh xác nhận cả nhóm duyệt 8 ảnh AI-assisted, import CVAT và đối chiếu với thành viên khác.
- [x] Kiểm tra offline manh.zip và AI ZIP; lưu số liệu tại project/06_offline_review_evidence.md.
- [x] Hoàn thiện nội dung QA plan và bổ sung provenance/tình trạng setup; chưa coi threshold là đã đo đạt.
- [x] Chốt 5 bất đồng giữa export Mạnh và bản consensus đã được cả nhóm duyệt; lưu trong project/06_calibration_report.csv.
- [x] Nâng guideline lên v2; hoàn thiện QA plan và 15 gold decisions.
- [x] Freeze chính thức; tag gold-freeze tại commit d87fcd27e9df44e79ef1c104b28b2281d0cca81c.
- [x] Tạo handoff/blind-pack.zip gồm 5 ảnh blind; đã kiểm CRC và xác nhận không lộ gold.
- [x] Nhận feedback từ nhóm Just For Fun; peer không báo sample vỡ hoặc lỗi nghiêm trọng.
- [x] Viết guideline v3 với bảng tra nhanh theo góp ý peer.
- [ ] Không có export CVAT trong repo nên không tạo transfer score/GTS giả; nếu Lab Coach yêu cầu điểm thì phải xin lại export.

G1–G4 đạt kiểm tra cơ học. G5–G6 chờ peer output; không tự tạo feedback/GTS/v3. Bản AI-assisted không thay thế calibration độc lập.

Use this file as the shared checklist for the whole lab. Check a box only when the named output is saved in `project/`, committed where appropriate, and the responsible owner plus reviewer agree it is complete.

## Team dashboard

- **Chosen topic:** Drivable area
- **Working topic sentence:** Annotate the visible road surface that the ego vehicle can legally and physically drive on, with explicit rules for curbs, shoulders, parking areas, intersections, occlusion, and uncertain boundaries.
- **Downstream use (proposed):** Free-space perception and safe path planning for an autonomous road vehicle.
- **Data source:** `data/bdd100k/` (26 images)
- **Geometry (proposed):** Polygon
- **Team:** sanaka
- **Team repository:** `https://github.com/Hank2307/Day9-Road-Elements-Lab-2A202602128`
- **Team Leader:** Phạm Hoàng Anh — 02299
- **Guideline Lead:** Tống Thanh Danh — 02128
- **Ontology & CVAT Lead:** Lê Đức Mạnh — 02122
- **Data & Edge-case Lead:** Chu Thái Hoà — 02083
- **Peer group:** _________________________________________
- **Gold keeper — only this person runs freeze:** Chu Thái Hoà (Team Leader reviews before running)
- **Current guideline version:** draft / v1 / v2 / v3
- **Current gate:** G1 / G2 / G3 / G4 / G5 / G6

## Working rules

- [ ] One shared repository has been created from the template.
- [ ] All members are GitHub collaborators and have cloned the repository.
- [ ] Each project file has one primary editor; other members review instead of editing simultaneously.
- [ ] Everyone pulls before editing and makes small, frequent commits.
- [ ] All lab commands are run inside `guideline-challenge/`.
- [ ] `py lab9.py status` or `make status` is run after every phase.
- [ ] CVAT/Docker/Git problems that last more than three minutes are escalated to the Lab Coach.
- [ ] Domain questions are resolved through a written rule, `unknown`, or escalation—not an unwritten agreement.

On this computer, if `py` is unavailable, use:

```powershell
$env:PYTHONUTF8 = "1"
& "C:\Users\pc\anaconda3\python.exe" lab9.py status
```

## Responsibility split

| Area | Primary owner | Reviewer | Done |
|---|---|---|---|
| Team setup and `00_team.md` | Phạm Hoàng Anh | Tống Thanh Danh | [ ] |
| Problem statement | Phạm Hoàng Anh | Tống Thanh Danh | [ ] |
| Guideline writing and versions | Tống Thanh Danh | Phạm Hoàng Anh | [ ] |
| Ontology and CVAT label JSON | Lê Đức Mạnh | Tống Thanh Danh | [ ] |
| Sample selection and split | Chu Thái Hoà | Phạm Hoàng Anh | [ ] |
| Edge-case cards and gold decisions | Chu Thái Hoà | Phạm Hoàng Anh | [ ] |
| Calibration comparison/report | Tống Thanh Danh | Phạm Hoàng Anh | [ ] |
| QA plan | Phạm Hoàng Anh | Lê Đức Mạnh | [ ] |
| Peer handoff and clarification log | Phạm Hoàng Anh | Chu Thái Hoà | [ ] |
| Peer scoring and GTS analysis | Cả nhóm | Phạm Hoàng Anh | [ ] |
| Final check, commit, and push | Phạm Hoàng Anh | Cả nhóm | [ ] |

## Decisions to settle before guideline v1

These are proposals, not hidden answers. Both members must decide and document them in the guideline and ontology.

- [ ] **Annotation unit:** one polygon per contiguous visible drivable surface, or another clearly defined unit.
- [ ] **Ego relevance:** decide whether to label only the ego vehicle's directly drivable area or also alternative/adjacent drivable areas.
- [ ] **Legal versus physical:** decide whether a physically traversable but illegal area is drivable.
- [ ] **Lane markings:** decide whether polygons cross painted lane markings and how markings affect boundaries.
- [ ] **Intersections:** define how far the drivable region extends when lane boundaries disappear.
- [ ] **Parking areas:** define when parking bays/lots count as drivable.
- [ ] **Shoulders and emergency lanes:** label, ignore, or represent as a separate value.
- [ ] **Curbs and sidewalks:** specify the exact stopping boundary.
- [ ] **Medians, traffic islands, vegetation, barriers, and cones:** state that they are excluded and how tightly geometry follows them.
- [ ] **Occlusion:** decide whether to infer the surface behind vehicles or annotate only visible evidence.
- [ ] **Truncation:** define behavior at image edges.
- [ ] **Poor visibility:** establish minimum evidence for night, rain, snow, shadows, or faded boundaries.
- [ ] **Unknown:** define when an attribute/value is `unknown`.
- [ ] **Object escalation:** decide whether to use a `needs_review` checkbox.
- [ ] **Image escalation:** decide whether to use an `image_escalate` tag.
- [ ] **IGNORE:** decide whether ignored regions are simply not drawn or explicitly represented.

### Candidate minimal ontology to evaluate

Keep this only if it serves the downstream contract; revise it before v1 if needed.

| CVAT item | Type | Candidate values/purpose |
|---|---|---|
| `drivable_area` | Polygon | Main annotation geometry |
| `relation_to_ego` | Select attribute | `__undefined__`, `direct`, `alternative`, `unknown` |
| `needs_review` | Checkbox attribute | Object-level escalation |
| `image_escalate` | Tag | Whole-image escalation |

Use `__undefined__` as the default for required choices so forgotten attributes remain detectable. Do not silently default to a semantic answer.

---

## Phase 0 — Environment and team setup (minutes 0–15)

- [ ] Docker Desktop is running.
- [ ] Existing Day 2 CVAT has been started with `docker compose start`.
- [ ] `http://localhost:8080` opens and every member can log in.
- [ ] `py lab9.py cvat` or `make cvat-status` passes.
- [ ] `project/00_team.md` has no `TODO` and assigns one primary editor per file.
- [ ] Peer pairing has been recorded.
- [ ] Run `py lab9.py status`.

**Gate evidence:** Team file complete and all members can use CVAT.

## Phase 1 — Topic lock / G1 (minutes 15–35)

- [ ] Run `py lab9.py samples --source bdd100k` and inspect the available data.
- [ ] Open candidate images at full size before finalizing scope.
- [ ] Finish `project/01_problem_statement.md` and remove every `TODO`.
- [ ] State who consumes the annotations.
- [ ] State exactly what geometry annotators draw and which attributes they answer.
- [ ] State the most costly error for the downstream use.
- [ ] State what annotators do in uncertain cases and how CVAT records it.
- [ ] Confirm the problem can be expressed in CVAT and tested using unseen blind images.
- [ ] Run `py lab9.py status` and confirm G1 passes.

**Stop condition:** The topic fits in one precise sentence and neither member needs an oral explanation to understand it.

## Phase 2 — Guideline v1 and ontology (minutes 35–80)

- [ ] Complete all ten sections of `project/02_guideline.md`.
- [ ] Set `Version:` to `v1`.
- [ ] Define what is included and excluded.
- [ ] Define the polygon boundary and minimum geometry quality.
- [ ] Define all labels and attributes with allowed values.
- [ ] Define occlusion, truncation, low visibility, and ambiguous boundaries.
- [ ] Write explicit `LABEL`, `IGNORE`, `UNKNOWN`, and `ESCALATE` behavior visible in CVAT/export.
- [ ] Write “not used for this task” in the temporal section because these are independent BDD images.
- [ ] Add initial cases to `project/04_edge_cases/edge_case_cards.md`.
- [ ] Include at least one critical case and one escalation case.
- [ ] Complete the ontology table in `project/03_ontology_and_cvat_setup.md`.
- [ ] Both members review v1 only from the written text—no oral repair of unclear rules.

**Final requirement:** `edge_case_cards.md` must contain at least eight cases by submission.

## Phase 3 — Sample pack and CVAT-ready schema / G2 (minutes 80–110)

- [ ] Fill `project/sample_pack.csv`; keep its header unchanged.
- [ ] Assign each selected image to exactly one split.
- [ ] Choose 3–5 `example` images.
- [ ] Choose 5–8 `calibration` images.
- [ ] Choose 4–5 unseen `blind` images.
- [ ] Every row has valid English `tags` separated by semicolons and a clear `reason`.
- [ ] Blind set includes at least one `normal`, two `edge`, and one `critical` image.
- [ ] If blind has five images, include one `ambiguity` image.
- [ ] Write `project/03_cvat_labels.json` from the ontology table.
- [ ] Validate the JSON.
- [ ] Run `py lab9.py pack calibration`.
- [ ] Confirm the images appear in `build/calibration/`.
- [ ] Each member creates a separate CVAT task named like `team-calib-member`.
- [ ] Paste all of `03_cvat_labels.json` into CVAT's **Raw** label editor.
- [ ] Verify every label and attribute in **Constructor**.
- [ ] Upload every calibration image with lexicographical sorting.
- [ ] Paste the entire v1 guideline into the task **Guide**.
- [ ] The member who did not configure the first task performs the setup test.
- [ ] Record the setup-test result in `03_ontology_and_cvat_setup.md`.
- [ ] Run `py lab9.py status` and confirm G2 passes.

## Phase 4 — Independent calibration / G3 (minutes 120–140)

- [ ] Both members annotate all calibration images independently.
- [ ] Do not watch each other's screen or agree on difficult cases beforehand.
- [ ] Check every polygon and required attribute.
- [ ] Save with `Ctrl+S` before export.
- [ ] Export as **CVAT for images 1.1** with **Save images** disabled.
- [ ] Rename exports after annotators and place them in `project/06_calibration_exports/`.
- [ ] Run calibration comparison, for example:

```text
py lab9.py calib project/06_calibration_exports/member-a.zip project/06_calibration_exports/member-b.zip
```

- [ ] Select at least three major disagreements.
- [ ] Fill at least three valid rows in `project/06_calibration_report.csv`.
- [ ] For each disagreement, record both outputs and diagnose `guideline_gap`, `data_ambiguity`, or `execution_error`.
- [ ] Convert guideline gaps into a rule, example, or escalation path instead of oral consensus.
- [ ] Update the guideline to `v2`.
- [ ] Add the v2 change to `project/08_revision_log.md`.
- [ ] Run `py lab9.py status` and confirm G3 passes.

## Phase 5 — QA plan, gold, and freeze / G4 (minutes 140–160)

- [ ] Complete `project/05_qa_plan.md`.
- [ ] Define reviewer, sampling method, severity, metrics, thresholds, PASS/REWORK/REJECT, and issue closure.
- [ ] Inspect every blind image at original size.
- [ ] Fill `project/04_edge_cases/gold_decisions.csv` before the peer sees any blind image.
- [ ] Gold contains at least ten decisions.
- [ ] Every blind image has at least one decision.
- [ ] At least two decisions have severity `critical`.
- [ ] At least one `expected` value begins exactly with `geometry:`.
- [ ] Every expected result is objectively checkable against a peer export.
- [ ] Both members review likely “absence” decisions for missed small/occluded areas.
- [ ] Confirm guideline is `v2` and all sample/schema/gold files are ready.
- [ ] **Only the named gold keeper** runs `py lab9.py freeze`.
- [ ] Gold keeper immediately pushes the freeze commit and tag with `git push --follow-tags`.
- [ ] Other member runs `git pull` and `git fetch --tags --force`.
- [ ] Run `py lab9.py status` and confirm G4 passes.

**Freeze rule:** After freeze, do not edit gold decisions or the sample split. If a pre-handoff correction is essential, only the gold keeper runs `py lab9.py freeze --refreeze`, pushes it, and everyone force-fetches tags again.

## Phase 6 — Blind handoff / G5 (minutes 160–185)

- [ ] Run `py lab9.py handoff`.
- [ ] Inspect `handoff/blind-pack.zip`: it should contain only guideline, labels JSON, blind images, and `PEER_README.md`.
- [ ] Confirm it contains no gold decisions or private edge-case cards.
- [ ] Send the package using the Lab Coach's stated channel.
- [ ] During the 15-minute blind window, do not explain domain rules orally.
- [ ] Log every peer domain question in `project/07_blind_handoff/clarification_log.csv`.
- [ ] Do not log purely technical CVAT/Docker questions.
- [ ] In parallel, open the other team's package and read `PEER_README.md` first.
- [ ] Create a new peer CVAT task using their images, labels JSON, and guideline.
- [ ] Annotate strictly from their written guideline; do not guess their intent.
- [ ] Export your peer result and answer all five feedback questions.
- [ ] Send the export and feedback back through the designated channel.
- [ ] Receive the peer's export for your project.
- [ ] Run `py lab9.py status` and confirm G5 passes when the required output exists.

## Phase 7 — Score and diagnose (minutes 185–205)

- [ ] Run `py lab9.py score "<path-to-peer-export.zip>"`.
- [ ] Fill every `correct` cell in `project/07_blind_handoff/transfer_score.csv` with `1` or `0`.
- [ ] Add an evidence-based note for every decision.
- [ ] Review geometry visually in CVAT when the export summary is insufficient.
- [ ] If frozen gold is wrong, still score against it and start the note with `gold sai:`.
- [ ] Run `py lab9.py gts`.
- [ ] Record the GTS result and identify the largest transfer failure.
- [ ] Copy all five peer feedback answers into `project/07_blind_handoff/peer_feedback.md`.
- [ ] Classify each failure as guideline gap, data ambiguity, execution error, or incorrect gold.
- [ ] Decide whether to revise, add escalation, or reject feedback with evidence.

GTS weights: 60% decision accuracy, 20% critical accuracy, 10% geometry, and 10% independence.

## Phase 8 — Guideline v3 and submission / G6 (minutes 205–240)

- [ ] Revise `project/02_guideline.md` from blind-test evidence—not from preference alone.
- [ ] Set guideline version to `v3`.
- [ ] Add the v3 entry to `project/08_revision_log.md`.
- [ ] Ensure `edge_case_cards.md` has at least eight cases, including critical and escalation cases.
- [ ] Complete `project/09_cvat_export_or_task_reference.txt`.
- [ ] Remove every remaining `TODO` in `project/`.
- [ ] Run `py lab9.py status` and resolve every incomplete gate.
- [ ] Run `py lab9.py check` and resolve every failure.
- [ ] Member B reviews the final Git diff and confirms gold/sample files were not changed after freeze.
- [ ] Commit and push:

```text
git add project
git commit -m "Day 9 project submission"
git push --follow-tags
```

- [ ] Confirm the final commit and `gold-freeze` tag are visible in the shared repository.
- [ ] Prepare the two-minute debrief: where the guideline failed, what changed in v3, and what the peer found hardest.

## Daily status log

| Time | Gate/phase | Completed | Blocker/next action | Owner |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Final acceptance checklist

- [ ] A new annotator can tell what to label and what not to label without asking.
- [ ] Every difficult case leads to a written decision or an explicit escalation path.
- [ ] CVAT labels exactly match the ontology and do not hide missing choices behind semantic defaults.
- [ ] Calibration produced at least three analyzed disagreements and concrete v2 changes.
- [ ] Frozen gold contains ≥10 decisions, ≥2 critical decisions, and ≥1 geometry decision.
- [ ] Blind testing remained independent and every domain question was logged.
- [ ] Peer results were fully scored with evidence and GTS was calculated.
- [ ] Guideline v3 is supported by blind-test evidence.
- [ ] All six gates pass and `py lab9.py check` succeeds.
