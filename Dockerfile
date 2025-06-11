# ベースイメージ
FROM python:3.11

# 作業ディレクトリ
WORKDIR /app

# 依存関係を先にコピーしてキャッシュ効かせる
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 残りのコードをコピー
COPY . .

# 環境変数の名前を宣言
ENV OPENAI_API_KEY=""

# Streamlit のデフォルトポートを開放
EXPOSE 8501

# コンテナ起動時に Streamlit を自動実行
ENTRYPOINT ["streamlit", "run"]
CMD ["home.py", "--server.address=0.0.0.0", "--server.port=8501"]