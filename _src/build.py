import os, shutil, glob, math
from common import *
import pages, cards, guide

os.makedirs(OUT, exist_ok=True)
shutil.copytree(os.path.join(os.path.dirname(__file__), "..", "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)

pages.index(); pages.features(); pages.howto(); pages.faq(); pages.contact(); pages.notfound()
cs = cards.build()
guide.build(cs)

# アイコン（ロゴ案 C2 をSVGに）
def lit(cx, cy, r, p):
    side = 1 if p < 0.5 else -1
    e = r * math.cos(2 * math.pi * p)
    pts = [(cx + side * r * math.sin(math.pi * i / 48), cy - r * math.cos(math.pi * i / 48)) for i in range(49)]
    pts += [(cx + side * e * math.sin(math.pi * i / 48), cy - r * math.cos(math.pi * i / 48)) for i in range(48, -1, -1)]
    return "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"

def card(x, y, w, h, alpha, fill, sw):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3.5" fill="{fill}" fill-opacity="{alpha}" stroke="#D4B26A" stroke-width="{sw}" stroke-opacity="{alpha}"/>'
            f'<rect x="{x+3.5}" y="{y+3.5}" width="{w-7}" height="{h-7}" rx="2" fill="none" stroke="#D4B26A" stroke-width=".9" stroke-opacity="{round(.45*alpha,3)}"/>')

icon = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#141A33"/><stop offset="1" stop-color="#2A1F45"/></linearGradient>
<linearGradient id="cd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#232B55"/><stop offset="1" stop-color="#1A2046"/></linearGradient>
<radialGradient id="gl" cx="54" cy="52" r="44" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#D4B26A" stop-opacity=".35"/><stop offset="1" stop-color="#D4B26A" stop-opacity="0"/></radialGradient>
<radialGradient id="mn" cx="48.75" cy="46.75" r="24" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF7E0"/><stop offset="1" stop-color="#E6D3A3"/></radialGradient>
</defs>
<rect width="108" height="108" rx="24" fill="url(#bg)"/>
<g transform="translate(54 54) scale(1.12) translate(-54 -52)">
<g transform="rotate(-19 53 94)">{card(38,30,30,50,.55,"#1F2650",1.6)}</g>
<g transform="rotate(19 53 94)">{card(38,30,30,50,.55,"#1F2650",1.6)}</g>
<ellipse cx="54" cy="52" rx="34" ry="44" fill="url(#gl)"/>
{card(34,18,40,68,1,"url(#cd)",2.2)}
<circle cx="54" cy="52" r="15" fill="#3A4275" stroke="#E6D3A3" stroke-opacity=".35" stroke-width=".8"/>
<path d="{lit(54,52,15,0.375)}" fill="url(#mn)"/>
</g>
</svg>'''
os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
open(os.path.join(OUT, "images", "icon.svg"), "w").write(icon)

# sitemap / robots
urls = []
for f in sorted(glob.glob(os.path.join(OUT, "**", "*.html"), recursive=True)):
    rel = os.path.relpath(f, OUT).replace(os.sep, "/")
    if rel == "404.html": continue
    urls.append(BASE_URL + (rel[:-10] if rel.endswith("index.html") else rel))
urls.append(BASE_URL + "privacypolicy.html")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{u}</loc><lastmod>2026-09-30</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
print(len(urls), "pages")
