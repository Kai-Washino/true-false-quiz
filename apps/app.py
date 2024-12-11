from flask import Flask
from pathlib import Path
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# データベースインスタンス
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # アプリケーション設定
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_SECRET_KEY="AuwzyszU5sugKN7KZs6f",
    )
    
    # データベースとマイグレーションの初期化
    db.init_app(app)
    Migrate(app, db)

    # Blueprintの登録
    from apps.answer import views as answer_views
    app.register_blueprint(answer_views.answer, url_prefix="/answer")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        upgrade()  # マイグレーションを適用
    app.run(host="0.0.0.0", port=8080)