import os
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        # 環境変数をロード
        load_dotenv()

        # OpenAI のクライアント設定
        self.client = "OpenAIのクライアントを立てる"
        self.model = "モデル名"