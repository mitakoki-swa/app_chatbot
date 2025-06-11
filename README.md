# LLM Multimodal ChatBot
Dockerを使用したマルチモーダルなチャットボットです。

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

## 前提
- Dockerがインストール・起動済みであること
- OPENAI_API_KEYを取得していること

## 起動方法
- UbuntuなどのLinux環境において、リポジトリをクローンしたいディレクトリに移動
- `code .`でVS Codeを起動
- `app_chatbot`リポジトリをクローン
- `.env`ファイルをDockerfileと同階層に作成し、下記のように取得したOPENAI_API_KEYを環境変数に設定
```
OPENAI_API_KEY=your_api_key
```
- bashにおいて下記コマンドによりビルド
```bash
docker build -t your_image_name:latest .
```
- 環境変数を読み込ませてアプリを起動
```bash
docker run \
  --rm \
  --env-file .env \
  -p 8501:8501 \
  your_image_name:latest
```
