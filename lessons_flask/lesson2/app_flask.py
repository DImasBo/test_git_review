from flask import Flask

app = Flask(__name__)
app.debug = True

news_list = [
    {
        "name": "Призедент зустрівся з Байденом",
        "context": "опис фівафдільвдщлфіьвфюю ...",
        "author": "ТСН"
    }
]

@app.route("/index")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/news/<index_news>")
def news(index_news):
    index_news = int(index_news)
    if index_news >= len(news_list):
        return "<h1>такої новини немає у списку</h1>"
    news = news_list[index_news]
    return f"<h1>Новина: {news['name']}</h1>" \
           f"<p>{news['context']}</p>"\
           f"<p> <small>author:{news['author']}</small></p>"


app.run()
