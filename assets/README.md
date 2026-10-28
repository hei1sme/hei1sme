# Profile artwork

`profile-hero.png` is the README banner, rendered at 2× for readable GitHub scaling.
`profile-hero.svg` is the self-contained editable composition; the original
workspace vector, unchanged duck sprite and licensed Manrope font live in
`source/`. See `../design/profile-refresh.md` for provenance and content sources.

Rebuild the SVG with Python 3:

```sh
python scripts/build-banner.py
```

Render its PNG with a Playwright-equipped Node environment:

```sh
node scripts/render-banner.cjs
```

Set `PROFILE_PLAYWRIGHT` to an existing Playwright module path if it is installed
outside this repository. `PROFILE_BROWSER_CHANNEL=chrome` can use an existing
Chrome installation instead of a separately installed Playwright Chromium.
The public profile itself needs no Node/Python runtime,
JavaScript, external image service or scheduled workflow.
