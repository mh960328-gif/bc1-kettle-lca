# Official GitHub source notes

Checked on 2026-10-08 for the BC1 kettle project.

## USLCI data release and download instructions

- Official repository: [FLCAC-admin/uslci-content](https://github.com/FLCAC-admin/uslci-content)
- Release instructions: [release-downloads.md](https://github.com/FLCAC-admin/uslci-content/blob/dev/docs/release_info/release-downloads.md)
- Selected screening release: USLCI `1.2026-09.0` (openLCA `2.7.1`), as listed on the page on the check date.
- The GitHub page documents release versions and links to the downloadable database. For this release, the JSON-LD database file is served from Federal LCA Commons; the release instructions note that recent JSON-LD downloads redirect to Box. Therefore the GitHub repository is the authoritative version/download guide, while the actual process records are retrieved from the linked Commons dataset. No full database archive has been downloaded into this project yet.
- The project has screened five LCA Commons process records and recorded their UUIDs and versions in `mapping-decisions.csv`. Those records remain provisional. We have not imported their process JSON-LD, checked all upstream providers, or calculated impacts.

## TianGong search tool

- Official source repository: [tiangong-lca/cli](https://github.com/tiangong-lca/cli)
- Intended role: use the published CLI to search TianGong for matching processes and record candidates alongside USLCI matches.
- Current status: the live CLI still fails before authentication with a filesystem `EPERM` error, so no account session or live TianGong query was used. Instead, public process XML records were screened directly in the historical GitHub data repository; see [`tiangong-github-screening.md`](tiangong-github-screening.md). Candidate metadata was read through GitHub; no raw XML was copied locally. No course code, API key, or password has been placed in this repository.

## Limits of this record

These GitHub sources establish provenance and reproducible retrieval instructions; they are not evidence that an unreviewed candidate is a valid match. Dataset release, exact UUID/version, geography, reference flow, system boundary, retrieval date, local file hash, and provider links must be verified for every process used in a calculated run. Raw database archives should be cached locally only when needed and kept out of the public repository unless their license and course rules explicitly permit redistribution.
