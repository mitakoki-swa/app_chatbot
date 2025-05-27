# Echo Bot
## 仕様
- こちらが投げかけた言葉をそのまま返してくれるchatボットです。
- 画面下の「What is up?」という欄にチャットを入力して下さい。
- その内容がbotから返ってきます。

## 起動方法
- `ctrl + @` ターミナル起動
- `py -3.11 -m venv .venv`を実行（Pythonバージョンに応じて-3.11を変化させる）
- `.venv/Scripts/activate`で仮想環境起動
- `pip install -r requirements.txt`を実行しライブラリインストール
- `streamlit run app.py`でアプリ起動