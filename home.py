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
                
                # 個人用GPTアプリへようこそ
                このアプリでは、以下の機能が使えます：
                1. **text2text**:
                    テキストを入力するとAIがSES業界に精通したコンサルタントとしてテキストで返答してくれます。
                2. **image2text**:
                    動物の写真をあげるとその動物の名前、特徴、面白い生態を教えてくれます。
                3. **text2image**:
                    テキストで写真のイメージを伝えるとそれに沿った画像を生成してくれます。
                4. **image2image**:
                    画像をあげ、完成イメージを伝えると、その画像をイメージ通りに書き換えてくれます。
                """)

if __name__ == '__main__':
    main()