# 読み物（占いを学びたい人向け）。装飾は控えめに、本文と出典を中心にする。
from common import *

R = "../"
REFS = {
    "met": ('Tim Husband (2016) "Before Fortune-Telling: The History and Structure of Tarot Cards." The Metropolitan Museum of Art', "https://www.metmuseum.org/perspectives/tarot-2"),
    "brit_tarot": ('Encyclopaedia Britannica "Tarot"', "https://www.britannica.com/topic/tarot"),
    "dummett": ("Ronald Decker, Thierry Depaulis, Michael Dummett (1996) A Wicked Pack of Cards: The Origins of the Occult Tarot. Duckworth", None),
    "waite": ("Arthur Edward Waite (1910) The Pictorial Key to the Tarot. William Rider & Son（全文：Internet Sacred Text Archive）", "https://sacred-texts.com/tarot/pkt/index.htm"),
    "brit_num": ('Encyclopaedia Britannica "Numerology"', "https://www.britannica.com/topic/numerology"),
    "brit_palm": ('Encyclopaedia Britannica "Palmistry"', "https://www.britannica.com/topic/palmistry"),
    "forer": ("Forer, B. R. (1949) The fallacy of personal validation: a classroom demonstration of gullibility. Journal of Abnormal and Social Psychology, 44(1), 118–123", "https://doi.org/10.1037/h0059240"),
    "carlson": ("Carlson, S. (1985) A double-blind test of astrology. Nature, 318, 419–425", "https://www.nature.com/articles/318419a0"),
    "nao_age": ("国立天文台「「月齢」ってなに？なぜ小数がつくの？」", "https://www.nao.ac.jp/faq/a0204.html"),
    "nao_moon": ("国立天文台 暦計算室「こよみ用語解説 月のあれこれ」", "https://eco.mtk.nao.ac.jp/koyomi/faq/moon.html"),
    "nao_meigetsu": ("国立天文台「中秋の名月（2026年9月）」", "https://www.nao.ac.jp/astro/sky/2026/09-topics03.html"),
    "nao_24": ("国立天文台 暦計算室「こよみ用語解説 二十四節気」", "https://eco.mtk.nao.ac.jp/koyomi/faq/24sekki.html"),
    "cajochen": ("Cajochen, C. et al. (2013) Evidence that the lunar cycle influences human sleep. Current Biology, 23(15), 1485–1488", "https://pubmed.ncbi.nlm.nih.gov/23891110/"),
    "cordi": ("Cordi, M. et al. (2014) Lunar cycle effects on sleep and the file drawer problem. Current Biology, 24(12), R549–R550", "https://www.sciencedirect.com/science/article/pii/S0960982214005429"),
    "casiraghi": ("Casiraghi, L. et al. (2021) Moonstruck sleep: Synchronization of human sleep with the moon cycle under field conditions. Science Advances, 7(5), eabe0465", "https://www.science.org/doi/10.1126/sciadv.abe0465"),
    "schredl": ("Schredl, M. & Hofmann, F. (2003) Continuity between waking activities and dream activities. Consciousness and Cognition, 12(2), 298–308", "https://www.sciencedirect.com/science/article/abs/pii/S1053810002000727"),
    "nielsen": ("Nielsen, T. A. et al. (2003) The typical dreams of Canadian university students. Dreaming, 13(4), 211–235", "https://link.springer.com/article/10.1023/B:DREM.0000003144.40929.0b"),
    "ncnp": ("国立精神・神経医療研究センター 精神保健研究所 睡眠・覚醒障害研究部「睡眠時随伴症」", "https://www.ncnp.go.jp/nimh/sleep/sleep-medicine/parasomnia/index.html"),
    "newrick": ("Newrick, P. G., Affie, E. & Corrall, R. J. M. (1990) Relationship between longevity and lifeline: a manual study of 100 patients. Journal of the Royal Society of Medicine, 83(8), 499–501", "https://journals.sagepub.com/doi/10.1177/014107689008300809"),
    "lucas": ("Lucas, T., Dhugga, A. & Henneberg, M. (2019) Predicting longevity from the line of life: is it accurate? Anthropological Review, 82(2)", "https://czasopisma.uni.lodz.pl/ar/article/view/10778"),
    "caa": ("消費者庁「消費者からの問合せ窓口（消費者ホットライン188）」", "https://www.caa.go.jp/about_us/about/contact/"),
}

ARTICLES = [
    ("tarot-howto", "タロット占いのやり方", "ひとりで占うための手順と、読み方のコツ。毎日の練習法まで。", "タロット"),
    ("tarot-basics", "タロットのきほんと歴史", "78枚の構成と、ゲームから占いへ変わってきた歴史。", "タロット"),
    ("spreads", "スプレッド（カードの並べ方）", "1枚引き・スリーカード・二者択一・ケルト十字の使い分け。", "タロット"),
    ("reversed", "逆位置のこと", "逆さまに出たカードの4つの読み方と、使う・使わないの考え方。", "タロット"),
    ("how-to-ask", "占う前の「問い」の立て方", "同じカードでも、問いしだいで役に立ち方が変わります。", "タロット"),
    ("numerology", "数秘術とライフパスナンバー", "生年月日から数を出す方法。その場で計算できます。", "数秘術"),
    ("moon", "月齢と月の満ち欠け", "今夜の月の形、月の名前、月と睡眠の研究まで。", "月"),
    ("dreams", "夢占いと夢日記", "夢の研究でわかっていることと、夢を自分のために使う方法。", "夢"),
    ("shichu-suimei", "四柱推命のきほん", "干支と五行のしくみ。生まれた日の干（日干）を計算できます。", "四柱推命"),
    ("palmistry", "手相のきほん", "4つの主な線の見方と、手相についての研究。", "手相"),
    ("fortune-and-mind", "占いとの上手な付き合い方", "「当たっている」と感じるしくみと、困ったときの相談先。", "占いとこころ"),
]

def refs_html(keys):
    items = []
    for k in keys:
        text, url = REFS[k]
        items.append(f'<li>{esc(text)}' + (f' <a href="{url}" target="_blank" rel="noopener">リンク</a>' if url else "") + "</li>")
    return f'<h2 id="refs">参考文献</h2><ol class="small">{"".join(items)}</ol>'

def related_html(slugs):
    m = {a[0]: a for a in ARTICLES}
    lis = "".join(f'<li><a href="{s}.html">{m[s][1]}</a></li>' for s in slugs)
    return f'<h2>あわせて読みたい</h2><ul>{lis}</ul>'

