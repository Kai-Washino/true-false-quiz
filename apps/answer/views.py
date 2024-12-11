from flask import Blueprint, render_template

answer = Blueprint(
    "answer",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@answer.route("/")
def index():
    return "Hello World"