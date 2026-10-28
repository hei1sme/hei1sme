"""Compose the profile banner from the portfolio's unchanged vector artwork."""
import base64
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "assets" / "source"
font = base64.b64encode((source / "manrope-latin.woff2").read_bytes()).decode()
sprite = base64.b64encode((source / "running-duck-sprite.webp").read_bytes()).decode()
workspace = (source / "workspace.svg").read_text(encoding="utf-8").strip()
workspace = workspace.replace('viewBox="0 0 1000 800"', 'x="540" y="0" width="740" height="480" viewBox="0 0 1000 800"', 1)
duck = f'''<g transform="translate(350 732)" pointer-events="none">
  <g transform="translate(-62 -115.32)" clip-path="url(#botanical-duck-crop)">
    <image href="data:image/webp;base64,{sprite}" width="372" height="248" transform="translate(-124 0)"/>
  </g>
</g>'''
marker = '<g data-botanical-layer="front">'
assert marker in workspace
workspace = workspace.replace(marker, duck + marker, 1)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 480" width="1280" height="480" role="img" aria-labelledby="title desc">
<title id="title">hei — Seeing beyond the prediction.</title>
<desc id="desc">A cobalt desk with a laptop, monitor and mechanical keyboard, surrounded by tropical foliage. A doodle duck runs past the desk.</desc>
<defs><style>
@font-face{{font-family:ProfileManrope;src:url(data:font/woff2;base64,{font}) format('woff2');font-weight:200 800;}}
text{{font-family:ProfileManrope,Arial,sans-serif;fill:#152344;}}
</style><clipPath id="profile-frame"><rect width="1280" height="480" rx="24"/></clipPath></defs>
<g clip-path="url(#profile-frame)">
<rect width="1280" height="480" fill="#edf1f5"/>
<text x="62" y="84" font-size="40" font-weight="800" letter-spacing="-2.8">hei</text>
<path d="M141 55v22m-11-11h22m-19-8 16 16m-16 0 16-16" fill="none" stroke="#214ce8" stroke-width="2.5" stroke-linecap="round"/>
<text x="62" y="220" font-size="66" font-weight="550" letter-spacing="-4.1">Seeing beyond</text>
<text x="62" y="294" font-size="66" font-weight="550" letter-spacing="-4.1">the prediction.</text>
<text x="65" y="350" font-size="19" font-weight="500">AI research &amp; things in motion</text>
<text x="65" y="417" font-size="15" font-weight="600" style="fill:#214ce8">hei-portfolio.vercel.app</text>
{workspace}
</g></svg>'''
(root / "assets" / "profile-hero.svg").write_text(svg + "\n", encoding="utf-8")
print("Built assets/profile-hero.svg")