def article(slug, lead, body, refs, related, head_extra="", cta=True):
    a = {x[0]: x for x in ARTICLES}[slug]
    title, desc = a[1], a[2]
    html_ = f'''
<article class="narrow article" style="padding-top:10px;padding-bottom:30px">
  <p class="eyebrow">{a[3]}</p>
  <h1>{title}</h1>
  <p class="muted">{lead}</p>
  {body}
  {refs_html(refs) if refs else ""}
  {related_html(related)}
  <p class="muted small" style="margin-top:28px">占いの結果は、日々の参考としてお使いください。健康・お金・法律などの大切な判断は、専門家にご相談ください。</p>
</article>
{cta_band(R, "学んだことを、アプリで試してみませんか", "質問に答えるだけで、カードの読み方がわかる文章が出ます。") if cta else ""}
'''
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": lead,
          "inLanguage": "ja", "author": {"@type": "Person", "name": "船原滉樹"},
          "publisher": {"@type": "Organization", "name": APP}, "datePublished": "2026-09-30", "dateModified": "2026-09-30"}
    page(f"guide/{slug}.html", title, f"{title}。{lead}", html_, crumbs=[("guide/index.html", "読み物"), (None, title)],
         jsonld=[ld], head_extra=head_extra, og_type="article", sticky=False)

def toc(items):
    return '<nav class="toc panel"><b>目次</b><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items) + "</ol></nav>"

# ---------------- タロット ----------------

def tarot_howto(cards):
    by = {c["id"]: c for c in cards}
    ex = [("今の状況", by["major_00"], "meanings"), ("これからの流れ", by["major_17"], "future"), ("アドバイス", by["major_01"], "advice")]
    ex_rows = "".join(f'<tr><th>{p}</th><td>{esc(c["name"])}（正位置）</td><td>{esc(fill(c["upright"][k]["work"]))}</td></tr>' for p, c, k in ex)
    body = f'''
{toc([("prep","用意するもの"),("steps","占う手順"),("read","読み方のコツ"),("example","例：スリーカードで仕事を占う"),("practice","上達のための練習法"),("care","気をつけたいこと")])}
<h2 id="prep">用意するもの</h2>
<ul>
  <li><b>タロットカード</b>：78枚のデッキ。はじめは大アルカナ22枚だけで練習しても大丈夫です。小アルカナまで場面の絵が描かれたデッキ（1909年にロンドンで出版された、パメラ・コールマン・スミス画のものと、その流れをくむもの）は、絵から意味を想像しやすく、学びはじめに向いています。</li>
  <li><b>ノート</b>：日付・問い・出たカード・感じたことを書き残します。あとで読み返すと、読み方の上達がよくわかります。</li>
  <li><b>静かな場所と数分の時間</b>：カードを広げられる平らな場所があれば十分です。</li>
</ul>

<h2 id="steps">占う手順</h2>
<ol>
  <li><b>問いを一つに決める。</b>「〜するには、今どうするとよい？」のように、自分が動ける形にすると結果を活かしやすくなります（<a href="how-to-ask.html">問いの立て方</a>）。</li>
  <li><b>スプレッドを決める。</b>迷ったら「1枚引き」か「スリーカード」から（<a href="spreads.html">スプレッド</a>）。</li>
  <li><b>シャッフルする。</b>カードを裏向きにテーブルへ広げ、両手で円を描くように混ぜます。逆位置を使うなら、この混ぜ方で上下もばらばらになります。問いを思い浮かべながら、気持ちが落ち着くまで続けます。</li>
  <li><b>まとめて、カットする。</b>一つの山にまとめ、いくつかの山に分けてから、好きな順に重ねて戻します。やり方は流派によってさまざまで、決まりはありません。</li>
  <li><b>並べて、めくる。</b>上から順に、スプレッドの位置に置いていきます。めくるときは、左右にめくるか上下にめくるかを決めておきます（逆位置の向きが変わらないように）。</li>
  <li><b>読む。</b>1枚ずつ「絵 → カードの意味 → 位置の意味」の順に考え、最後に全体を一文にまとめます。</li>
  <li><b>書き残す。</b>その場の解釈と、数日後に実際どうだったかを書き足します。</li>
</ol>

<h2 id="read">読み方のコツ</h2>
<ul>
  <li><b>本より先に、絵を見る。</b>人物の表情、向き、色、天気。最初に目に入ったものが、問いとつながることがよくあります。</li>
  <li><b>カードの意味 × 位置の意味。</b>たとえば「ソード（考え・言葉）」が「アドバイス」の位置に出たら、「言葉にして整理する」がヒントになる、のように組み合わせます。</li>
  <li><b>全体の傾向を見る。</b>大アルカナが多ければ大きな節目、同じスートが多ければそのテーマ（カップなら気持ち、ペンタクルならお金や暮らし）が中心だと読めます。</li>
  <li><b>最後は一文にまとめる。</b>「今は〇〇な状況で、△△の流れ。だから□□してみる」の形にすると、行動につながります。</li>
</ul>

<h2 id="example">例：スリーカードで仕事を占う</h2>
<p>問い：「新しい部署での仕事、これからどう進めるとよい？」</p>
<div class="table-wrap"><table><tr><th>位置</th><th>カード</th><th>読み</th></tr>{ex_rows}</table></div>
<p>まとめ：「新しいことに踏み出す時期で、希望を持って進める流れ。まず手元にあるもので小さく始めてみる」。3枚の意味をつなげて、今日からできる一歩を一つ決めます。</p>
<p class="muted small">読みの文章は、アプリ「{APP}」の文章です。カードごとの意味は<a href="{R}cards/index.html">カードの意味の一覧</a>で読めます。</p>

<h2 id="practice">上達のための練習法</h2>
<ul>
  <li><b>毎朝1枚引き。</b>朝に1枚引いて「今日のテーマ」を決め、夜に「実際はどうだったか」を一行書きます。大アルカナだけなら、およそ3週間で一巡します。</li>
  <li><b>1枚を3つの言葉で。</b>カードを1枚見て、意味を見ずに3つの言葉を書き出します。そのあと本や一覧と見比べます。</li>
  <li><b>同じスートを並べる。</b>エースから10までを並べると、数字の流れ（始まり → 広がり → 完成）が見えてきます。</li>
</ul>

<h2 id="care">気をつけたいこと</h2>
<ul>
  <li>同じ問いを何度も占い直すと、かえって迷いが増えます。日にちを置いてから、もう一度。</li>
  <li>健康・お金・法律など、生活に大きく関わることは、占いだけで決めず専門家に相談してください。</li>
  <li>人を占うときは、その人のプライバシーと気持ちを大切に。</li>
</ul>
'''
    article("tarot-howto", "タロットをひとりで占うための手順と読み方のコツを、はじめての方向けにまとめました。", body,
            ["waite", "met", "dummett"], ["tarot-basics", "spreads", "reversed", "how-to-ask"])

