# BC1 kettle cradle-to-gate LCA (working project)

> **Status: preparation only.** The BOM mass check is complete, but the life-cycle inventory and impact calculation are not. No GWP result is reported. This README records the project as it currently exists and leaves unresolved information visible.

## 1. Study identity and purpose

- **Study title:** Cradle-to-gate LCA of one packaged BC1 1 L plastic electric kettle.
- **Public student/group alias:** unknown; choose a non-identifying alias before publishing.
- **Repository URL:** unknown; no GitHub repository has been created or linked yet.
- **Run identifier:** `kettle-bc1-independent-2026-10-08` (preparation record only).
- **Study date:** 2026-10-08.
- **Goal:** establish a reproducible baseline for the course's common declared unit, then compare one documented modeling choice in a later revised run.
- **Run status:** intended independent baseline; no LCA result or Git tag exists yet.

See [`run-manifest.json`](run-manifest.json) and [`decision-log.md`](decision-log.md). Full name and email belong only in the course submission form.

## 2. Product, declared unit and system boundary

- **Declared unit:** one manufactured and packaged BC1 1 L plastic electric kettle at the factory gate.
- **Product specification:** BC1 is the course's representative base case, not a named commercial product.
- **BOM:** course-provided file, copied from the user's Downloads folder on 2026-10-08; the private local path is omitted from this public README. Course source: [EU Electric Kettles preparatory study (2020)](https://publica-rest.fraunhofer.de/server/api/core/bitstreams/3df3f4d6-3717-4261-99e3-a232323111d6/content), Task 4, Tables 4-3, 4-4 and 4-8 (printed pp. 26, 27 and 30). Source publication date is 2020; original download date is unknown.
- **Mass check:** 723.00 g kettle + 137.80 g packaging = 860.80 g packaged product. The executable check is [`results/independent/bom-check.json`](results/independent/bom-check.json).
- **Included in the common factory-gate boundary:** materials, component manufacture, assembly and packaging.
- **Excluded:** customer delivery, use and end of life. Any later extension must be reported separately.
- **Geography, product reference year and cut-off criteria:** unknown; the course brief does not specify them.

## 3. Foreground inventory and quantitative assumptions

The finished material masses are course-sourced. See [`kettle-bom.csv`](kettle-bom.csv) for all 12 entries, [`foreground-inventory.csv`](foreground-inventory.csv) for finished-mass conversions to kilograms, and [`results/independent/bom-check.json`](results/independent/bom-check.json) for the mass check. Purchase amounts remain unknown because manufacturing yields were not supplied.

| Parameter | Current value | Unit | Evidence/status |
|---|---:|---|---|
| Kettle material mass | 723.00 | g/kettle | Sourced; BOM |
| Packaging mass | 137.80 | g/packaged kettle | Sourced; BOM |
| Total finished mass | 860.80 | g/packaged kettle | Calculated; mass check passed |
| Material grade for stainless steel | unknown | — | BOM does not specify grade |
| Nylon grade | unknown | — | BOM does not specify grade |
| Manufacturing losses/yields and scrap | unknown | — | No supporting data found in supplied files |
| Component conversion services | unknown | — | Not quantified or matched yet |
| Assembly electricity | unknown | — | Not specified in supplied files |
| Factory/inbound transport | unknown | — | Not quantified; boundary and evidence need review |
| Prices/monetary proxies | not used | — | No monetary proxy selected |

Mass conversion is `finished_mass_kg = finished_mass_g / 1000`. If a manufacturing yield `y` is later sourced, required purchased material is `finished_mass_kg / y`; no yield adjustment has been applied. Background-process activity must be normalized by its reference flow and unit. Process conversion and energy burdens already included in each dataset must be checked before adding foreground processes to avoid double counting.

## 4. Background data and matching decisions

