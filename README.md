# LLM Multimodal ChatBot
## 仕様
### text2text
- SES業界を熟知したChatBotです。こちらの質問に答えてくれます。
- 画面下の「What is up?」という欄にチャットを入力して下さい。
- その返答がbotから返ってきます。

### image2text
- 動物の鑑定に優れた画像認識ChatBotです。
- 画像を渡すとその動物の名前、特徴、面白い生態を教えてくれます。
- 使い方はtext2textと同じです。

### text2image
- イメージを伝えるとそれに沿った画像を作ってくれます。
- 生成された画像に対して、「他には？」「別のも作って」などと指示をすれば別バージョンの画像を生成します。

### image2image
- 渡した画像を指定通りに加工してくれます。
- 加工してくれた画像に対しても、そのまま指示を出すことで追加加工が可能です。

## 起動方法
- `ctrl + @` ターミナル起動
- `py -3.11 -m venv .venv`を実行（Pythonバージョンに応じて-3.11を変化させる）
- `.venv/Scripts/activate`で仮想環境起動
- `pip install -r requirements.txt`を実行しライブラリインストール
- `streamlit run home.py`でアプリ起動
  - 別途OPENAI_API_KEYが必要です。