def tarot_basics():
    body = f'''
{toc([("deck","78枚の構成"),("major","大アルカナ"),("minor","小アルカナ"),("history","歴史：ゲームから占いへ"),("choose","デッキの選び方")])}
<h2 id="deck">78枚の構成</h2>
<p>タロットは78枚のカードでできています。22枚の<b>大アルカナ</b>と、56枚の<b>小アルカナ</b>です。</p>
<div class="table-wrap"><table>
<tr><th>グループ</th><th>枚数</th><th>内容</th></tr>
<tr><td>大アルカナ</td><td>22枚</td><td>0番「愚者」から21番「世界」まで。人生の大きなテーマや転機を表します。</td></tr>
<tr><td>小アルカナ</td><td>56枚</td><td>4つのスート（ワンド・カップ・ソード・ペンタクル）× 14枚。日常の出来事や気持ちを表します。</td></tr>
</table></div>

<h2 id="major">大アルカナ</h2>
<p>0番の「愚者」が旅に出て、さまざまな出会いや試練を経て、21番の「世界」で一つの旅を終える。大アルカナは、そんな成長の物語として読まれることがあります。1枚ずつの意味は<a href="{R}cards/index.html#major">大アルカナの一覧</a>をご覧ください。</p>

<h2 id="minor">小アルカナ</h2>
<p>各スートは、エース（1）から10までの数札と、ペイジ・ナイト・クイーン・キングの4枚の人物カードでできています。</p>
<div class="table-wrap"><table>
<tr><th>スート</th><th>エレメント（とされるもの）</th><th>表すこと</th></tr>
<tr><td><a href="{R}cards/index.html#wands">ワンド（棒）</a></td><td>火</td><td>情熱・やる気・行動</td></tr>
<tr><td><a href="{R}cards/index.html#cups">カップ（杯）</a></td><td>水</td><td>気持ち・愛情・つながり</td></tr>
<tr><td><a href="{R}cards/index.html#swords">ソード（剣）</a></td><td>風</td><td>考え・言葉・決断</td></tr>
<tr><td><a href="{R}cards/index.html#pentacles">ペンタクル（金貨）</a></td><td>地</td><td>お金・仕事・体・暮らし</td></tr>
</table></div>
<p class="muted small">スートとエレメントの対応は、19世紀以降のオカルト思想の中で整えられたもので、流派によって違うこともあります。</p>

<h2 id="history">歴史：ゲームから占いへ</h2>
<ul>
  <li><b>15世紀の北イタリア。</b>記録に残る最初のタロットは、1440年代ごろの北イタリアのものです。ふつうの4スートのカードに、「トリオンフィ（切り札）」21枚と「愚者」を加えたもので、トリックテイキングのカードゲームに使われていました。ミラノの貴族のために描かれた豪華なデッキが、今も美術館に残っています（ヴィスコンティ・スフォルツァ版など）。</li>
  <li><b>18世紀の終わりのフランス。</b>タロットが占いや神秘思想と結びつけて語られるようになったのは、ずっと後のことです。1781年、フランスの学者クール・ド・ジェブランが「タロットは古代エジプトの知恵を伝えるもの」と書きましたが、この説には歴史的な根拠がありません。その後、エテイヤが占い用のデッキと解説書を出し、占いとしてのタロットが広まっていきました。</li>
  <li><b>1909年のロンドン。</b>A. E. ウェイトの監修、パメラ・コールマン・スミスの絵によるデッキが出版されました。小アルカナの数札にも場面の絵を描いたことで、意味を覚えていなくても絵から読めるようになり、今の多くのデッキの手本になっています。</li>
</ul>
<p>今でもヨーロッパの一部では、タロットはゲームとして遊ばれています。</p>

<h2 id="choose">デッキの選び方</h2>
<ul>
  <li><b>はじめての1組</b>には、小アルカナまで絵が描かれたデッキがおすすめです。本や解説サイトの多くが、このタイプを前提にしています。</li>
  <li><b>見ていて落ち着く絵</b>を選ぶのがいちばんです。毎日手に取るものなので、好きになれることが続けるコツです。</li>
  <li>カードの大きさも大切です。手の小さい方は、ひとまわり小さいサイズだとシャッフルしやすくなります。</li>
</ul>
'''
    article("tarot-basics", "78枚の構成と、15世紀のゲームから占いへ変わってきたタロットの歴史を、信頼できる資料をもとにまとめました。", body,
            ["met", "brit_tarot", "dummett", "waite"], ["tarot-howto", "spreads", "reversed"])

def spreads():
    body = f'''
{toc([("one","1枚引き"),("three","スリーカード"),("choice","二者択一"),("celtic","ケルト十字"),("pick","どれを選ぶ？")])}
<h2 id="one">1枚引き</h2>
<p>1枚だけ引いて読む、いちばんシンプルな方法です。「今日のテーマ」「今いちばん大切にしたいこと」など、短い問いに向いています。毎日の練習にも最適です。</p>

<h2 id="three">スリーカード</h2>
<p>3枚を左から順に並べます。位置の意味はいくつかの型があり、問いに合わせて選びます。</p>
<div class="table-wrap"><table>
<tr><th>型</th><th>1枚目</th><th>2枚目</th><th>3枚目</th></tr>
<tr><td>時間の流れ</td><td>過去</td><td>現在</td><td>未来</td></tr>
<tr><td>相談の整理</td><td>今の状況</td><td>これからの流れ</td><td>アドバイス</td></tr>
<tr><td>二人の関係</td><td>あなた</td><td>相手</td><td>二人の関係</td></tr>
</table></div>
<p>アプリ「{APP}」では、2番目の「相談の整理」の型を使っています。</p>

<h2 id="choice">二者択一</h2>
<p>「AとBのどちらを選ぶか」で迷っているときの並べ方です。いちばん簡単なのは、Aを選んだ場合に1枚、Bを選んだ場合に1枚を引いて比べる方法です。それぞれに2〜3枚ずつ引いて「近い未来」「その先」まで見る型もあります。</p>
<p>どちらかに「良い」カードが出ても、それで決めてしまうのではなく、「なぜ自分はそちらを選びたいのか」を確かめる材料にするのがおすすめです。</p>

<h2 id="celtic">ケルト十字</h2>
<p>10枚を使う、よく知られた並べ方です。十字の形に6枚、その右に縦に4枚を並べます。位置の呼び方は本によって少しずつ違います。以下は、よく使われる並びの一例です。</p>
<ol>
  <li>今の状況</li><li>障害・課題（1枚目に交差させて置く）</li><li>目標・意識していること</li><li>土台・無意識</li><li>過去</li><li>近い未来</li><li>あなた自身</li><li>周りの人・環境</li><li>願い・恐れ</li><li>最終的な結果</li>
</ol>
<p>情報が多い分、読むのに慣れが必要です。まずはスリーカードに慣れてから試すと、つながりが読みやすくなります。</p>

<h2 id="pick">どれを選ぶ？</h2>
<ul>
  <li>毎日のこと、短い問い → <b>1枚引き</b></li>
  <li>一つの悩みを整理したい → <b>スリーカード</b></li>
  <li>2つの道で迷っている → <b>二者択一</b></li>
  <li>時間をとって、じっくり向き合いたい → <b>ケルト十字</b></li>
</ul>
<p>迷ったら、枚数の少ない方を選びましょう。少ない枚数の方が、一枚一枚の意味をていねいに読めます。</p>
'''
    article("spreads", "カードの並べ方（スプレッド）の代表的な4つと、問いに合わせた選び方を紹介します。", body,
            ["waite"], ["tarot-howto", "how-to-ask", "reversed"])

