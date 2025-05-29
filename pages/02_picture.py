import streamlit as st

def init_page():
    """ ページ設定 """
    st.set_page_config(
        page_title = "Picture"
    )
    st.title("Picture")


def main():
    init_page()


if __name__ == "__main__":
    main()