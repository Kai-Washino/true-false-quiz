# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt .
COPY apps/ ./apps/
COPY .env .env

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# 環境変数を設定
ENV FLASK_APP=apps.app:create_app
ENV FLASK_ENV=development

# コンテナ起動時に実行されるコマンド
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
