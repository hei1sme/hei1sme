# Portfolio-aligned GitHub profile

2026-10-28. The owner asked to clone `hei1sme/hei1sme` into the parent work folder
and refresh it to match the current portfolio. This is a profile README, so use
GitHub's native layout rather than emulating website interactions with widgets.
Frontend Design leads composition; Humanizer guides concise personal writing.

## Plan before implementation

Keep the portfolio's Manrope, ink #152344, cobalt #214ce8, mist #edf1f5,
paper #f7f9fb, haze #a8c2eb and leaf #d7ed91. One wide banner reuses the selected
forest workspace and the original running duck. It includes the portfolio's
"Seeing beyond the prediction" headline. Leave all essential identity, facts,
status and links in selectable Markdown beneath it.

Layout: banner → identity and direct links → published research → optional
under-review detail → selected projects → experience/builds → tools and contact.
Use normal headings, short paragraphs and a compact comparison table. Avoid
multi-column image cards that squeeze on mobile, animated typing, code-block
biographies, repeated badge groups and external statistics/counter services.

Critique: copying the whole website into a single tall screenshot would hide
research/links inside pixels. Copying the old README's tables and replacing
purple with blue would keep its clutter. Use one authored visual and a short
native profile with deeper evidence linked to the portfolio instead.

## Content reconciliation

Source of current facts: `hei1sme/hei-portfolio` commit `785849d` and the owner's
confirmed updates in that checkout. The original profile is backed up at tag
`profile-before-portfolio-style-2026-10-28`, commit `d6361c2`.

- Keep SmokeNet as published at AJCAI 2025 / Springer LNAI, first and corresponding
  author, with its DOI and research-code link. Omit Q-rank marketing and numerical
  baseline/improvement claims pending source review.
- Bloom moved from the rejected AJCAI 2026 submission to ACIIDS 2027, under review.
  Add the missing AISTATS 2027 paper. Keep the evening-alert AJCAI 2026 manuscript
  and SIGKDD 2027 manuscript separately under review, matching portfolio titles
  and author roles. None is labelled accepted or a public preprint without a URL.
- MERR-GAT uses WavLM + Compact Conformer, BERT/RoBERTa and GAT; it remains in
  progress. Remove the old Wav2Vec/GATv2 architecture and target-journal badge.
- Link ASR/PPE to their case studies and scope ASR numbers as reported results.
- Include FCAJ/NutriTrack, BioListen's 6th place in VAIC Round 1, and CosmicOptic's
  frontend/backend role with synthetic demo data. Keep program/employment and
  participation/award distinctions intact.
- Keep FPT University, GPA 8.62/10 and expected Dec 2027 graduation. Preserve the
  academic/social contact links; detailed certifications remain in the CV/site.

## Asset provenance

The workspace SVG is copied from the portfolio's authored vector poster; no
actual photograph or private screen contents are published. The six-frame duck
sprite is existing generated artwork, reused unchanged from the portfolio.
See `hei-portfolio/design/duck-cursor-and-blog-cover.md` for the original record.
The banner uses a static clipped pose so GitHub never needs JavaScript or a
third-party animation endpoint to display the mascot.

Manrope is the same font used by the portfolio. Its embedded Latin WOFF2 comes
from the portfolio's Next/font output. Upstream font license: SIL Open Font
License 1.1, retained alongside the source font. Source:
https://github.com/google/fonts/tree/main/ofl/manrope .

## Verification

- GitHub's `/markdown` API rendered the actual README in GFM mode. This caught
  its hard line wrapping before publication; prose/navigation now use single
  physical lines so layout wraps naturally at the reader's width.
- Playwright inspected that GitHub-rendered HTML with GitHub's own Primer and
  Markdown CSS at 390px and 1440px, in light and dark modes. No document overflow;
  the banner loaded at its 2560px native width and scaled to the content column.
  Screenshots were visually inspected, including the mobile project table.
- The native manuscript disclosure opens and contains exactly four records.
  Published work stays visible. Essential name, role, education, contribution,
  paper status and contact links remain selectable outside the image.
- All 15 portfolio/CV/SpeedyLabX organization/repository links checked returned
  HTTP 200. Third-party scholarly/social services are retained from the verified
  portfolio/profile, not claimed as newly authenticated accounts.
- The banner renders at 2x through headless Chrome using the embedded Manrope
  font and unchanged duck sprite. It is about 446KB and has meaningful alt text.
  No private input files, source photograph, telemetry widgets or image services
  are required by the profile. Source files and the font license are included.
- `git diff --check` passed. Local preview/logs stay ignored in `output/`;
  `output/review/` points to the D-drive QA directory. Publication on GitHub is
  checked after pushing the commit and backup tag.
- Final 320px check also passed with the manuscript disclosure expanded. UTF-8
  text and PM₂.₅ were verified after a Windows default-encoding issue was fixed
  before publishing. Markdown word count fell from 1,134 to 457. All five paper
  titles match the portfolio source exactly; workspace and duck source hashes
  match their public portfolio originals.
