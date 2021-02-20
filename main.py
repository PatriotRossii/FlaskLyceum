from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route("/index")
def mission_credo():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return "</br>".join(["Человечество вырастает из детства.\n",
                         "Человечеству мала одна планета.\n",
                         "Мы сделаем обитаемыми безжизненные пока планеты.\n",
                         "И начнем с Марса!\n",
                         "Присоединяйся!\n"])


@app.route("/image_mars")
def image_of_mars():
    return "\n".join(["<html>", "<head>", "<title>Привет, Марс!</title>", "</head>",
                      "<body>", "<h1>Жди нас, Марс!</h1>",
                      f"<image src={url_for('static', filename='img/mars.jpg')}/></br>",
                      "Вот она какая, красная планета.",
                      "</body>", "</html>"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
