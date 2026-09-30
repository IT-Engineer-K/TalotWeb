# タロットカードの意味：一覧と78枚のページ（アプリの文章から作る）
from common import *

CATS = [("love", "恋愛"), ("relationships", "人間関係"), ("work", "仕事・学業"),
        ("money", "お金"), ("life", "生活"), ("today", "今日の運勢")]
SUITS = {
    None: ("大アルカナ", "major", "22枚の大アルカナは、人生の大きなテーマや転機を表すカードです。0番の「愚者」から21番の「世界」まで、一人の旅人が成長していく物語として読むこともできます。"),
    "wands": ("ワンド", "wands", "ワンド（棒）は、火のエレメントに対応するとされ、情熱・やる気・行動・始めることを表します。"),
    "cups": ("カップ", "cups", "カップ（杯）は、水のエレメントに対応するとされ、気持ち・愛情・人とのつながりを表します。"),
    "swords": ("ソード", "swords", "ソード（剣）は、風のエレメントに対応するとされ、考え・言葉・決断・悩みを表します。"),
    "pentacles": ("ペンタクル", "pentacles", "ペンタクル（金貨）は、地のエレメントに対応するとされ、お金・仕事・体・暮らしなど形あるものを表します。"),
}
COURT = {11: "ペイジ", 12: "ナイト", 13: "クイーン", 14: "キング"}

def card_group(c):
    if c["arcana"] == "major":
        return f'大アルカナの{c["number"]}番'
    s = SUITS[c["suit"]][0]
    n = c["number"]
    if n == 1: rank = "エース（1）"
    elif n <= 10: rank = f"数札の{n}"
    else: rank = f"人物カード（{COURT[n]}）"
    return f"小アルカナ・{s}の{rank}"

def pos_block(c, key, label, cls):
    d = c[key]
    kws = "・".join(d["keywords"])
    items = []
    for k, name in CATS:
        extra = []
        if k in d.get("feelings", {}):
            extra.append(f'<b>相手の気持ち</b>{esc(fill(d["feelings"][k]))}')
        extra.append(f'<b>この先</b>{esc(fill(d["future"][k]))}')
        extra.append(f'<b>アドバイス</b>{esc(fill(d["advice"][k]))}')
        extra.append(f'<b>気をつけること</b>{esc(fill(d["caution"][k]))}')
        items.append(f'''<div class="panel meaning"><h3>{name}</h3><p>{esc(fill(d["meanings"][k]))}</p>
<div class="adv">{"<br>".join(extra)}</div></div>''')
    return f'''<div class="pos-block" id="{key}">
<h2><span class="pos-tag{cls}">{label}</span>{esc(c["name"])}の{label}</h2>
<p class="muted">キーワード：{kws}</p>
<div class="meaning-list">{"".join(items)}</div></div>'''

def build():
    cards = load("cards.json")["cards"]
    r = "../"
    for i, c in enumerate(cards):
        prev_c = cards[i - 1] if i > 0 else None
        next_c = cards[i + 1] if i + 1 < len(cards) else None
        up = "・".join(c["upright"]["keywords"])
        rv = "・".join(c["reversed"]["keywords"])
        grp = card_group(c)
        suit_desc = SUITS[c["suit"]][2]
        pager = '<nav class="pager" aria-label="前後のカード">'
        pager += f'<a href="{prev_c["id"]}.html">‹ {esc(prev_c["name"])}</a>' if prev_c else "<span></span>"
        pager += f'<a href="{next_c["id"]}.html">{esc(next_c["name"])} ›</a>' if next_c else "<span></span>"
        pager += "</nav>"
        body = f'''
<div class="narrow">
  <div class="card-hero">
    <div class="pic"><img src="{r}images/cards/{c["image"]}" alt="タロットカード「{esc(c["name"])}」の絵" width="360" height="630"></div>
    <div class="txt">
      <p class="eyebrow">{grp}</p>
      <h1>{esc(c["name"])}</h1>
      <p class="en">{esc(c["nameEn"])}</p>
      <dl class="kw">
        <dt>正位置</dt><dd>{up}</dd>
        <dt>逆位置</dt><dd>{rv}</dd>
      </dl>
      <p>「{esc(c["name"])}」は{grp}のカードです。正位置では「{up}」、逆位置では「{rv}」を表します。</p>
      <p class="muted small">{suit_desc}</p>
      <p class="small"><a href="#upright">正位置の意味</a>　<a href="#reversed">逆位置の意味</a></p>
    </div>
  </div>
  {pos_block(c, "upright", "正位置", "")}
  {pos_block(c, "reversed", "逆位置", " rev")}
  <p class="muted small" style="margin-top:28px">このページの文章は、アプリ「{APP}」の結果に使っている文章です。アプリでは、あなたの相談や、カードが出た位置（今の状況・これからの流れ・アドバイス）に合わせて、この中から文章を選びます。逆位置の読み方は<a href="{r}guide/reversed.html">逆位置のこと</a>をご覧ください。</p>
  {pager}
  <p class="center" style="margin-top:22px"><a href="index.html">カードの意味の一覧へ</a></p>
</div>
{cta_band(r, f"「{esc(c['name'])}」が出たら、あなたの相談ではどう読む？", "アプリでは、質問への答えに合わせて、カードの言葉をあなたの相談に合わせて届けます。")}
'''
        desc = f"タロットカード「{c['name']}（{c['nameEn']}）」の意味。正位置は{up}、逆位置は{rv}。恋愛・人間関係・仕事・お金・生活・今日の運勢ごとに、意味とアドバイスをやさしい言葉で解説します。"
        page(f"cards/{c['id']}.html", f"タロット「{c['name']}」の意味（正位置・逆位置）", desc, body,
             crumbs=[("cards/index.html", "カードの意味"), (None, c["name"])], og_type="article", sticky=False)

    # 一覧
    sections, nav = [], []
    for suit, (name, anchor, desc) in SUITS.items():
        group = [c for c in cards if c["suit"] == suit]
        nav.append(f'<a href="#{anchor}">{name}（{len(group)}枚）</a>')
        links = "".join(f'<a class="card-link" href="{c["id"]}.html"><img src="{r}images/cards/{c["image"]}" alt="" loading="lazy" width="360" height="630">{esc(c["name"])}</a>' for c in group)
        sections.append(f'<h2 class="suit-title" id="{anchor}">{name}</h2><p class="suit-desc">{desc}</p><div class="card-grid">{links}</div>')
    body = f'''
<section style="padding-top:30px">
  <div class="wrap">
    <p class="eyebrow">カードの意味</p>
    <h1 class="sec-title" style="font-size:34px">タロットカード78枚の意味</h1>
    <p class="sec-lead">大アルカナ22枚と小アルカナ56枚。それぞれのカードの正位置・逆位置の意味を、恋愛・人間関係・仕事・お金・生活・今日の運勢に分けて、やさしい言葉でまとめました。</p>
    <p class="small"><a href="{r}guide/tarot-basics.html">はじめての方は「タロットのきほん」から ›</a></p>
    <nav class="suit-nav" aria-label="グループ">{"".join(nav)}</nav>
    {"".join(sections)}
  </div>
</section>
{cta_band(r)}
'''
    page("cards/index.html", "タロットカード78枚の意味一覧",
         "タロットカード78枚（大アルカナ22枚・小アルカナ56枚）の意味一覧。正位置・逆位置の意味を、恋愛・仕事・人間関係・お金・生活・今日の運勢ごとにやさしく解説します。",
         body, crumbs=[(None, "カードの意味")])
    return cards

if __name__ == "__main__":
    build()