def reversed_(cards):
    by = {c["id"]: c for c in cards}
    rows = "".join(f'<tr><td><a href="{R}cards/{i}.html">{esc(by[i]["name"])}</a></td><td>{"・".join(by[i]["upright"]["keywords"])}</td><td>{"・".join(by[i]["reversed"]["keywords"])}</td></tr>' for i in ["major_00", "major_08", "major_13", "major_16", "minor_cups_03"])
    body = f'''
<h2>逆位置とは</h2>
<p>カードをめくったとき、絵が上下逆さまに出ることがあります。これを<b>逆位置</b>、正しい向きを<b>正位置</b>と呼びます。逆位置を読みに使うかどうかは、占う人によって違います。どちらが正しいということはありません。</p>

<h2>読み方の4つの型</h2>
<ol>
  <li><b>意味が弱まる・遅れる。</b>正位置の意味が、まだ十分に出ていない状態。「今はまだ準備中」と読みます。</li>
  <li><b>内側に向かう。</b>外に出ていくはずの力が、心の中にとどまっている状態。「気持ちはあるけれど、まだ表に出していない」など。</li>
  <li><b>行き過ぎ・足りない。</b>正位置の良さが、やり過ぎたり足りなかったりする状態。「自信」なら「過信」や「自信のなさ」。</li>
  <li><b>反対の意味。</b>正位置の反対として読む、昔からの読み方です。</li>
</ol>
<p>どの型で読むかを最初に決めておくと、読みがぶれにくくなります。迷ったときは、1か2の「やさしい読み」から始めるのがおすすめです。</p>

<h2>正位置と逆位置のキーワードの例</h2>
<div class="table-wrap"><table><tr><th>カード</th><th>正位置</th><th>逆位置</th></tr>{rows}</table></div>
<p class="muted small">キーワードは、アプリ「{APP}」で使っているものです。</p>

<h2>使う？使わない？</h2>
<ul>
  <li><b>使うと</b>：一つの問いに対する読みの幅が広がり、「今はまだ」「やり過ぎ注意」などの細かいニュアンスが伝えられます。</li>
  <li><b>使わないと</b>：覚える意味が半分になり、はじめての方でも読みやすくなります。慎重な意味は、周りのカードとの組み合わせから読み取ります。</li>
</ul>
<p>アプリでは、マイページの「逆位置を使う」をオフにすると、すべてのカードが正位置で出ます。</p>

<h2>逆位置が出ても、怖がらなくて大丈夫</h2>
<p>逆位置は「悪いことが起きる」というしるしではありません。「ここを少し見直すと、流れが良くなる」というヒントとして読むと、次の行動につなげやすくなります。</p>
'''
    article("reversed", "逆さまに出たカード（逆位置）の読み方の型と、使う・使わないの考え方をまとめました。", body,
            ["waite"], ["tarot-howto", "tarot-basics", "spreads"])

def how_to_ask():
    body = '''
<h2>問いしだいで、答えの使い方が変わる</h2>
<p>タロットの結果が役に立つかどうかは、問いの立て方で大きく変わります。自分が動ける形の問いにすると、カードの言葉を「次の一歩」に変えやすくなります。</p>

<h2>良い問いの3つのポイント</h2>
<ol>
  <li><b>自分を主語にする。</b>「あの人はどう思っている？」だけでなく、「あの人との関係のために、私にできることは？」も一緒に問います。</li>
  <li><b>はい・いいえで終わらせない。</b>「うまくいく？」より「うまくいくために、何を大切にするとよい？」。</li>
  <li><b>期間を区切る。</b>「この1か月で」「次の面接までに」など、区切りがあると読みやすくなります。</li>
</ol>

<h2>言い換えの例</h2>
<div class="table-wrap"><table>
<tr><th>こう聞きたくなったら</th><th>こう言い換えてみる</th></tr>
<tr><td>彼は私のことを好き？</td><td>彼との関係を良くするために、今の私にできることは？</td></tr>
<tr><td>転職は成功する？</td><td>転職を考える上で、今いちばん大切にしたいことは？</td></tr>
<tr><td>お金は貯まる？</td><td>この3か月、お金との付き合い方で見直すとよいことは？</td></tr>
<tr><td>家族とうまくいく？</td><td>家族と話すとき、どんな気持ちで向き合うとよい？</td></tr>
<tr><td>なんとなく毎日がつらい</td><td>今の私に、いちばん必要な休み方は？</td></tr>
</table></div>

<h2>占う前の小さな準備</h2>
<ul>
  <li>気になっていることを、紙に一行で書き出してみる。</li>
  <li>「本当はどうなってほしいか」を、自分で一度考えておく。</li>
  <li>深呼吸をひとつ。気持ちが波立っているときは、少し時間を置く。</li>
</ul>

<h2>同じ問いを何度も占わない</h2>
<p>望む答えが出るまで引き直すと、結局どれを信じればいいのか分からなくなります。一度占ったら、数日は結果を試してみる期間にしましょう。気持ちや状況が変わってから、もう一度問い直すと、変化が見えてきます。</p>
<p>アプリ「ひとやすみタロット」の質問は、この考え方で作っています。選択肢に答えていくと、相談の焦点（相手の気持ち・この先・アドバイス・注意すること）が決まり、それに合わせた文章が出ます。</p>
'''
    article("how-to-ask", "同じカードでも、問いの立て方しだいで役に立ち方が変わります。言い換えの例と一緒に紹介します。", body,
            [], ["tarot-howto", "spreads", "fortune-and-mind"])

# ---------------- 数秘術 ----------------

