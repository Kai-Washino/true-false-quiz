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

# 正解データを定義
CORRECT_ANSWERS = {
    "question1": "○",
    "question2": "×",
    "question3": "×",
    "question4": "×",
    "question5": "○",
    "question6": "×",
    "question7": "○",
    "question8": "○",
    "question9": "×",
    "question10": "○",
}

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
            return redirect(url_for("answer.thanks"))
    return render_template("answer/question.html", form=form, question_number=question_number)

@answer.route("/thanks")
def thanks():
    return render_template("answer/thanks.html")

@answer.route("/list")
def list_answers():
    answers = Answer.query.all()

    # 各回答の一致率を計算
    results = []
    for ans in answers:
        total_questions = 0
        correct_count = 0
        for key, correct_value in CORRECT_ANSWERS.items():
            user_answer = getattr(ans, key)
            if user_answer is not None:  # Null を除外
                total_questions += 1
                if user_answer == correct_value:
                    correct_count += 1
        accuracy = (correct_count / total_questions * 100) if total_questions > 0 else 0
        results.append({"answer": ans, "accuracy": accuracy})

    # 一致率で降順に並び替え
    results = sorted(results, key=lambda x: x["accuracy"], reverse=True)

    return render_template("answer/list.html", results=results)


@answer.route("/delete_all", methods=["POST"])
def delete_all():
    # データベースのすべてのレコードを削除
    Answer.query.delete()
    db.session.commit()
    flash("すべてのデータを削除しました", "success")
    return redirect(url_for("answer.list_answers"))