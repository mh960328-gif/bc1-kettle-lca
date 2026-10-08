# Final course submission checklist

This file records the fields visible in the course's final submission form. It does not store personal information or the course submission code.

| Form field | What it means | Current state |
|---|---|---|
| Full name and email | Private identification sent to the instructor through the form; these do not belong in the public README. | Student enters directly in the form. |
| Group / alias | Optional public-facing label. | Not chosen. |
| Public GitHub repository URL | Link to the public repository containing the README, code, inputs allowed by course rules, and results. | https://github.com/mh960328-gif/bc1-kettle-lca |
| Final commit SHA | Exact 40-character Git commit identifier for the submitted public version. Obtain with git rev-parse HEAD after the final commit and push. | Capture after this README/checklist update is pushed; do not store its own future SHA here. |
| Course submission code | Shared form code supplied by the instructor. It is not a GitHub or TianGong credential. | Student enters directly; do not store it in this repository. |
| Public repository checkbox | Attests that the linked repository is public and its README documents the analysis with required fields and links to code/results. | Leave unchecked until the public repository and its contents have been reviewed. |

## Current readiness

The public repository is created and the project files are uploaded. The BOM mass check is complete. The background-data screen is still provisional, no product system has been assembled, no impact method has been selected, and no GWP100 total or contribution results exist. The form should not be submitted as a completed impact analysis until the student has reviewed the repository and decided whether this explicitly incomplete status meets the course submission rules.

The course README requirements explicitly allow the values unknown, not calculated, and not applicable where justified. Those words are transparent status reporting; they do not turn missing results into a completed calculation.

## Order when ready

1. Review the project files and remove anything not permitted for public release.
2. Choose a public alias if desired; keep full name, email, and course code out of the repository.
3. Verify the public repository URL and README links.
4. Record the final pushed commit with git rev-parse HEAD after the last update.
6. Enter the private form fields and course submission code directly in the course form, then check the public-repository attestation only if it is true.
