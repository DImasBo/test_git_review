from flask import Flask, render_template

app = Flask(__name__)

name = "Dmytro"

news_all = {
    "Погода": "На вулиці ясно температура 22",
    "Bitcoin": "Біткоїн знову упав!...",
    "ПризедетЗустріч": "Призедин зустрівся з кимось ...!...",
}


@app.route("/")
def hello():
    return f"<h1>Hello, {name}</h1>"


@app.route("/news/<name_post>")
def news_wather(name_post):
    news = news_all.get(name_post)
    if not news:
        return "<h1>Такої новини в нас немає :(</h1>"
    return f"<h1>Новина: {name_post}</h1>" \
           f"<p>{news}</p>"


app.run()
