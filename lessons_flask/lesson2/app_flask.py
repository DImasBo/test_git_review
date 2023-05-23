from flask import Flask, request
from news_view import news_route
app = Flask(__name__)
app.debug = True


@app.route("/index")
def hello():
    return "<h1>Hello, World!</h1>"


app.register_blueprint(news_route)


app.run()
