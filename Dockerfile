# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY apps/ ./apps/
COPY migrations/ ./migrations/  
COPY .env .env

# パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# 環境変数を設定
ENV FLASK_APP=apps.app:create_app
ENV FLASK_ENV=production

# コンテナ実行時にマイグレーションを実行してアプリを起動
CMD flask db upgrade && flask run --host=0.0.0.0 --port=8080
