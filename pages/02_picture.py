import base64

import streamlit as st

from config import OpenAIClient

# openai client
client = OpenAIClient()

# promptファイル
PROMPT_FILE = "./prompts/02_animal.md"

def init_page():
    """ ページ設定 """
    st.set_page_config(
        page_title = "Picture x llm"
    )
    st.title("Picture x llm")
    if "picture_chat_log" not in st.session_state:
        st.session_state.picture_chat_log = []


def png_upload():
    """ PNGファイルのアップローダー """
    # jpg, jpeg, pngを受け入れるアップローダーを作成してください
    # まず、アップロードされたファイルをtemp folderに格納し、そのデータをエンコードしにいくコードを考えてみると分かりやすいかもです。
    # ただ、できれば無駄なフォルダを作りたくないので、直接エンコードできればなお良しです。
    picture = st.file_uploader("画像を選択", type=["png", "jpeg", "jpg"])
    if picture is None:
        return None
    b64_pct = encode_image(picture)
    return b64_pct


def encode_image(picture):
    """ 画像をBase64エンコード """
    b64_pct = base64.b64encode(picture.read()).decode("utf-8")
    return b64_pct



def get_prompt(filepath):
    """ システムプロンプトの取得 """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def get_llm_response(query, b64_pct=None):
    """ LLMにクエリを送信し、回答を取得 """
    prompt = get_prompt(PROMPT_FILE)
    # システムプロンプト入力
    messages = [{"role": "system", "content": prompt}]
    # 過去プロンプトを順番に追加
    messages += [
        {"role": "assistant", "content": log["content"]} if log["role"] == "assistant"
        else {"role": "user", "content": log["content"]}
        for log in st.session_state.picture_chat_log
    ]
    # 今回のプロンプトを追加
    if b64_pct is None:
        messages.append({"role": "user", "content": query})
    else:
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpeg;base64,{b64_pct}"
                    }
                }
            ]
        })
    # LLMに投げる
    response = client.client.chat.completions.create(
        model=client.model,
        messages=messages,
        temperature=0
    )
    answer = response.choices[0].message.content
    return answer

def chat_interface():
    """ chat機能全般 """
    # ログ表示
    for message in st.session_state.picture_chat_log:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.chat_input("質問を入力")
    b64_pct = png_upload()
    if query:
        answer = get_llm_response(query, b64_pct)

        with st.chat_message("user"):
            st.write(query)
            if b64_pct is not None:
                st.image(
                    f"data:image/jpeg;base64,{b64_pct}",
                    caption="あなたがアップロードした画像"
                )

        with st.chat_message("assistant"):
            st.write(answer)

        # 履歴に追加
        st.session_state.picture_chat_log.append({"role": "user", "content": query})
        st.session_state.picture_chat_log.append({"role": "assistant", "content": answer})

def main():
    init_page()
    chat_interface()


if __name__ == "__main__":
    main()