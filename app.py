import streamlit as st

def init_page():
    '''stleamlit 初期化'''
    st.set_page_config(
        page_title = 'Echo Bot'
    )
    st.title('Echo Bot')

def init_chat():
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

def print_chat_log():
    '''chatの履歴を表示'''
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

def create_chat(prompt):
    '''promptを読み取りbotが返信する'''
    # 入力を出力
    with st.chat_message('user'):
        st.markdown(prompt)
    # 入力したchatを履歴に追加
    st.session_state.messages.append({'role':'user', 'content':prompt})
    # botが返信
    response = f'echo:{prompt}'
    with st.chat_message('assistant'):
        st.markdown(response)
    # botの返答を履歴に追加
    st.session_state.messages.append({'role':'assistant', 'content':response})

def main():
    init_chat()
    print_chat_log()
    if prompt := st.chat_input('What is up?'):
        create_chat(prompt)

if __name__ == '__main__':
    init_page()
    main()