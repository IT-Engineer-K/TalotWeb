# トップ・特長・使い方・よくある質問・お問い合わせ・404
from common import *

FAQ = [
    ("はじめての方へ", [
        ("タロットのことを何も知らなくても使えますか？",
         "はい、大丈夫です。今の状況に近いものを選んでいくだけで、占い方（スプレッド）もアプリが選びます。カードの意味も、ふだんの言葉で説明します。"),
        ("会員登録やログインは必要ですか？",
         "必要ありません。アプリを入れたら、すぐに占えます。メールアドレスなどの入力もありません。"),
        ("どの端末で使えますか？",
         "Android のスマートフォンでお使いいただけます。iPhone 版は今のところありません。"),
        ("1日に何回でも占えますか？",
         "「今日の運勢」は1日1枚です。同じ日にもう一度開くと、引いたカードをそのまま読み返せます。ほかの相談に回数の制限はありません。ただ、同じことを何度も占うと迷いが増えることもあります。気持ちが落ち着いてから、もう一度カードを引いてみてください。"),
    ]),
    ("占いの内容について", [
        ("どんなことを占えますか？",
         "仕事・学業、人間関係、恋愛、お金、生活、今日の運勢の6つです。たとえば「職場の人間関係」「貯金・節約」「なんとなく毎日がもやもやする」など、テーマごとに質問が用意されています。"),
        ("質問に答えるのが面倒なときは？",
         "どの画面でも「すぐ占う」を押せば、そこでカードを引けます。質問に答えるほど、結果の文章があなたの相談に近づきます。"),
        ("逆位置は使いますか？",
         "はじめは使う設定です。逆位置を使いたくない方は、マイページの設定でオフにできます。"),
        ("結果が良くなかったときは、どう受け止めればいいですか？",
         "タロットは未来を決めるものではなく、「今どう動くとよいか」のヒントです。慎重な結果のときは、アドバイスと気をつけることを一緒に読んで、できそうなことを一つだけ選んでみてください。"),
        ("数秘術や月の満ち欠けも見られますか？",
         "はい。マイページで生年月日を登録すると、結果の最後にライフパスナンバーからのひとことが出ます。月の満ち欠けのひとことは、登録しなくても毎回表示されます。"),
    ]),
    ("広告・プライバシー", [
        ("広告は出ますか？",
         "使い始めて8日目から、占い結果の最後のページに広告が1つ表示されます。結果の途中で広告に止められることはありません。最初の7日間は広告を表示しません。"),
        ("入力した名前や生年月日は、どこかに送られますか？",
         "送られません。ニックネーム・生年月日・相手のお名前・占いの履歴は、お使いのスマートフォンの中にだけ保存されます。くわしくは<a href=\"{r}privacypolicy.html\">プライバシーポリシー</a>をご覧ください。"),
        ("相手の名前を入れたくありません。",
         "空欄のままで大丈夫です。その場合、結果の文章では「相手」と表示します。"),
        ("履歴を消すことはできますか？",
         "履歴の画面から1件ずつ、またはマイページの「履歴をすべて削除」でまとめて消せます。"),
        ("機種変更のとき、履歴は引き継げますか？",
         "申し訳ありませんが、引き継ぎには対応していません。データはバックアップの対象外で、端末の中だけに保存されます。"),
    ]),
    ("お知らせ・アイコン", [
        ("毎日の通知はうるさくないですか？",
         "「今日のカード」のお知らせは、毎日・3日に1回・週に1回・お知らせしない、から選べます。その日のカードをもう引いていれば、お知らせは届きません。"),
        ("ホーム画面のアイコンが変わりました。",
         "アイコンの中の月は、本物の月の満ち欠けに合わせて8つの形に変わります。満月の日は、月が金色に光ります。"),
    ]),
]

def faq_html(r, groups):
    out = []
    for g, items in groups:
        out.append(f"<h2>{g}</h2>")
        for q, a in items:
            out.append(f'<details><summary>{q}</summary><div class="a"><p>{a.format(r=r)}</p></div></details>')
    return "\n".join(out)

