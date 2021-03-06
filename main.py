import os

from flask import Flask, url_for
from flask import request

UPLOAD_FOLDER = "./static/upload"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <image src={url_for('static', filename='img/mars.jpg')}/></br>
                    Вот она какая, красная планета.
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href={url_for('static', filename='css/style.css')}>
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <image src={url_for('static', filename='img/mars.jpg')}/></br></br>
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <center><h1>Анекта претендента</br>на участие в миссии</h1></center>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name"></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="engineer-researcher" value="engineer-researcher">
                                          <label class="form-check-label" for="engineer-researcher">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="engineer-builder" value="engineer-builder">
                                          <label class="form-check-label" for="engineer-builder">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="meteorolog" value="meteorolog">
                                          <label class="form-check-label" for="meteorolog">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="life-engineer" value="life-engineer">
                                          <label class="form-check-label" for="life-engineer">
                                            Инженер по жизнеообеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="nuclear-engineer" value="nuclear-engineer">
                                          <label class="form-check-label" for="nuclear-engineer">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Доктор
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="exo-biologus" value="exo-biologus">
                                          <label class="form-check-label" for="exo-biologus">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="motivation">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_name(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-light" role="alert">
                        <b>Эта планета близка к Земле;</b>
                    </div>
                    <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-warning" role="alert">
                      На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Наконец, она просто красива!
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                        Составляет {rating}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    image = ""
    template = '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <center><h1>Загрузка фотографии</br>для участия в миссии</h1></center>
                            <div>
                                <form class="photo_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label></br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div></br>
                                    {image}
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    if request.method == 'GET':
        return template.format(url=url_for('static', filename='css/style.css'), image="")
    elif request.method == 'POST':
        file = request.files['file']
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        image = f"<img src='{url_for('static', filename='upload/' + file.filename)}'/>"
        return template.format(url=url_for('static', filename='css/style.css'), image=image)


@app.route('/carousel')
def landscapes():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                    <center><h1>Пейзажи Марса</h1></center>
                    <div id="myCarousel" class="carousel slide" data-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active" data-bs-interval="1000">
                          <img class="d-block w-100" src="{url_for('static', filename='img/landscapes/landscape_1.jpg')}" alt="First slide">
                        </div>
                        <div class="carousel-item" data-bs-interval="1000">
                          <img class="d-block w-100" src="{url_for('static', filename='img/landscapes/landscape_2.jpg')}" alt="Second slide">
                        </div>
                        <div class="carousel-item" data-bs-interval="1000">
                          <img class="d-block w-100" src="{url_for('static', filename='img/landscapes/landscape_3.png')}" alt="Third slide">
                        </div>
                        <div class="carousel-item" data-bs-interval="1000"
                          <img class="d-block w-100" src="{url_for('static', filename='img/landscapes/landscape_4.jpg')}" alt="Fourth slide">
                        </div>
                        <div class="carousel-item" data-bs-interval="1000">
                          <img class="d-block w-100" src="{url_for('static', filename='img/landscapes/landscape_5.jpg')}" alt="Fifth slide">
                        </div>
                      </div>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
