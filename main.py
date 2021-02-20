from flask import Flask

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
