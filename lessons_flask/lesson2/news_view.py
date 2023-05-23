from flask import Blueprint, request, render_template

news_route = Blueprint("news", __name__, url_prefix="/news")

news_list = [
    {
        "name": "Призедент зустрівся з Байденом",
        "context": "опис фівафдільвдщлфіьвфюю ...",
        "author": "ТСН"
    }
]


@news_route.route("/<index_news>")
def news(index_news):
    index_news = int(index_news)
    if index_news >= len(news_list):
        a = 1212 / 0
        return "<h1>такої новини немає у списку</h1>", 404
    news = news_list[index_news]
    return render_template("news_post.html", news=news)


@news_route.route("/form/create/", methods=['GET'])
def create_news():
    return """
<form method="post">
    <label>заголовок</label>
    <input name="name" type="text">
    <label>Опис</label>
    <input name="context" type="text">
    <label>Автор</label>
    <input name="author" type="text">
    <input type="submit">
</form>    
"""


@news_route.route("/form/create/", methods=['POST'])
def create_news_post():
    news = request.form.to_dict()
    news_list.append(news)
    return "на сайті новин" + str(len(news_list))
