import os
import streamlit as st

"""
- クライアントを立てる機能を、config.pyにまとめ、各ページでロードする形にしてください。
- まず、以下の部分が不要になります。
```
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

- 次に、clientの立て方がちょっと変わります。
- 伝え忘れてましたが、キーワード引数の=前後は空白無しでもOKです。このコメントも消していただいてOKです。
```
    response = client.client.chat.completions.create(
        model=client.model,
        messages=messages,
        temperature=0
    )
```

- これのメリットとして、例えばモデルを変更するとき、pages配下の各pyファイルのmodelを内直す必要がなくなります。configだけ変更すればいいので。
- こんな感じでモジュールごとにファイルを分けるのがおすすめです。

- さらに、システムプロンプトを prompts フォルダ配下で md ファイルして管理できるようにします。
- 今後、プロンプトがどんどん長大になってくるので、こうすると管理が楽です。

"""

from config import OpenAIClient

# openai client
client = OpenAIClient()

# promptファイル
PROMPT_FILE = "./prompts/01_SES.md"

def init_page():
    """ ページ設定 """
    st.set_page_config(
        page_title = "Echo Bot"
    )
    st.title("Echo Bot")
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []


def get_prompt(filepath):
    """ システムプロンプトの取得 """
    # ここ埋めてみてください。
    # pythonのwith句とopen関数を使用します。ついでに、それらの機能も調べていただけると。
    pass


def get_llm_response(query):
    """ LLMにクエリを送信し、回答を取得 """
    prompt = get_prompt(PROMPT_FILE)
    # システムプロンプト入力
    messages = [{"role": "system", "content": prompt}]
    # 過去プロンプトを順番に追加
    messages += [
        {"role": "assistant", "content": log["content"]} if log["role"] == "assistant"
         else {"role": "user", "content": log["content"]}
         for log in st.session_state.chat_log
    ]
    # 今回のプロンプトを追加
    messages += [{"role": "user", "content": query}]
    response = client.client.chat.completions.create(
        model=client.model, # model="gpt-4o-mini",
        messages=messages,
        temperature=0
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