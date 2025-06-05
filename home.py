import streamlit as st

def init_page():
    st.set_page_config(
        page_title="個人用gpt4o",
        page_icon="📚"
    )
    st.info("☜ 選択してね")

def main():
    init_page()
    st.markdown("""
# LLM Multimodal ChatBot
このアプリでは、以下の機能が使えます：
***
1. **text2text**: テキストを入力するとAIがSES業界に精通したコンサルタントとしてテキストで返答してくれます。
2. **image2text**: 動物の写真をあげるとその動物の名前、特徴、面白い生態を教えてくれます。
3. **text2image**: テキストで写真のイメージを伝えるとそれに沿った画像を生成してくれます。
4. **image2image**: 画像をあげ、完成イメージを伝えると、その画像をイメージ通りに書き換えてくれます。
***
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
                """)

if __name__ == '__main__':
    main()