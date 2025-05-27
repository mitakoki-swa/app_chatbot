import streamlit as st


def init_page():
    """ ページ設定 """
    st.set_page_config(
        page_title = "Echo Bot"
    )
    st.title("Echo Bot")
    if "messages" not in st.session_state:
        st.session_state.messages = []


def get_llm_response(query):
    """ LLMにクエリを送信し、回答を取得 """
    # ここの関数を完成させてください。
    return "LLMの生成結果"


def chat_interface():
    """ chat機能全般 """
    # ログ表示
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.chat_input("質問を入力")
    if query:
        answer = get_llm_response()

        with st.chat_message("user"):
            st.write(query)

        with st.chat_message("assistant"):
            st.write(answer)

    # 履歴に追加
    st.session_state.messages.append({"role": "user", "content": query})
    st.session_state.messages.append({"role": "assistant", "content": answer})


def main():
    init_page()
    chat_interface()

if __name__ == "__main__":
    main()