def faq_ld(groups):
    import re
    ents = []
    for _, items in groups:
        for q, a in items:
            ents.append({"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a.format(r=""))}})
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ents}

THEMES = [
    ("今日の運勢", "毎日の1枚で、今日の流れを見ます。朝の習慣にどうぞ。", ["1枚引き", "今日のアドバイス", "今日の数字"], True),
    ("仕事・学業", "毎日の仕事や勉強、これからの進み方を占います。", ["仕事", "勉強・試験", "進路・就活・転職", "副業・やりたいこと"], False),
    ("人間関係", "身近な人との関係を、落ち着いて見つめ直します。", ["友だち", "家族", "職場・学校", "グループ・サークル", "人付き合い全般"], False),
    ("恋愛", "あの人の気持ちや、この先の流れを占います。", ["片思い中", "恋人がいる", "復縁したい", "出会いがほしい", "恋愛に少し疲れた"], False),
    ("お金", "収入や貯金、大きな買い物の迷いに。", ["収入を増やしたい", "貯金・節約", "大きな買い物", "お金の不安"], False),
    ("生活", "暮らしのリズムや、心の疲れに寄り添います。", ["引っ越し・住まい", "生活リズム・習慣", "疲れ・休み方", "なんとなく毎日がもやもやする"], False),
]

def themes_html():
    out = []
    for name, desc, chips, feat in THEMES:
        cls = "panel theme featured" if feat else "panel theme"
        out.append(f'<div class="{cls}"><h3><span class="dot"></span>{name}</h3><p class="muted small" style="margin:0">{desc}</p>'
                   f'<div class="chips">{"".join(f"<span class=chip>{c}</span>" for c in chips)}</div></div>')
    return '<div class="themes">' + "".join(out) + "</div>"

def phones(r):
    c = f"{r}images/cards/"
    return f'''<div class="phones">
  <figure class="phone-fig">
    <div class="phone"><div class="screen">
      <div class="s-moon" data-moon-now></div>
      <p class="s-title">ゆかりさん、何を占いますか？</p>
      <div class="s-today"><b>今日の運勢</b>毎日の1枚で、今日の流れを見ます</div>
      <p class="s-label">相談したいこと</p>
      <div class="s-cat">仕事・学業</div><div class="s-cat">人間関係</div><div class="s-cat">恋愛</div><div class="s-cat">お金</div><div class="s-cat">生活</div>
      <div class="s-tabs"><span class="on">占う</span><span>履歴</span><span>マイページ</span></div>
    </div></div>
    <figcaption><b>1. 占いたいことを選ぶ</b>いちばん上は毎日の「今日の運勢」。</figcaption>
  </figure>
  <figure class="phone-fig">
    <div class="phone"><div class="screen">
      <div class="s-moon" data-moon-now></div>
      <p class="s-ack">毎日顔を合わせる場所のことなんですね。</p>
      <p class="s-q">職場や学校で、気になることは？</p>
      <div class="s-opt">特定の人とのこと</div><div class="s-opt">周りになじめるか</div><div class="s-opt">上司・先生との関係</div><div class="s-opt">周りからどう見られているか</div>
      <p class="s-skip">すぐ占う ›</p>
    </div></div>
    <figcaption><b>2. 質問に答える</b>まず受け止めてから、次の質問へ。</figcaption>
  </figure>
  <figure class="phone-fig">
    <div class="phone"><div class="screen">
      <div class="s-moon" data-moon-now></div>
      <div class="s-cards"><img src="{c}major_17.webp" alt=""><img class="dim" src="{c}minor_cups_02.webp" alt=""><img class="dim" src="{c}minor_wands_01.webp" alt=""></div>
      <p class="s-pos">今の状況</p>
      <p class="s-name">星</p>
      <p class="s-star">✦</p>
      <p class="s-body">心を開いて、素直につながれる時です。</p>
      <div class="s-tap"><div class="s-dots"><i class="on"></i><i></i><i></i><i></i><i></i></div>タップして次のカードへ</div>
    </div></div>
    <figcaption><b>3. 1枚ずつ、ゆっくり読む</b>画面のどこをタップしても次へ。</figcaption>
  </figure>
</div>
<p class="img-note">※ 画面はイメージです。実際の文章はカードと答えによって変わります。</p>'''

def index():
    r = ""
    c = "images/cards/"
    body = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">タロット占いアプリ</p>
      <h1>がんばる毎日に、<br><span class="gold">ひとやすみ</span>の一枚を。</h1>
      <p class="lead">質問に答えて、カードを引くだけ。<br>占い師と話しているような、やさしい言葉の流れで、今の気持ちを整理できます。</p>
      <div class="btn-row">{play_button(r)}<a class="btn btn-ghost" href="howto.html">使い方を見る</a></div>
      <p class="btn-note">Android 対応・会員登録なし・入力した情報は端末の中だけ</p>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <div class="hero-moon" data-moon-now></div>
      <div class="fan">
        <div class="card left"><img src="{c}major_18.webp" alt=""></div>
        <div class="card right"><img src="{c}major_19.webp" alt=""></div>
        <div class="card mid"><img src="{c}major_17.webp" alt=""></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">こんな時に</p>
    <h2 class="sec-title">少しだけ、立ち止まりたい時に</h2>
    <ul class="moments">
      <li>仕事で迷うことが続いて、考えを整理したい</li>
      <li>家族や職場の人間関係に、もやもやが残っている</li>
      <li>あの人の気持ちが、ふと気になった夜に</li>
      <li>お金やこれからの暮らしが、なんとなく不安</li>
      <li>朝、今日一日のヒントがほしい</li>
      <li>理由はないけれど、心が少し疲れている</li>
    </ul>
    <p class="muted" style="margin-top:22px">占いは、答えを決めるものではなく、気持ちを整えるきっかけ。{APP}は、日々の「参考にする占い」を大切にしています。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="center">
      <p class="eyebrow">特長</p>
      <h2 class="sec-title">迷わず、やさしく、最後まで。</h2>
      <p class="sec-lead">はじめての方でも、画面に出てくる言葉のとおりに進むだけ。落ち着いた夜空の画面で、ゆっくり読めます。</p>
    </div>
    <div class="grid grid-3" style="margin-top:28px">
      <div class="panel"><div class="icon-badge">{ICONS["hand"]}</div><h3>質問に答えるだけ</h3><p>今の状況に近いものを選ぶだけで、占い方（スプレッド）はアプリが選びます。タロットを知らなくても大丈夫です。</p></div>
      <div class="panel"><div class="icon-badge">{ICONS["chat"]}</div><h3>話しているような流れ</h3><p>答えをまず受け止めてから、次の質問へ。結果はカードを1枚ずつ解説し、最後に全体をまとめます。</p></div>
      <div class="panel"><div class="icon-badge">{ICONS["book"]}</div><h3>結果を最後まで読める</h3><p>結果の途中で広告に止められることはありません。広告は結果の最後に1つだけ。使い始めて7日間は表示しません。</p></div>
      <div class="panel"><div class="icon-badge">{ICONS["text"]}</div><h3>大きな文字と、やさしい言葉</h3><p>ゆったりした大きめの文字。画面のどこをタップしても次へ進むので、細かいボタンを探す必要がありません。</p></div>
      <div class="panel"><div class="icon-badge">{ICONS["moon"]}</div><h3>数秘術と月の満ち欠けも</h3><p>生年月日から出すライフパスナンバーと、本物の月の満ち欠けから、あなたと今日へのひとことを添えます。</p></div>
      <div class="panel"><div class="icon-badge">{ICONS["lock"]}</div><h3>情報は端末の中だけ</h3><p>会員登録はありません。ニックネームや生年月日、相手のお名前は、スマートフォンの外に送られません。</p></div>
    </div>
    <p class="center" style="margin-top:26px"><a href="features.html">すべての特長を見る ›</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="facts">
      <div class="panel fact"><div class="num">78<small>枚</small></div><p>すべてのカードの<br>正位置と逆位置に対応</p></div>
      <div class="panel fact"><div class="num">6<small>つ</small></div><p>仕事・人間関係・恋愛<br>お金・生活・今日の運勢</p></div>
      <div class="panel fact"><div class="num">131<small>通り</small></div><p>質問の答えで変わる<br>相談の流れ</p></div>
      <div class="panel fact"><div class="num">4,700<small>以上</small></div><p>相談ごとに書き分けた<br>結果の文章</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="center">
      <p class="eyebrow">画面</p>
      <h2 class="sec-title">3つのステップで、今日の一枚へ</h2>
    </div>
    <div style="margin-top:30px">{phones(r)}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">占えること</p>
    <h2 class="sec-title">毎日の悩みに近いテーマから</h2>
    <p class="sec-lead">質問は全部で48問。あなたの答えに合わせて、結果の言葉が変わります。</p>
    <div style="margin-top:24px">{themes_html()}</div>
  </div>
</section>

<section>
  <div class="narrow">
    <div class="panel moon-now">
      <div data-moon-now></div>
      <div>
        <p class="eyebrow" style="margin:0">今夜の月</p>
        <p class="moon-name" data-moon-name>…</p>
        <p class="muted small">月齢 <span data-moon-age>…</span></p>
        <p>アプリの背景とホーム画面のアイコンの月は、本物の月の満ち欠けと同じ形。満月の日だけ、アイコンの月が金色に光ります。</p>
        <p style="margin:0"><a href="guide/moon.html">月の満ち欠けと過ごし方 ›</a></p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">読み物</p>
    <h2 class="sec-title">タロットカードの意味</h2>
    <p class="sec-lead">アプリの文章をもとに、78枚それぞれの意味を、恋愛・仕事・人間関係などのテーマ別にまとめました。</p>
    <div class="card-grid" style="margin-top:22px">
      {"".join(f'<a class="card-link" href="cards/{i}.html"><img src="{c}{i}.webp" alt="{n}" loading="lazy" width="360" height="630">{n}</a>' for i, n in [("major_00","愚者"),("major_01","魔術師"),("major_17","星"),("major_18","月"),("major_19","太陽"),("major_21","世界")])}
    </div>
    <p style="margin-top:22px"><a href="cards/index.html">78枚すべてを見る ›</a></p>
  </div>
</section>

<section>
  <div class="narrow faq">
    <p class="eyebrow">よくある質問</p>
    <h2 class="sec-title">はじめる前に</h2>
    {"".join(f'<details><summary>{q}</summary><div class="a"><p>{a.format(r=r)}</p></div></details>' for q, a in [FAQ[0][1][0], FAQ[0][1][1], FAQ[2][1][0], FAQ[2][1][1]])}
    <p style="margin-top:18px"><a href="faq.html">よくある質問をすべて見る ›</a></p>
  </div>
</section>

{cta_band(r)}
'''
    app_ld = {
        "@context": "https://schema.org", "@type": "MobileApplication", "name": APP,
        "operatingSystem": "Android", "applicationCategory": "LifestyleApplication",
        "inLanguage": "ja", "url": BASE_URL, "installUrl": PLAY_URL,
        "description": "質問に答えてカードを引くだけのタロット占いアプリ。仕事・人間関係・恋愛・お金・生活・今日の運勢を、やさしい言葉で占います。",
        "image": BASE_URL + "images/og.png",
    }
    page("index.html", None,
         "質問に答えてカードを引くだけ。占い師と話しているような流れで、仕事・人間関係・恋愛・お金・生活・今日の運勢を、やさしい言葉で占うタロットアプリです。会員登録なし。",
         body, jsonld=[app_ld], full_title=f"{APP}｜がんばる毎日に、ひとやすみの一枚を。")

def features():
    r = ""
    items = [
        ("hand", "質問に答えるだけで、占い方が決まります",
         "タロットには、カードの並べ方（スプレッド）がたくさんあります。{app}では、あなたの答えからアプリが「1枚引き」「スリーカード」「二者択一」を選びます。どれを選べばいいか迷うことはありません。",
         ["「うまく言えない」を選んでも占えます", "どの画面でも「すぐ占う」でカードを引けます", "カードはシャッフルのあと、自動で引かれます"]),
        ("chat", "占い師と話しているような流れ",
         "「片思い中」を選ぶと「想っている人がいるんですね。」、「恋愛に少し疲れた」を選ぶと「無理に元気を出さなくて大丈夫です。」。答えをまず受け止めてから、次の質問に進みます。",
         ["カードは1枚ずつ飛んできて、その場でめくれます", "1枚ずつ解説したあと、全体を一つのまとめに", "まとめのあとに、気になる視点を追加で読み直せます"]),
        ("book", "結果を、最後まで読めます",
         "結果の途中で、課金の案内や動画広告に止められることはありません。広告は結果の最後のページに1つだけ。使い始めて7日間は、広告を表示しません。",
         ["結果の一部が隠れることはありません", "広告は結果を読み終えたあとの1つだけ"]),
        ("text", "大きな文字と、迷わない操作",
         "本文は大きめの文字と、ゆったりした行間。スマートフォンの文字サイズの設定に合わせて、さらに大きくなります。結果の画面では、画面のどこをタップしても次へ進みます。",
         ["下のバーは「占う」「履歴」「マイページ」の3つだけ", "今どこを読んでいるかは、点の数でわかります"]),
        ("leaf", "決めつけない、やさしい言葉",
         "「死神」や「塔」のように怖い印象のカードも、「区切り」「見直しのとき」として、今どう動くとよいかを伝えます。良い結果も慎重な結果も、あなたが次の一歩を選べるように書いています。",
         ["一つの相談に、今の状況・これからの流れ・アドバイス", "ニックネームを登録すると「〇〇さん、」と呼びかけます"]),
        ("moon", "数秘術と、本物の月の満ち欠け",
         "生年月日を登録すると、ライフパスナンバーから「あなたらしい動き方」を結果に添えます。さらに、その日の月の形からのひとことも。タロットと合わせて、いくつかの角度から今を見つめられます。",
         ["ライフパスナンバーは 1〜9・11・22・33", "今日の運勢には、その日のパーソナルデイも"]),
        ("star", "月の形で変わる、ホーム画面のアイコン",
         "扇に広げた3枚のカードの真ん中に、今夜の月。アイコンは月の満ち欠けに合わせて8つの形に変わり、満月の日だけ金色に光ります。ホーム画面を見るたびに、空の月を思い出せます。",
         ["新月・三日月・上弦・満ちていく月・満月・欠けていく月・下弦・有明の月"]),
        ("history", "履歴は、ふつうの言葉で残ります",
         "履歴には、カード名のような用語ではなく「片思い中 › 相手の気持ち」のように、あなたが選んだ言葉で残ります。あとから読み返して、気持ちの変化を振り返れます。",
         ["消すまで残ります（期限はありません）", "1件ずつでも、まとめてでも消せます"]),
        ("bell", "好きなペースで「今日のカード」のお知らせ",
         "毎日・3日に1回・週に1回・お知らせしない、から選べます。時間も自由に決められます。その日のカードをもう引いていれば、お知らせは届きません。",
         ["はじめは朝8時（あとから変えられます）", "通知の許可は、お知らせをオンにしたときだけお願いします"]),
        ("lock", "登録なし。情報は端末の中だけ",
         "メールアドレスや会員登録は必要ありません。ニックネーム・生年月日・相手のお名前・占いの履歴は、スマートフォンの中にだけ保存され、外には送られません。相手のお名前は入れなくても占えます。",
         ["くわしくはプライバシーポリシーをご覧ください"]),
    ]
    blocks = []
    for i, (ic, h, t, pts) in enumerate(items, 1):
        lis = "".join(f"<li>{p}</li>" for p in pts)
        blocks.append(f'''<div class="panel"><div class="icon-badge">{ICONS[ic]}</div>
<p class="eyebrow" style="margin:0 0 4px">POINT {i:02d}</p><h3>{h}</h3><p>{t.format(app=APP)}</p>
<ul class="small muted" style="margin:0;padding-left:1.2em">{lis}</ul></div>''')
    body = f'''
<section style="padding-top:30px">
  <div class="wrap">
    <p class="eyebrow">特長</p>
    <h1 class="sec-title" style="font-size:34px">{APP}の10のこだわり</h1>
    <p class="sec-lead">「占いアプリは広告が多くて読みにくい」「どれを選べばいいかわからない」。そんな声から、落ち着いて最後まで読めるタロットを目指しました。</p>
    <div class="grid grid-2" style="margin-top:30px">{"".join(blocks)}</div>
  </div>
</section>
<section>
  <div class="narrow">
    <h2 class="sec-title">大切にしていること</h2>
    <div class="panel">
      <p>タロットは、未来を言い当てるためのものではなく、今の自分を見つめるための鏡だと考えています。</p>
      <p>カードの言葉は、あなたの背中をそっと押すことも、立ち止まって考えるきっかけになることもあります。どちらの場合も、最後に決めるのはあなた自身です。</p>
      <p style="margin:0">忙しい毎日の中で、ほんの数分、自分のための時間を。{APP}が、そんな「ひとやすみ」の相棒になれたらうれしいです。</p>
    </div>
  </div>
</section>
{cta_band(r)}
'''
    page("features.html", "特長・こだわり",
         f"{APP}の10のこだわり。質問に答えるだけで占い方が決まり、結果は最後まで読めます。大きな文字、やさしい言葉、数秘術と月の満ち欠け、登録なしで情報は端末の中だけ。",
         body, crumbs=[(None, "特長")])

def howto():
    r = ""
    body = f'''
<section style="padding-top:30px">
  <div class="narrow">
    <p class="eyebrow">使い方</p>
    <h1 class="sec-title" style="font-size:34px">はじめての占い、6つのステップ</h1>
    <p class="sec-lead">画面に出てくる言葉のとおりに進むだけ。1回の占いは、ゆっくり読んでも数分ほどです。</p>
    <ol class="steps" style="margin-top:26px">
      <li><h3>占いたいことを選ぶ</h3><p>ホームで「今日の運勢」か、「仕事・学業」「人間関係」「恋愛」「お金」「生活」から選びます。毎日使うなら、いちばん上の「今日の運勢」がおすすめです。</p></li>
      <li><h3>質問に答える</h3><p>「今の状況に近いものを選んでください」のような質問に、選択肢から答えます。途中で「すぐ占う」を押せば、そこでカードを引けます。</p></li>
      <li><h3>相手のお名前（入れなくても大丈夫）</h3><p>恋愛や人間関係では、占う相手のお名前やニックネームを入れられます。結果の文章にお名前が入ります。空欄なら「相手」と表示します。</p></li>
      <li><h3>シャッフルする</h3><p>占いたいことを思い浮かべながら、「シャッフルする」を押します。カードは自動で引かれ、上から1枚ずつ飛んできて、その場でめくれます。</p></li>
      <li><h3>1枚ずつ読む</h3><p>「今の状況」「これからの流れ」「アドバイス」など、カードの位置ごとに解説します。画面のどこをタップしても次へ進みます。</p></li>
      <li><h3>まとめと、もう一歩</h3><p>最後に全体のまとめ。気になる視点（相手の気持ち・この先・注意すること など）を追加で読み直したり、数秘術や月のひとことを読んだりできます。結果は履歴に残ります。</p></li>
    </ol>
  </div>
</section>

<section>
  <div class="narrow">
    <h2 class="sec-title">3つの占い方（スプレッド）</h2>
    <p class="muted">どれを使うかは、あなたの答えからアプリが選びます。</p>
    <div class="grid" style="margin-top:18px">
      <div class="panel"><h3>1枚引き</h3><p>「今日の運勢」で使います。今日のカードを1枚引いて、今日の流れとアドバイスを読みます。</p></div>
      <div class="panel"><h3>スリーカード</h3><p>「今の状況」「これからの流れ」「アドバイス」の3枚で、相談をひとつの流れとして読みます。</p></div>
      <div class="panel"><h3>二者択一</h3><p>「転職する／今の職場に残る」のように迷っている2つを入力すると、それぞれを選んだ場合をカードで比べます。</p></div>
    </div>
    <p style="margin-top:18px"><a href="guide/spreads.html">スプレッドについてもっと読む ›</a></p>
  </div>
</section>

<section>
  <div class="narrow">
    <h2 class="sec-title">マイページで、もっと自分らしく</h2>
    <div class="table-wrap panel">
      <table>
        <tr><th>ニックネーム</th><td>ホームや結果で「〇〇さん、」と呼びかけます。</td></tr>
        <tr><th>生年月日</th><td>数秘術（ライフパスナンバー）のひとことが、結果に加わります。</td></tr>
        <tr><th>保存した相手</th><td>よく占う相手のお名前を保存しておけます。</td></tr>
        <tr><th>逆位置を使う</th><td>オフにすると、カードはすべて正位置で出ます。</td></tr>
        <tr><th>お知らせ</th><td>「今日のカード」のお知らせの回数と時間を選べます。</td></tr>
        <tr><th>履歴をすべて削除</th><td>これまでの占いの履歴をまとめて消せます。</td></tr>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="narrow">
    <h2 class="sec-title">上手に使うコツ</h2>
    <div class="panel">
      <ul style="margin:0;padding-left:1.2em">
        <li>占う前に、深呼吸をひとつ。気になっていることを一つだけ思い浮かべます。</li>
        <li>同じことを何度も占うより、日にちを置いてもう一度。気持ちの変化が見えてきます。</li>
        <li>結果の中から「今日できること」を一つだけ選んで、試してみてください。</li>
        <li>履歴を読み返すと、あの時の迷いが今どうなったかを振り返れます。</li>
      </ul>
    </div>
    <p style="margin-top:18px"><a href="guide/how-to-ask.html">占う前の「問い」の立て方 ›</a></p>
  </div>
</section>
{cta_band(r)}
'''
    page("howto.html", "使い方",
         f"{APP}の使い方。テーマを選び、質問に答えてシャッフルするだけ。1枚引き・スリーカード・二者択一の3つの占い方と、マイページの設定を紹介します。",
         body, crumbs=[(None, "使い方")])

def faq():
    r = ""
    body = f'''
<section style="padding-top:30px">
  <div class="narrow faq">
    <p class="eyebrow">よくある質問</p>
    <h1 class="sec-title" style="font-size:34px">よくある質問</h1>
    <p class="muted">ほかに気になることがあれば、<a href="contact.html">お問い合わせ</a>からお気軽にどうぞ。</p>
    {faq_html(r, FAQ)}
  </div>
</section>
{cta_band(r)}
'''
    page("faq.html", "よくある質問",
         f"{APP}のよくある質問。会員登録、広告、プライバシー、占えること、逆位置、数秘術、お知らせ、アイコンについてお答えします。",
         body, crumbs=[(None, "よくある質問")], jsonld=[faq_ld(FAQ)])

def contact():
    body = f'''
<section style="padding-top:30px">
  <div class="narrow">
    <p class="eyebrow">お問い合わせ</p>
    <h1 class="sec-title" style="font-size:34px">お問い合わせ</h1>
    <p>アプリについてのご質問、不具合のご報告、ご感想は、下のメールアドレスまでお送りください。いただいたメールはすべて読んでいます。</p>
    <div class="panel" style="margin:22px 0">
      <dl class="kw" style="margin:0">
        <dt>運営者</dt><dd>船原滉樹</dd>
        <dt>メール</dt><dd><a href="mailto:{MAIL}?subject={APP}%20%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6">{MAIL}</a></dd>
      </dl>
    </div>
    <h2 class="sec-title" style="font-size:22px">不具合のご報告の際は</h2>
    <p>次のことを書いていただけると、原因を調べやすくなります。</p>
    <ul>
      <li>お使いの機種と Android のバージョン</li>
      <li>どの画面で、何をしたときに起きたか</li>
      <li>できれば、画面のスクリーンショット</li>
    </ul>
    <p class="muted small">お返事には数日いただくことがあります。占いの個別の鑑定・ご相談にはお答えできません。ご了承ください。</p>
    <p style="margin-top:24px"><a href="faq.html">よくある質問を見る ›</a></p>
  </div>
</section>
'''
    page("contact.html", "お問い合わせ", f"{APP}へのお問い合わせ。ご質問、不具合のご報告、ご感想はメールでお送りください。",
         body, crumbs=[(None, "お問い合わせ")], sticky=False)

def notfound():
    # 404 はどの階層から開かれても動くよう、絶対パスで書き換える
    body = f'''
<section style="padding:60px 0">
  <div class="narrow center">
    <div style="width:120px;margin:0 auto 20px" data-moon-phase="0"></div>
    <h1 class="sec-title">ページが見つかりませんでした</h1>
    <p class="muted">新月の夜のように、ここには何もないようです。<br>お手数ですが、トップページからお探しください。</p>
    <p style="margin-top:24px"><a class="btn btn-ghost" href="index.html">トップへ戻る</a></p>
  </div>
</section>
'''
    p = page("404.html", "ページが見つかりません", "お探しのページは見つかりませんでした。", body, sticky=False)
    f = os.path.join(OUT, p)
    s = open(f, encoding="utf-8").read()
    for a in ['href="', 'src="']:
        for target in ["assets/", "images/", "index.html", "features.html", "howto.html", "cards/", "guide/", "faq.html", "contact.html", "privacypolicy.html"]:
            s = s.replace(a + target, a + "/TalotWeb/" + target)
    s = s.replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"')
    open(f, "w", encoding="utf-8").write(s)

if __name__ == "__main__":
    index(); features(); howto(); faq(); contact(); notfound()
