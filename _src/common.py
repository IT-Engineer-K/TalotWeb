# 共通のレイアウトと部品
import json, html, os

BASE_URL = "https://it-engineer-k.github.io/TalotWeb/"
PLAY_URL = "https://play.google.com/store/apps/details?id=com.konju.talot"
MAIL = "funahkonju@gmail.com"
APP = "ひとやすみタロット"
OUT = os.path.join(os.path.dirname(__file__), "..", "out")
SRC = "/mnt/user-data/uploads/Talot/app/src/main/assets/text/ja/"

def load(name):
    return json.load(open(SRC + name, encoding="utf-8"))

esc = html.escape

NAV = [
    ("index.html", "トップ"),
    ("features.html", "特長"),
    ("howto.html", "使い方"),
    ("cards/index.html", "カードの意味"),
    ("guide/index.html", "読み物"),
    ("faq.html", "よくある質問"),
]

ICONS = {
    "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 3.8v16.4c0 .8.9 1.3 1.6.9l13-8.2c.6-.4.6-1.3 0-1.7l-13-8.2C6.9 2.5 6 3 6 3.8z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 5h16v10H9l-5 4z" stroke-linejoin="round"/><path d="M8 9h8M8 12h5" stroke-linecap="round"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 5c3-1.5 5.5-1.5 8 0v14c-2.5-1.5-5-1.5-8 0zM20 5c-3-1.5-5.5-1.5-8 0v14c2.5-1.5 5-1.5 8 0z" stroke-linejoin="round"/></svg>',
    "text": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 18 9 6l5 12M5.8 14h6.4M15 18l3-7 3 7M16 16h4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z" stroke-linejoin="round"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="5" y="10.5" width="14" height="9.5" rx="2"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/><circle cx="12" cy="15" r="1.2" fill="currentColor"/></svg>',
    "bell": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z" stroke-linejoin="round"/><path d="M10 20.5a2 2 0 0 0 4 0" stroke-linecap="round"/></svg>',
    "history": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4.5 12a7.5 7.5 0 1 0 2.2-5.3M4.5 4v3.5H8" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 8v4l3 2" stroke-linecap="round"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5c.6 4.8 2.5 7.3 7.5 9.5-5 2.2-6.9 4.7-7.5 9.5-.6-4.8-2.5-7.3-7.5-9.5 5-2.2 6.9-4.7 7.5-9.5z"/></svg>',
    "hand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11m0-1.5a1.5 1.5 0 0 1 3 0V12m0-1a1.5 1.5 0 0 1 3 0v4a6 6 0 0 1-6 6h-.5a6 6 0 0 1-4.6-2.2L4.6 15a1.5 1.5 0 0 1 2.3-1.9L9 15" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14zM5 19l7-7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

def play_button(r, cls="btn btn-primary", label="Google Play で入手"):
    return f'<a class="{cls}" href="{PLAY_URL}" target="_blank" rel="noopener">{ICONS["play"]}{label}</a>'

def page(path, title, desc, body, *, crumbs=None, jsonld=None, sticky=True, head_extra="", og_type="website", full_title=None):
    depth = path.count("/")
    r = "../" * depth
    canonical = BASE_URL + (path[:-10] if path.endswith("index.html") else path)
    ttl = full_title or (f"{title}｜{APP}" if title else APP)
    nav = []
    for href, label in NAV:
        cur = ' aria-current="page"' if (href == path or (href.endswith("index.html") and href != "index.html" and path.startswith(href.split("/")[0] + "/"))) else ""
        nav.append(f'<a href="{r}{href}"{cur}>{label}</a>')
    crumb_html = ""
    if crumbs:
        items = [f'<a href="{r}index.html">トップ</a>']
        for href, label in crumbs:
            items.append(f'<a href="{r}{href}">{esc(label)}</a>' if href else f'<span>{esc(label)}</span>')
        crumb_html = '<nav class="crumbs wrap" aria-label="パンくずリスト">' + '<span aria-hidden="true">›</span>'.join(items) + '</nav>'
        bl = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": []}
        pos = 1
        bl["itemListElement"].append({"@type": "ListItem", "position": pos, "name": "トップ", "item": BASE_URL})
        for href, label in crumbs:
            pos += 1
            it = {"@type": "ListItem", "position": pos, "name": label}
            if href: it["item"] = BASE_URL + (href[:-10] if href.endswith("index.html") else href)
            bl["itemListElement"].append(it)
        jsonld = (jsonld or []) + [bl]
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    sticky_html = f'<div class="sticky-cta">{play_button(r)}</div>' if sticky else ""
    doc = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#141A33">
<title>{esc(ttl)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{APP}">
<meta property="og:title" content="{esc(ttl)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}images/og.png">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}images/icon.svg" type="image/svg+xml">
<link rel="icon" href="{r}images/icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="{r}images/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;700&family=Noto+Sans+JP:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
{head_extra}{ld}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{r}index.html"><img src="{r}images/icon.svg" alt="" width="40" height="40">{APP}</a>
    <nav class="nav" aria-label="メインメニュー">{"".join(nav)}</nav>
  </div>
</header>
{crumb_html}
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="logo" href="{r}index.html" style="font-size:18px"><img src="{r}images/icon.svg" alt="" width="34" height="34">{APP}</a>
        <p class="small" style="margin-top:10px">がんばる毎日に、ひとやすみの一枚を。<br>Android 向けタロット占いアプリです。</p>
      </div>
      <div>
        <h2>アプリについて</h2>
        <ul>
          <li><a href="{r}features.html">特長</a></li>
          <li><a href="{r}howto.html">使い方</a></li>
          <li><a href="{r}faq.html">よくある質問</a></li>
          <li><a href="{PLAY_URL}" target="_blank" rel="noopener">Google Play</a></li>
        </ul>
      </div>
      <div>
        <h2>読み物</h2>
        <ul>
          <li><a href="{r}cards/index.html">タロットカードの意味</a></li>
          <li><a href="{r}guide/tarot-basics.html">タロットのきほん</a></li>
          <li><a href="{r}guide/numerology.html">ライフパスナンバー</a></li>
          <li><a href="{r}guide/moon.html">今日の月と過ごし方</a></li>
        </ul>
      </div>
      <div>
        <h2>運営</h2>
        <ul>
          <li><a href="{r}contact.html">お問い合わせ</a></li>
          <li><a href="{r}privacypolicy.html">プライバシーポリシー</a></li>
        </ul>
      </div>
    </div>
    <p class="copy">占いの結果は、日々の参考としてお楽しみください。健康・お金・法律などの大切な判断は、専門家にご相談ください。<br>カードの絵：1909年に出版されたパメラ・コールマン・スミスの絵（パブリックドメイン）。<br>Google Play は Google LLC の商標です。<br>© 2026 {APP}</p>
  </div>
</footer>
{sticky_html}
<script src="{r}assets/site.js" defer></script>
</body>
</html>
'''
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(doc)
    return path

def cta_band(r, title="ひと息つきたくなったら、カードを1枚。", text="質問に答えるだけで、今の気持ちがすっと整理できます。"):
    return f'''<section class="cta-band"><div class="narrow"><div class="panel">
  <h2>{title}</h2>
  <p class="muted">{text}</p>
  <div class="btn-row">{play_button(r)}</div>
  <p class="btn-note">Android 対応・会員登録なし</p>
</div></div></section>'''

def fill(s):
    return s.replace("{partner}", "相手").replace("{you}", "あなた")
