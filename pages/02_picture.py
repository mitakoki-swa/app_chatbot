import streamlit as st


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
    return


def encode_image():
    """ 画像をBase64エンコード """
    # エンコード結果をリターンしてください
    return


def get_prompt(filepath):
    """ システムプロンプトの取得 """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def get_llm_response():
    """ LLMにクエリを送信し、回答を取得 """
    # ここは一緒です
    # messages = [{"role":"system", "content": prompt}]
    # 画像データは append する方法が違います。以下ヒントです。これを元に格納してみてください。
    # messages.append({
    #     "role": "user",
    #     "content": [
    #         {"type": "text", "text": query},
    #         {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
    #     ]
    # })
    # もし画像データがないなら、textだけappendすればいいです。
    # messages.append({"role": "assistant", "content": アンサー]})
    return


def chat_interface():
    """ chat機能全般 """
    # ログ表示
    for message in st.session_state.picture_chat_log:
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
        st.session_state.picture_chat_log.append({"role": "user", "content": query})
        st.session_state.picture_chat_log.append({"role": "assistant", "content": answer})


def main():
    init_page()
    # chat_interface()


if __name__ == "__main__":
    main()