import os
import streamlit as st
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def init_page():
    """ ページ設定 """
    st.set_page_config(
        page_title = "Echo Bot"
    )
    st.title("Echo Bot")
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []


def get_llm_response(query):
    """ LLMにクエリを送信し、回答を取得 """
    # システムプロンプト入力
    messages = [{"role": "system", "content": "あなたは日本のSES企業の事情に精通するスペシャリストです"}]
    # 過去プロンプトを順番に追加
    messages += [
        {"role": "assistant", "content": log["content"]} if log["role"] == "assistant"
         else {"role": "user", "content": log["content"]}
         for log in st.session_state.chat_log
    ]
    # 今回のプロンプトを追加
    messages += [{"role": "user", "content": query}]
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages,
        temperature = 0
    )
    answer = response.choices[0].message.content
    return answer


def chat_interface():
    """ chat機能全般 """
    # ログ表示
    for message in st.session_state.chat_log:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.chat_input("質問を入力")
    if query:
        answer = get_llm_response(query)

        with st.chat_message("user"):
            st.write(query)

        with st.chat_message("assistant"):
            st.write(answer)
        # 履歴に追加
        st.session_state.chat_log.append({"role": "user", "content": query})
        st.session_state.chat_log.append({"role": "assistant", "content": answer})

def main():
    init_page()
    chat_interface()

if __name__ == "__main__":
    main()