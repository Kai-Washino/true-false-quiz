from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AnswerForm(FlaskForm):
    user_number = StringField(
        "班番号",
        validators=[
            DataRequired(message="番号は必要です"),
            Length(max=2, message="2文字以下で記入してください")
        ],
    )
    submit = SubmitField("決定")
