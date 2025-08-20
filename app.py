from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище новостей
news_list = [
    {"title": "Новости 1", "content": "Содержание первой новости."},
    {"title": "Новости 2", "content": "Содержание второй новости."}
]

@app.route("/")
def index():
    return render_template("index.html", news=news_list)

@app.route("/add", methods=["GET", "POST"])
def add_news():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if title and content:
            news_list.append({"title": title, "content": content})
