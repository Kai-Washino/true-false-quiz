from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length

class UserNumberForm(FlaskForm):
    user_number = StringField(
        "班番号",
        validators=[
            DataRequired(message="番号は必要です"),
            Length(max=2, message="2文字以下で記入してください")
        ],
    )
    submit = SubmitField("決定")

class QuestionForm(FlaskForm):
    answer = RadioField(
        "回答",
        choices=[("○", "○"), ("×", "×")],
        validators=[DataRequired(message="回答を選択してください")],
    )
    submit = SubmitField("次へ")