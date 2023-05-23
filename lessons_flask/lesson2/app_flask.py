from flask import Flask, request, render_template
from news_view import news_route, news_list

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return render_template("index.html", news_list=news_list)


app.register_blueprint(news_route)


app.run()