USLCI release **1.2026-09.0** was selected for a first-pass public-data search. The official GitHub repository documents the release and links to the actual release data, which is hosted through Federal LCA Commons (recent JSON-LD links may redirect to Box). We have reviewed the official source and screened five Commons process records, but have not downloaded the complete database archive or individual process JSON-LD files. All five matches remain provisional, and provider closure has not been completed. See [`source-notes.md`](source-notes.md) for the GitHub repositories used and exact retrieval status.

| BOM input | Candidate | Key caveat |
|---|---|---|
| Stainless steel | [Steel; stainless 304; flat rolled coil](https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/dataset/PROCESS/49f5324b-fc33-36e9-b5af-3c80d73492bd) | BOM grade unspecified; 304 is a proxy. Dataset notes European producer technology with American electricity; older data. |
| PP | [Polypropylene, PP; virgin resin; at plant](https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/dataset/PROCESS/2e8facf6-46aa-4ddb-95de-a4e2a00eb2bb) | Virgin resin is a direct material candidate; process technology and upstream supplier closure still need review. |
| PVC | [Polyvinyl chloride resin; suspension grade PVC; at plant](https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/dataset/PROCESS/3dbccdda-2014-4239-ad1f-4e15c034942b) | BOM grade unspecified; suspension grade is a proxy. 2022 US data. |
| ABS | [Acrylonitrile-butadiene-styrene, ABS; copolymer resin; at plant](https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/dataset/PROCESS/0e42a306-ee2d-362e-8bc3-580000096459) | North American 2015–2016 data; process description calls it gate-to-gate while saying upstream raw materials and incoming transport are included. Boundary needs review. |
| Cardboard packaging | [Corrugated carton production](https://github.com/tiangong-lca/data/blob/c50cab7961e0b0ca11c26a600bd4c90fea6c6c32/tiangong_lca_data/processes/b0a8d882-9859-4069-b59b-90dd19dc98a0.xml) | Closer finished-carton candidate than the USLCI containerboard intermediate; China data, provider links, and representativeness still need review. Product flow is 83.4% recycled and 16.6% primary fibre. |

Complete USLCI UUID/version, geography, year, reference flow, search query, alternatives, rationale, included burdens and provider-link status: [`mapping-decisions.csv`](mapping-decisions.csv). TianGong public GitHub process candidates and rejected matches are separately recorded in [`tiangong-github-screening.md`](tiangong-github-screening.md). The TianGong screen has provisional PP, PVC, brass-alloy, copper, LDPE-resin and corrugated-carton records; nylon filament was rejected as an incomplete resin proxy. Stainless steel, POM, PC, ABS and silicone still have no accepted direct match. Candidate dataset files have not been copied locally, so no local dataset file hashes are available. The USLCI release record is documented at the [official USLCI release page](https://github.com/FLCAC-admin/uslci-content/blob/dev/docs/release_info/release-downloads.md).

These are unit-process candidates, not cumulative impact factors or monetary proxies. No candidate is accepted for calculation until reference units, boundary and upstream providers are checked.

## 5. Calculation and impact-assessment methods

- **Calculation status:** not calculated.
- **Planned algorithm:** if the selected data support an inventory matrix, solve `A s = f` for process activities, calculate elementary flows `g = B s`, then characterize impacts `h = C g`. The actual matrix construction and solver are not implemented yet.
- **Process scaling/provider linking:** not performed; unresolved providers must be reported rather than set to zero.
- **Allocation, system model, recycling/scrap treatment and credits:** unknown.
- **Impact method/version, GWP100 time horizon, biogenic carbon and elementary-flow matching:** unknown; no method has been selected.

## 6. How to reproduce the analysis

Current project files:

- `kettle-bom.csv` — course input.
- `foreground-inventory.csv` — finished BOM quantities in grams and kilograms; no yield assumptions or purchase quantities.
- `mapping-decisions.csv` — candidate match record.
- `data-manifest.csv` — source locations and SHA-256 hashes for available local artifacts.
- `run-manifest.json` — current run metadata.
- `decision-log.md` — curated modeling decisions; no private messages or credentials.
- `source-notes.md` — official GitHub sources and which data were actually retrieved.
- `tiangong-github-screening.md` — material searches and provisional records from TianGong's historical GitHub snapshot.
- `submission-checklist.md` — fields in the course's final submission form and current readiness.
- `src/check_bom.py` — standard-library BOM mass check only.
- `results/independent/bom-check.json` — generated mass check, not an LCA result.

The BOM check requires Python 3.11+ and no third-party packages. From the repository root run:

```powershell
python src/check_bom.py --bom kettle-bom.csv --output results/independent/bom-check.json
```

The check was run here with Python 3.12.14 on Windows; installed user OS version is unknown. No dependency lockfile is needed for this check. It does not retrieve data or calculate impacts.

Public TianGong process candidates were screened directly in the historical [TianGong GitHub data repository](https://github.com/tiangong-lca/data) without logging in; see [`tiangong-github-screening.md`](tiangong-github-screening.md). This is an archived snapshot, not current live data. The official [TianGong CLI](https://github.com/tiangong-lca/cli) supports authenticated platform searches, but it currently fails to launch in this Windows environment with a filesystem `EPERM` error. No TianGong account session or live platform query has been used. The course page says automated Federal LCA Commons API use needs a free data.gov API key; manual Commons browsing does not establish that one was used here. If the automated API route is selected, document its setting name and local setup without recording the key. Never commit credentials, `.env` files, session files or restricted data dumps. Current `.gitignore` excludes common credential/session files and raw downloads.

## 7. Results, checks and interpretation

- **LCA calculation:** not calculated; GWP100 total and contribution breakdown are not available, not zero.
- **BOM unit and mass checks:** passed — 12 materials; kettle 723.00 g; packaging 137.80 g; total 860.80 g.
- **Supplier closure, contribution-sum and double-counting checks:** not performed because no product system has been assembled.
- **Generated file:** [`results/independent/bom-check.json`](results/independent/bom-check.json), a BOM mass check only.
- **Interpretation:** no climate-impact or contribution claims can be made from this preparation state.

## 8. Uncertainty and sensitivity

Not calculated. There is no complete product system or impact result, and the key assumptions, provider matches and characterization method remain unresolved. No distributions, correlations, Monte Carlo draws, seed, convergence check, mean/median or P05/P95 are available.

## 9. Codex and human decisions

- **Codex model/version and runtime settings as displayed:** unknown in the available project record.
- **Codex assistance:** BOM organization, first-pass public USLCI candidate screening, mass-check script and documentation draft; details of decisions are in [`decision-log.md`](decision-log.md).
- **Student decisions still required:** alias, proxy approval, remaining dataset matches, system geography/reference year, foreground assumptions, characterization method and later revised-run choice.
- **Independent human verification:** pending. No private messages, contact details or credentials are included.

## 10. Independent and revised runs

The current folder is an independent-run preparation area, but no full independent LCA output, Git commit or tag exists yet. Preserve this baseline before comparing with classmates. No revised run has been made; revision comparison is not applicable at this stage. Do not embed a future README commit hash in this file.

## Unresolved information to review before commit and push

1. Public alias and public GitHub repository URL.
2. Stainless and nylon grades, plus geography and product reference year.
3. Losses/yields, component conversion, assembly electricity, factory/inbound transport and scrap treatment.
4. Accepted matches and provider closure for brass, copper, nylon, POM, PC, silicone, LDPE foil and finished carton.
5. Provider closure and the burdens already included in each selected dataset.
6. Allocation/system model, characterization method and GWP100 flow mapping.
7. TianGong/Commons data retrieval route and any required local account/API configuration.
8. Complete result, contribution, balance and double-counting checks, followed by uncertainty/sensitivity if feasible.
9. Exact Codex model/settings if the UI exposes them, and a human-reviewed independent run before public submission.

The final submission form requires the public repository URL and exact 40-character commit SHA after the public repository is created and pushed. The course submission code is an instructor-provided form code, not a GitHub/TianGong credential. See [`submission-checklist.md`](submission-checklist.md); personal name/email and the submission code are not stored in this project.

