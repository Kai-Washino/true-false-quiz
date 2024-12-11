# ベースイメージの指定
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY app.py app.py

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナのデフォルト実行コマンド
CMD ["python", "app.py"]
