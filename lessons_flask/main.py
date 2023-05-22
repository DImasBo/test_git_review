from flask import Flask, render_template

app = Flask(__name__)

name = "Dmytro"

@app.route("/")
def hello():
    return f"<h1>Hello, {name}</h1>"


@app.route("/about")
def about():
    return f"<h1>Hello about</h1>"


@app.route("/news")
def news():
    return f"<h1>All news</h1>"


@app.route("/news/<name_post>")
def news_wather(name_post):

    return f"<h1>Новина {name_post}</h1>"


app.run()
