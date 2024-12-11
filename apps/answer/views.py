from flask import Blueprint, render_template, request, redirect, url_for, flash
from apps.app import db
from apps.answer.models import Answer
from apps.answer.forms import AnswerForm

answer = Blueprint(
    "answer",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@answer.route("/", methods=["GET", "POST"])
def index():
    form = AnswerForm()
    if form.validate_on_submit():
        user_number = form.user_number.data

        # 新しいAnswerインスタンスを作成してデータベースに保存
        answer = Answer(user_number=user_number)
        db.session.add(answer)
        db.session.commit()

        flash("班を記入しました", "success")
        return redirect(url_for("answer.list_answers"))

    return render_template("answer/index.html", form=form)


@answer.route("/list", methods=["GET"])
def list_answers():
    # データベースからすべてのAnswerデータを取得
    answers = Answer.query.all()
    return render_template("answer/list.html", answers=answers)