def numerology():
    n = load("numerology.json")
    data = json.dumps({"lifePath": n["lifePath"], "day": n["day"]}, ensure_ascii=False)
    rows = "".join(f'<tr><th>{k}</th><td>{esc(v)}</td></tr>' for k, v in n["lifePath"].items())
    body = f'''
{toc([("what","数秘術とは"),("calc","ライフパスナンバーを計算する"),("how","出し方（手計算）"),("list","12の数の意味"),("day","パーソナルデイ"),("note","知っておきたいこと")])}
<h2 id="what">数秘術とは</h2>
<p>数秘術は、名前や生年月日から数を出し、その人の性格や、これからの流れを読む占いです。「すべてのものは数で表せる」という古代ギリシャのピタゴラス学派の考え方が、思想的な源とされています。今よく使われている「生年月日の数字を足していく」方法は、20世紀以降に広まったものです。</p>

<h2 id="calc">ライフパスナンバーを計算する</h2>
<form class="tool panel" id="np-form">
  <label>生年月日を入れてください</label>
  <div class="row">
    <input name="y" type="number" inputmode="numeric" min="1900" max="2026" placeholder="1985" aria-label="年" style="width:110px"> 年
    <input name="m" type="number" inputmode="numeric" min="1" max="12" placeholder="7" aria-label="月" style="width:80px"> 月
    <input name="d" type="number" inputmode="numeric" min="1" max="31" placeholder="23" aria-label="日" style="width:80px"> 日
  </div>
  <p style="margin:16px 0 0"><button class="btn btn-primary" type="submit">計算する</button></p>
  <div class="result" id="np-result" aria-live="polite"></div>
  <p class="muted small" style="margin:14px 0 0">入力した生年月日は、このページの中だけで計算に使い、どこにも送信しません。</p>
</form>
<script type="application/json" id="np-texts">{data}</script>

<h2 id="how">出し方（手計算）</h2>
<p>生年月日の数字を、1桁ずつすべて足します。2桁になったら、1桁になるまで足し続けます。ただし、途中で <b>11・22・33</b> になったときは、それ以上足さずに「マスターナンバー」とします。</p>
<div class="panel">
<p><b>例：1985年7月23日生まれ</b></p>
<p>1 + 9 + 8 + 5 + 7 + 2 + 3 = 35</p>
<p>3 + 5 = <b>8</b> → ライフパスナンバーは 8</p>
</div>
<p class="muted small">年・月・日をそれぞれ先に1桁にしてから足す方法など、計算のしかたには流派があります。方法によって、マスターナンバーが出るかどうかが変わることがあります。このページとアプリは、すべての数字を1桁ずつ足す方法を使っています。</p>

<h2 id="list">12の数の意味</h2>
<p>アプリ「{APP}」で使っている、ライフパスナンバーのひとことです。</p>
<div class="table-wrap"><table>{rows}</table></div>

<h2 id="day">パーソナルデイ</h2>
<p>「誕生月 + 誕生日 + 今日の年月日」の数字をすべて足して1桁にしたものを、パーソナルデイと呼びます。その日をどう過ごすかのヒントとして使います。上の計算では、今日のパーソナルデイも一緒に出ます。</p>

<h2 id="note">知っておきたいこと</h2>
<ul>
  <li>数秘術は占いであり、性格や未来を科学的に言い当てるものではありません。</li>
  <li>性格の説明が「当たっている」と感じやすいのは、誰にでも当てはまる言葉を自分のことだと受け取りやすい、人の心のしくみも関係しています（<a href="fortune-and-mind.html">占いとの上手な付き合い方</a>）。</li>
  <li>「自分はこういう数だから」と決めつけず、自分をふり返るきっかけとして使うのがおすすめです。</li>
</ul>
'''
    article("numerology", "生年月日からライフパスナンバーを出す方法と、12の数の意味。このページでそのまま計算できます。", body,
            ["brit_num", "forer"], ["fortune-and-mind", "moon", "shichu-suimei"])

# ---------------- 月 ----------------

def moon():
    n = load("numerology.json")["moon"]
    texts = {k: v["today"] for k, v in n["text"].items()}
    cards = "".join(f'<div class="panel" data-moon-card="{k}"><div data-moon-phase="{k}"></div><div><h3>{n["names"][int(k)]}</h3><p>{esc(texts[k])}</p></div></div>' for k in sorted(texts, key=int))
    body = f'''
<div class="panel moon-now" style="margin:22px 0">
  <div data-moon-now></div>
  <div>
    <p class="muted small" style="margin:0">今夜の月</p>
    <p class="moon-name" data-moon-name>…</p>
    <p class="muted small">月齢 およそ <span data-moon-age>…</span></p>
    <p style="margin:0" data-moon-text></p>
  </div>
</div>
<script type="application/json" id="moon-texts">{json.dumps(texts, ensure_ascii=False)}</script>
<p class="muted small">月の形は、平均の朔望月（約29.53日）から計算した目安です。実際の満ち欠けとは、1日ほどずれることがあります。正確な日時は国立天文台の暦計算室で確かめられます。</p>

{toc([("age","月齢とは"),("see","月が見える時間"),("names","月の名前"),("sleep","月と睡眠の研究"),("eight","8つの月と過ごし方")])}

<h2 id="age">月齢とは</h2>
<p>月齢は「新月の瞬間から何日たったか」を表す数です。新月が0で、1日ごとに1ずつ増えます。新月の瞬間は日によって時刻がばらばらなので、正午の時点で数えると小数がつきます。</p>
<p>新月から次の新月までは、平均で約29.5日。月の動きは複雑なため、「月齢15 = 満月」とは限りません。</p>

<h2 id="see">月が見える時間</h2>
<p>月の出は、1日におよそ50分ずつ遅くなります（24時間 ÷ 約29.5日）。月の形で、見えやすい時間帯がわかります。</p>
<div class="table-wrap"><table>
<tr><th>月の形</th><th>見えやすい時間と方角</th></tr>
<tr><td>三日月</td><td>夕方、西の低い空。日が沈んだあと、すぐに沈みます。</td></tr>
<tr><td>上弦の月</td><td>夕方に南の空。夜中に西へ沈みます。</td></tr>
<tr><td>満月</td><td>日の入りのころ東から昇り、一晩じゅう見えます。</td></tr>
<tr><td>下弦の月</td><td>真夜中ごろに昇り、明け方に南の空。</td></tr>
</table></div>

<h2 id="names">月の名前</h2>
<p>日本では、昔の暦（太陰太陽暦）の日付で、月にいろいろな名前をつけてきました。</p>
<ul>
  <li><b>十五夜（中秋の名月）</b>：昔の暦の8月15日の夜の月。天文学の満月と同じ日になるとは限りません（2026年は、十五夜が9月25日、満月が9月27日でした）。</li>
  <li><b>十六夜（いざよい）</b>：十五夜の次の夜。月の出が少し遅れるのを、ためらう（いざよう）様子にたとえました。</li>
  <li><b>立待月・居待月・寝待月・更待月</b>：17日〜20日ごろの月。月の出がだんだん遅くなるので、立って待つ、座って待つ、寝て待つ、夜更けまで待つ、と名づけられました。</li>
  <li><b>十三夜</b>：昔の暦の9月13日の月。十五夜と並ぶお月見の日です。</li>
</ul>

<h2 id="sleep">月と睡眠の研究</h2>
<p>「満月の夜は眠りが浅い」という話を聞いたことがあるかもしれません。研究の結果は、まだ一致していません。</p>
<ul>
  <li>スイスの研究（2013年）では、窓のない実験室で眠った33人を後から分析したところ、満月のころは深い眠りが約30%減り、寝つくまでが約5分長く、睡眠時間が約20分短くなっていました。</li>
  <li>一方、別のグループが、より多くの睡眠データで確かめたところ、同じような関係は見つかりませんでした（2014年）。「結果が出なかった研究は発表されにくい」問題も指摘されています。</li>
  <li>アルゼンチンの先住民のコミュニティとアメリカの大学生を調べた研究（2021年）では、満月の前の数日は、寝る時刻が遅く、睡眠が短くなる傾向がありました。</li>
</ul>
<p>もし満月のころに眠りにくいと感じたら、寝室を暗くする、寝る前にスマートフォンの明るい画面を見ない、など、ふだんの眠りの工夫を少し意識してみてください。眠れない日が続くときは、医療機関に相談しましょう。</p>

<h2 id="eight">8つの月と過ごし方</h2>
<p>アプリ「{APP}」で、その日の月に合わせて出しているひとことです。今夜の月の形には、金色の枠がつきます。</p>
<div class="phase-list">{cards}</div>
<style>.phase-list .is-current {{ border-color: var(--gold); box-shadow: 0 0 24px rgba(212,178,106,.3); }}</style>
'''
    article("moon", "今夜の月の形と月齢、月の名前、月と睡眠についての研究を、国立天文台の資料や論文をもとにまとめました。", body,
            ["nao_age", "nao_moon", "nao_meigetsu", "cajochen", "cordi", "casiraghi"], ["numerology", "dreams", "fortune-and-mind"])

