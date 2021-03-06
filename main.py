from flask import Flask, render_template
import os
import json

app = Flask(__name__)


@app.route("/")
def page_index():
    # Формируем список скилов
    list_skill = []
    for _ in list_candidates:
        list_skill += create_list_skill(_['skills'])
    # Делаем список скилов уникальным
    list_skill = list(set(list_skill))
    # Сортируем скилы  при передаче
    return render_template('index.html', candidates=list_candidates, list_skill=sorted(list_skill))


@app.route("/person/<int:person_id>/")
def candidate(person_id):
    person = list(filter(lambda item: item['id'] == person_id, list_candidates))
    return render_template('person.html', candidates=person)


@app.route("/skill/<x>/")
def skill(x):
    person = []
    for _ in list_candidates:
        list_skill = create_list_skill(_['skills'])
        if x in list_skill:
            person.append(_)
    return render_template('skill.html', candidates=person)


def create_list_skill(skill_str):
    """
    Функция получаюет строку элементов  разделенных запятыми и возвращаеи список в нижнем регистре и
    очищенные от пробелов элементы списка
    :param skill_str:
    :return: список list_skill
    """
    list_skill = skill_str.lower().split(',')
    list_skill = [x.strip() for x in list_skill]
    return list_skill


if __name__ == '__main__':
    # Загрузка json если файл найден
    if os.path.isfile('candidates.json'):
        with open('candidates.json', 'r', encoding='utf8') as json_file:
            list_candidates = json.load(json_file)
    else:
        print('Увы, но файл не найден!!!')
        quit()

    # Активация  режиам отладки  для  автоперезапуска сервера  при  изменении кода
    app.debug = True
    app.run(host="127.0.0.1", port=5000)
