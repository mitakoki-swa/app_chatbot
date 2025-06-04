import streamlit as st

from config import OpenAIClient

# openai client
client = OpenAIClient()

# promptファイル
PROMPT_FILE = "./prompts/03_createImage.md"

def init_page():
    """ ページ設定 """
    st.set_page_config(
        page_title = "text2image x llm"
    )
    st.title("text2image x llm")
    if "chat_image_log" not in st.session_state:
        st.session_state.chat_image_log = []


def get_prompt(filepath):
    """ システムプロンプトの取得 """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def get_llm_response(query):
    """ LLMにクエリを送信し、回答を取得 """
    prompt = get_prompt(PROMPT_FILE)
    # LLMに投げる
    response = client.client.images.generate(
        model=client.image_model,
        prompt=query,
        n=1,
        size="1024x1024"
    )
    answer = response.data[0].url
    return answer


def chat_interface():
    """ chat機能全般 """
    # ログ表示
    for message in st.session_state.chat_image_log:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.write(message["content"])
            else:
                st.image(message["image"])
    query = st.chat_input("質問を入力")
    if query:
        answer = get_llm_response(query)
        with st.chat_message("user"):
            st.write(query)

        with st.chat_message("assistant"):
            st.image(answer)

        # 履歴に追加
        st.session_state.chat_image_log.append({"role": "user", "content": query})
        st.session_state.chat_image_log.append({"role": "assistant", "image": answer})


def main():
    init_page()
    chat_interface()


if __name__ == "__main__":
    main()