# ---------------- 夢 ----------------

def dreams():
    body = '''
{toc}
<h2 id="science">夢について、わかっていること</h2>
<ul>
  <li><b>起きているときの気がかりが、夢に出やすい。</b>「連続性仮説」と呼ばれる考え方です。ただし、ドイツの研究（2003年、133人・約2週間の夢日記）では、読書やパソコン作業のように集中する作業は夢に出にくく、人との会話などは出やすい、という違いも見つかりました。起きている時間がそのまま夢に映るわけではありません。</li>
  <li><b>多くの人が見る「典型的な夢」がある。</b>カナダの大学生1,181人の調査（2003年）では、「追いかけられる（けがはしない）」が81.5%、「落ちる」が73.8%、「学校・先生・勉強」が67.1%、「遅刻する・乗り遅れる」が59.5%の人に経験がありました。こうした夢を見るのは、ごくふつうのことです。</li>
  <li><b>夢の意味を一つに決める方法は、確かめられていない。</b>夢辞典の解釈は、昔からの言い伝えや、読み手の考えにもとづくものです。</li>
</ul>

<h2 id="use">夢占いを、自分のために使うには</h2>
<p>夢占いは「未来を当てるもの」より、「今の自分の気持ちに気づくきっかけ」として使うと役立ちます。</p>
<ol>
  <li><b>起きたらすぐ、動かずに思い出す。</b>体を動かすと、夢はすぐに消えていきます。</li>
  <li><b>枕元のメモに書く。</b>場面、出てきた人、そして<b>感じた気持ち</b>（怖い・うれしい・焦る）を短く。気持ちがいちばん大切な手がかりです。</li>
  <li><b>最近の出来事と並べる。</b>「この焦る感じは、来週の締め切りと似ている」など、起きているときの出来事とのつながりを探します。</li>
  <li><b>夢辞典は「ひとつの見方」として。</b>一般的な解釈を読んで、しっくりくるものだけを取り入れます。</li>
  <li><b>2週間ほど続けて、読み返す。</b>何度も出てくる場面や気持ちが、今の自分のテーマかもしれません。</li>
</ol>

<h2 id="common">よく見る夢と、昔から言われる解釈</h2>
<p>以下は、夢占いで一般に言われている解釈です。科学的に確かめられたものではないので、自分の気持ちと照らし合わせる材料としてお読みください。</p>
<div class="table-wrap"><table>
<tr><th>夢</th><th>よく言われる解釈</th><th>自分に聞いてみる問い</th></tr>
<tr><td>追いかけられる</td><td>プレッシャーや、避けたいことがある</td><td>最近、後回しにしていることは？</td></tr>
<tr><td>高いところから落ちる</td><td>不安、自信が揺らいでいる</td><td>足元がぐらついていると感じることは？</td></tr>
<tr><td>遅刻する・乗り遅れる</td><td>準備不足への心配、焦り</td><td>間に合わないと感じていることは？</td></tr>
<tr><td>試験を受ける</td><td>評価されることへの緊張</td><td>誰かの目を気にしている場面は？</td></tr>
<tr><td>歯が抜ける</td><td>変化への不安、見た目や自信のこと</td><td>失いたくないと思っているものは？</td></tr>
<tr><td>空を飛ぶ</td><td>解放感、自由になりたい気持ち</td><td>どこから自由になりたい？</td></tr>
<tr><td>亡くなった人が出てくる</td><td>その人への思い、自分の中の記憶の整理</td><td>その人に伝えたかったことは？</td></tr>
</table></div>

<h2 id="nightmare">怖い夢が続くとき</h2>
<p>ときどき悪夢を見るのは、よくあることです。ただ、悪夢がたびたび起きて眠りが妨げられ、日中の生活にも影響しているときは、「悪夢障害」という睡眠の病気の可能性があります。つらい出来事のあとに悪夢が続く場合も含め、睡眠の専門医や心療内科・精神科に相談してください。</p>
'''.replace("{toc}", toc([("science", "夢について、わかっていること"), ("use", "夢占いを、自分のために使うには"), ("common", "よく見る夢と、昔から言われる解釈"), ("nightmare", "怖い夢が続くとき")]))
    article("dreams", "夢の研究でわかっていることと、夢日記を使って今の気持ちに気づく方法を紹介します。", body,
            ["schredl", "nielsen", "ncnp"], ["moon", "fortune-and-mind", "how-to-ask"])

# ---------------- 四柱推命 ----------------

STEMS = [("甲", "きのえ", "木", "陽", "大きな木。まっすぐ伸びる、向上心のある人。"),
         ("乙", "きのと", "木", "陰", "草花。しなやかで、周りと調和できる人。"),
         ("丙", "ひのえ", "火", "陽", "太陽。明るく、周りを照らす人。"),
         ("丁", "ひのと", "火", "陰", "ともしび。静かな情熱と、細やかな心配りの人。"),
         ("戊", "つちのえ", "土", "陽", "山。どっしりと構え、頼りにされる人。"),
         ("己", "つちのと", "土", "陰", "田畑。人やものを育てる、面倒見のよい人。"),
         ("庚", "かのえ", "金", "陽", "鉄や刀。決断力があり、筋を通す人。"),
         ("辛", "かのと", "金", "陰", "宝石。繊細で、美しいものを大切にする人。"),
         ("壬", "みずのえ", "水", "陽", "大河や海。おおらかで、自由を好む人。"),
         ("癸", "みずのと", "水", "陰", "雨や露。やさしく、しみわたるような人。")]
BRANCHES = "子丑寅卯辰巳午未申酉戌亥"

