import os
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        # 環境変数をロード
        load_dotenv()

        # OpenAI のクライアント設定
        self.api_key = os.getenv("OPENAI_API_KEY")

        self.client = OpenAI(self.api_key)
        self.model = "gpt-4o-mini"