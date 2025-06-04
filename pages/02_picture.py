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
    picture = st.file_uploader(
        label="画像を選択",
        type=["png", "jpeg", "jpg"],
        accept_multiple_files=False
        )
    if picture:
        return picture.read()
    else:
        return None


def encode_image(pct_byte):
    """ 画像をBase64エンコード """
    return base64.b64encode(pct_byte).decode("utf-8")


def show_pct(pct_byte):
    """アップロードされた画像を表示"""
    st.image(pct_byte)


def get_prompt(filepath):
    """ システムプロンプトの取得 """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def get_llm_response(query, pct_b64=None):
    """ LLMにクエリを送信し、回答を取得 """
    prompt = get_prompt(PROMPT_FILE)
    # システムプロンプト入力
    messages = [{"role": "system", "content": prompt}]
    # 過去プロンプトを順番に追加
    for log in st.session_state.picture_chat_log:
        if log["role"] == "user":
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": log["content"]},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpeg;base64,{log['image']}"
                        }
                    }
                ]
            })
        else:
            messages.append({
                "role": "assistant",
                "content": log["content"]
            })
    # 今回のプロンプトを追加
    messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpeg;base64,{pct_b64}"
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

def chat_interface(pct_byte):
    """ chat機能全般 """
    # ログ表示
    for message in st.session_state.picture_chat_log:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    pct_b64 = encode_image(pct_byte)
    query = st.chat_input("質問を入力")
    if query:
        answer = get_llm_response(query, pct_b64)

        with st.chat_message("user"):
            st.write(query)

        with st.chat_message("assistant"):
            st.write(answer)

        # 履歴に追加
        st.session_state.picture_chat_log.append({"role": "user", "content": query, "image": pct_b64})
        st.session_state.picture_chat_log.append({"role": "assistant", "content": answer})

def main():
    init_page()
    image = png_upload()
    if image:
        show_pct(image)
        chat_interface(image)


if __name__ == "__main__":
    main()