def shichu():
    stems_js = json.dumps([list(s) for s in STEMS], ensure_ascii=False)
    rows = "".join(f'<tr><th>{s[0]}</th><td>{s[1]}</td><td>{s[2]}（{s[3]}）</td><td>{s[4]}</td></tr>' for s in STEMS)
    script = '''<script>
document.addEventListener("DOMContentLoaded", function () {
  var STEMS = %s, BR = "%s";
  var f = document.getElementById("ss-form");
  f.addEventListener("submit", function (e) {
    e.preventDefault();
    var y = +f.y.value, m = +f.m.value, d = +f.d.value, out = document.getElementById("ss-result");
    var t = new Date(Date.UTC(y, m - 1, d));
    if (!y || !m || !d || t.getUTCMonth() !== m - 1 || y < 1900 || y > 2100) { out.innerHTML = "<p class=muted>生年月日をもう一度ご確認ください。</p>"; out.classList.add("show"); return; }
    // ユリウス通日（正午）。2000年1月1日＝2451545（戊午）
    var jdn = Math.floor(t.getTime() / 86400000) + 2440588;
    var day = ((jdn + 49) %% 60 + 60) %% 60;
    var s = STEMS[day %% 10], b = BR[day %% 12];
    var yi = (((y - 4) %% 60) + 60) %% 60;
    var early = (m === 1) || (m === 2 && d <= 3);
    var yearStr = early ? "前の年の " + STEMS[((yi + 59) %% 60) %% 10][0] + BR[((yi + 59) %% 60) %% 12] : STEMS[yi %% 10][0] + BR[yi %% 12];
    out.innerHTML = '<p class="muted small" style="margin:0">あなたの日柱（生まれた日の干支）</p>' +
      '<div class="big-num">' + s[0] + b + '</div>' +
      '<p>日干は<b>「' + s[0] + '（' + s[1] + '）」</b>。五行は' + s[2] + '（' + s[3] + '）です。' + s[4] + '</p>' +
      '<p class="muted small">年柱の目安：' + yearStr + (m === 2 && d >= 3 && d <= 5 ? '（2月3〜5日生まれの方は、その年の立春の日時で変わります）' : '') + '</p>';
    out.classList.add("show");
  });
});
</script>''' % (stems_js, BRANCHES)
    body = f'''
{toc([("what","四柱推命とは"),("kanshi","干支（十干と十二支）"),("gogyo","五行"),("calc","日干を計算する"),("stems","10の日干"),("next","もっと学ぶには"),("note","知っておきたいこと")])}
<h2 id="what">四柱推命とは</h2>
<p>四柱推命は、中国で生まれた占いです。生まれた<b>年・月・日・時刻</b>の4つを、それぞれ干支（かんし）で表したものを「柱」と呼び、4本の柱から性格や運の流れを読みます。中国では「子平（しへい）」「八字（はちじ）」とも呼ばれ、宋の時代ごろに今の形に近い方法がまとめられたとされています。日本には江戸時代に伝わりました。</p>

<h2 id="kanshi">干支（十干と十二支）</h2>
<p>十干（甲・乙・丙・丁・戊・己・庚・辛・壬・癸）と、十二支（子・丑・寅・卯・辰・巳・午・未・申・酉・戌・亥）を順に組み合わせると、60通りの組み合わせができます。これを<b>六十干支</b>と呼び、年・月・日・時刻それぞれに順番に割り当てられています。</p>
<ul>
  <li><b>年の干支</b>：四柱推命では、1月1日ではなく<b>立春</b>（毎年2月4日ごろ）で年が変わります。</li>
  <li><b>月の干支</b>：二十四節気の「節」（立春・啓蟄・清明など）で月が変わります。節の日時は年によって変わるので、暦（万年暦）で確かめます。</li>
  <li><b>日の干支</b>：60日で一巡し、毎日一つずつ進みます。</li>
  <li><b>時刻の干支</b>：2時間ごとに十二支が割り当てられます（23時〜1時が子の刻）。</li>
</ul>

<h2 id="gogyo">五行</h2>
<p>十干は、<b>木・火・土・金・水</b>の5つの要素（五行）と、陰陽に分けられます。五行には、互いを生み出す関係（相生：木→火→土→金→水→木）と、抑える関係（相剋：木→土→水→火→金→木）があるとされ、4本の柱の中の五行のバランスから、その人の性質を読みます。</p>

<h2 id="calc">日干を計算する</h2>
<p>四柱推命では、生まれた日の干（<b>日干</b>）を「その人自身」として、読み解きの中心にします。生年月日を入れると、日柱（生まれた日の干支）と日干がわかります。</p>
<form class="tool panel" id="ss-form">
  <div class="row">
    <input name="y" type="number" inputmode="numeric" min="1900" max="2100" placeholder="1985" aria-label="年" style="width:110px"> 年
    <input name="m" type="number" inputmode="numeric" min="1" max="12" placeholder="7" aria-label="月" style="width:80px"> 月
    <input name="d" type="number" inputmode="numeric" min="1" max="31" placeholder="23" aria-label="日" style="width:80px"> 日
  </div>
  <p style="margin:16px 0 0"><button class="btn btn-primary" type="submit">計算する</button></p>
  <div class="result" id="ss-result" aria-live="polite"></div>
  <p class="muted small" style="margin:14px 0 0">日の干支は、ユリウス通日（紀元前4713年1月1日からの通し日数）から計算しています（2000年1月1日＝戊午）。0時で日が変わるものとしています。流派によっては23時（子の刻）で日を変えるため、23時台に生まれた方は次の日の干支になることがあります。入力はこのページの中だけで使い、送信しません。</p>
</form>
{script}

<h2 id="stems">10の日干</h2>
<p>日干は、自然のものにたとえて読まれることが多いです。以下は一般的なたとえです。</p>
<div class="table-wrap"><table><tr><th>日干</th><th>読み</th><th>五行</th><th>たとえと性質</th></tr>{rows}</table></div>

<h2 id="next">もっと学ぶには</h2>
<ul>
  <li>まずは自分の<b>4本の柱</b>を万年暦で調べて、紙に書き出してみましょう。生まれた時刻がわからないときは、年・月・日の3本（三柱）で読む方法もあります。</li>
  <li>次に、柱に含まれる五行を数えて、多いもの・少ないものを見ます。</li>
  <li>そのあと「通変星（つうへんせい）」「十二運」など、日干とほかの干支との関係を表す考え方に進みます。流派による違いが大きい分野なので、1冊の入門書を軸に学ぶのがおすすめです。</li>
</ul>

<h2 id="note">知っておきたいこと</h2>
<p>四柱推命は、暦の計算にもとづく伝統的な占いです。生年月日から性格や運命を読む占いの効果は、科学的には確かめられていません（占星術について、二重盲検という方法で検証した研究などがあります）。自分を見つめ直すための「ひとつの物差し」として楽しんでください。</p>
'''
    article("shichu-suimei", "干支と五行のしくみ、立春で年が変わる理由など、四柱推命の入り口をまとめました。生まれた日の干（日干）をその場で計算できます。", body,
            ["nao_24", "carlson"], ["numerology", "fortune-and-mind", "moon"])

# ---------------- 手相 ----------------

