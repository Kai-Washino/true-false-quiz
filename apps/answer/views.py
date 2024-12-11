from flask import Blueprint, render_template, redirect, url_for, request, flash
from apps.app import db
from apps.answer.models import Answer
from apps.answer.forms import QuestionForm, UserNumberForm

answer = Blueprint(
    "answer",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@answer.route("/", methods=["GET", "POST"])
def index():
    form = UserNumberForm()
    if form.validate_on_submit():
        user_number = form.user_number.data
        # user_number に対応するデータベースレコードを作成または取得
        current_answer = Answer.query.filter_by(user_number=user_number).first()
        if not current_answer:
            current_answer = Answer(user_number=user_number)
            db.session.add(current_answer)
            db.session.commit()

        flash("班番号を記入しました", "success")
        return redirect(url_for("answer.question", user_number=user_number, question_number=1))

    return render_template("answer/index.html", form=form)


@answer.route("/question/<user_number>/<int:question_number>", methods=["GET", "POST"])
def question(user_number, question_number):
    form = QuestionForm()
    if form.validate_on_submit():
        answer_value = form.answer.data

        # データベースに回答を保存
        current_answer = Answer.query.filter_by(user_number=user_number).first()
        if current_answer:
            setattr(current_answer, f"question{question_number}", answer_value)
            db.session.commit()

        # 次の質問または完了ページへ
        if question_number < 10:
            return redirect(url_for("answer.question", user_number=user_number, question_number=question_number + 1))
        else:
            flash("全ての回答を送信しました", "success")
            return redirect(url_for("answer.list_answers"))

    return render_template("answer/question.html", form=form, question_number=question_number)


@answer.route("/list")
def list_answers():
    # 全ての回答を取得
    answers = Answer.query.all()
    return render_template("answer/list.html", answers=answers)
