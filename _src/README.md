# サイトの作り方（_src）

このフォルダは GitHub Pages には公開されません（`_` で始まるフォルダは Jekyll が除外）。

- `build.py`：全ページを作る入口。`python3 build.py`
- `common.py`：共通のヘッダー・フッター、URL、Play ストアのリンク（`PLAY_URL`）、メールアドレス
- `pages.py`：トップ・特長・使い方・よくある質問・お問い合わせ・404
- `cards.py`：カードの意味（アプリの `cards.json` から78ページを作る）
- `guide.py`：読み物11本と参考文献（`REFS`）

使う前に `common.py` の `SRC`（アプリの `assets/text/ja/` の場所）と `OUT`（出力先）を自分の環境に合わせてください。
スタイルは `assets/style.css`、月齢と数秘術の計算は `assets/site.js`。