def palmistry():
    body = f'''
{toc([("what","手相とは"),("hand","どちらの手を見る？"),("lines","4つの主な線"),("mounts","丘"),("how","見方のコツ"),("study","手相についての研究")])}
<h2 id="what">手相とは</h2>
<p>手相は、手のひらの線やふくらみ、手の形から、性格やこれからを読む占いです。古代インドで生まれ、中国やペルシャ、古代ギリシャなどに広まったと考えられています。19世紀には、ヨーロッパで手相の本が多く出版され、今の見方のもとになりました。</p>

<h2 id="hand">どちらの手を見る？</h2>
<p>よく言われるのは、「利き手はこれまでの生き方やこれから、反対の手は生まれ持ったもの」という見方です。ただし流派によって考え方は違います。はじめは両手を並べて、違いを見てみましょう。</p>

<h2 id="lines">4つの主な線</h2>
<div class="table-wrap"><table>
<tr><th>線</th><th>場所</th><th>一般に読まれること</th></tr>
<tr><td>生命線</td><td>親指と人さし指の間から、親指の付け根を囲むように手首へ</td><td>体力、生活の活力</td></tr>
<tr><td>頭脳線（知能線）</td><td>生命線と同じあたりから、手のひらを横切る</td><td>考え方のくせ、物事の決め方</td></tr>
<tr><td>感情線</td><td>小指の下から、人さし指・中指の方へ</td><td>気持ちの表し方、人との関わり方</td></tr>
<tr><td>運命線</td><td>手首の近くから、中指に向かって縦に</td><td>仕事や生き方の流れ（はっきりしない人も多い線です）</td></tr>
</table></div>
<p>線の長さだけでなく、濃さ・分かれ方・途切れ方も読みます。</p>

<h2 id="mounts">丘</h2>
<p>指の付け根などのふくらみを「丘」と呼び、それぞれに意味があるとされます。代表的なのは、親指の付け根の<b>金星丘</b>（愛情・活力）、小指側の手首に近い<b>月丘</b>（想像力・感受性）です。</p>

<h2 id="how">見方のコツ</h2>
<ul>
  <li>明るい場所で、手を軽く曲げると線がはっきり見えます。</li>
  <li>スマートフォンで手のひらの写真を撮っておくと、数か月後に見比べられます。細い線は、生活とともに変わることがあります。</li>
  <li>線の意味を「良い・悪い」で決めつけず、自分の性格をふり返る材料にしましょう。</li>
</ul>

<h2 id="study">手相についての研究</h2>
<p>「生命線が短いと寿命が短い」という話を聞いたことがあるかもしれません。これについては、いくつかの研究があります。</p>
<ul>
  <li>1990年にイギリスで、亡くなった100人の手を調べ、生命線の長さと亡くなった年齢に関連がある、と報告した研究がありました。</li>
  <li>一方、2019年にオーストラリアで60人の遺体を調べた研究では、生命線の長さと寿命のあいだに関連は見つかりませんでした。研究者は「生命線で寿命は予測できない」と結論づけています。</li>
</ul>
<p>今のところ、手相で寿命や将来を言い当てられるという科学的な根拠はありません。生命線が短くても、心配する必要はありません。</p>
'''
    article("palmistry", "生命線・頭脳線・感情線・運命線の見方と、手相についての研究をまとめました。", body,
            ["brit_palm", "newrick", "lucas"], ["fortune-and-mind", "shichu-suimei", "numerology"])

# ---------------- 占いとこころ ----------------

def fortune_and_mind():
    body = '''
<h2>「当たっている」と感じるしくみ</h2>
<p>1948年、アメリカの心理学者フォアは、学生たちに性格テストを受けてもらい、後日「あなただけの分析結果」を渡しました。実は全員に同じ文章（星占いの本などから集めたもの）を渡していたのですが、学生たちは「どのくらい当たっているか」を5点満点で平均4.26点と評価しました。</p>
<p>「あなたには、まだ活かしきれていない力があります」のように、誰にでも当てはまる言葉を「自分のことだ」と感じやすい心のしくみは、<b>バーナム効果</b>（フォア効果）と呼ばれています。</p>
<p>ほかにも、当たったことはよく覚えていて、外れたことは忘れやすい、という心のくせ（<b>確証バイアス</b>）もあります。</p>

<h2>それでも、占いが役に立つとき</h2>
<p>占いの言葉が「当たるかどうか」とは別に、占いには次のような使い方があります。</p>
<ul>
  <li><b>気持ちを整理するきっかけ。</b>カードや数字の言葉を手がかりに、「自分は本当はどうしたいのか」を考えられます。</li>
  <li><b>行動を後押しするきっかけ。</b>迷っていたことに、小さく一歩を踏み出す理由になります。</li>
  <li><b>ひと息つく時間。</b>数分でも自分のことを考える時間は、忙しい毎日の中で貴重です。</li>
</ul>

<h2>上手に付き合うための5つのこと</h2>
<ol>
  <li>結果は「参考」にとどめ、最後は自分で決める。</li>
  <li>良い結果は背中を押す言葉として、慎重な結果は見直しのヒントとして読む。</li>
  <li>望む答えが出るまで占い直さない。</li>
  <li>健康・お金・法律など大切なことは、専門家に相談する。</li>
  <li>占いのために、生活に無理が出るほどのお金や時間を使わない。</li>
</ol>

<h2>困ったときの相談先</h2>
<p>「このままだと不幸になる」と不安をあおられ、高額な開運グッズやお祓いなどを勧められるトラブルが起きています。おかしいと感じたら、契約する前に相談してください。</p>
<ul>
  <li><b>消費者ホットライン「188」</b>：お住まいの地域の消費生活センターなどの相談窓口を案内してくれます（相談は無料、通話料はかかります）。</li>
</ul>
<p>気持ちのつらさが続くときや、眠れない日が続くときは、占いだけで抱えこまず、身近な人や医療機関に相談してください。</p>
'''
    article("fortune-and-mind", "「当たっている」と感じる心のしくみと、占いを日々に活かすためのヒント、困ったときの相談先をまとめました。", body,
            ["forer", "caa"], ["how-to-ask", "numerology", "tarot-howto"])

def index_page():
    groups = {}
    for slug, title, desc, cat in ARTICLES:
        groups.setdefault(cat, []).append((slug, title, desc))
    parts = []
    for cat, items in groups.items():
        lis = "".join(f'<a class="panel guide-item" href="{s}.html"><h3>{t}</h3><p class="muted small">{d}</p></a>' for s, t, d in items)
        parts.append(f'<h2 class="suit-title">{cat}</h2><div class="guide-list">{lis}</div>')
    body = f'''
<section style="padding-top:30px">
  <div class="wrap">
    <p class="eyebrow">読み物</p>
    <h1 class="sec-title" style="font-size:34px">占いを学ぶ読み物</h1>
    <p class="sec-lead">タロットのやり方から、数秘術・月・夢・四柱推命・手相まで。できるだけ信頼できる資料や研究をもとに、読んだその日から使える形でまとめています。各ページの最後に参考文献を載せています。</p>
    {"".join(parts)}
    <h2 class="suit-title">カードの意味</h2>
    <div class="guide-list"><a class="panel guide-item" href="{R}cards/index.html"><h3>タロットカード78枚の意味</h3><p class="muted small">正位置・逆位置の意味を、恋愛・仕事・人間関係などのテーマ別に。</p></a></div>
  </div>
</section>
{cta_band(R)}
'''
    page("guide/index.html", "占いを学ぶ読み物",
         "タロット占いのやり方、スプレッド、逆位置、数秘術、月齢、夢占い、四柱推命、手相。信頼できる資料をもとに、占いを学びたい方向けにまとめた読み物です。",
         body, crumbs=[(None, "読み物")])

def build(cards):
    tarot_howto(cards); tarot_basics(); spreads(); reversed_(cards); how_to_ask()
    numerology(); moon(); dreams(); shichu(); palmistry(); fortune_and_mind(); index_page()
