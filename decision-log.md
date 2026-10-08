# Curated decision log

This log records analysis decisions and consequential corrections, not private messages or credentials.

| Date | Decision or action | Evidence | Status |
|---|---|---|---|
| 2026-10-08 | Use the course's BC1 1 L kettle BOM and the packaged kettle at factory gate as the declared unit. | Course page and `kettle-bom.csv`; BOM masses sum to 723.00 g kettle + 137.80 g packaging. | Sourced |
| 2026-10-08 | Screen USLCI release 1.2026-09.0 for background process candidates. | Official course link to USLCI/Federal LCA Commons; per-process records are linked in `mapping-decisions.csv`. | First-pass source choice only |
| 2026-10-08 | Keep stainless 304 and suspension-grade PVC as explicit proxies because the BOM does not specify these grades. | Candidate dataset metadata and BOM. | Candidate only; needs student review |
| 2026-10-08 | Prefer the TianGong corrugated-carton record over USLCI containerboard as a finished-packaging candidate, subject to provider and representativeness review. | Historical public process output is corrugated board boxes (normalized to 1 kg) with 83.4% recycled and 16.6% primary fibre. | Provisional candidate only; China data and provider links unresolved |
| 2026-10-08 | Add the TianGong copper-zinc alloy process as a brass candidate, retaining its secondary-copper route and unknown reference year as caveats. | Historical public process record UUID 216385c1-5e30-4122-b31a-afcea87645c0; output 1000 kg brass. | Provisional candidate only; not accepted for calculation |
| 2026-10-08 | Do not calculate GWP or uncertainty before data links, impact method and foreground assumptions are resolved. | Current mapping table has unresolved inputs and provider closure. | Not calculated |

Codex model/version and settings as displayed in the desktop UI: unknown. Codex assistance was used to organize the BOM, screen dataset candidates and draft project documentation. Human review and independent checks of all matches/results: pending.
