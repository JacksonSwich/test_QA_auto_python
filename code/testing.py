import pytest
from unittest.mock import patch

from main import find_hero, main

# создал тестовые данные, которые будут передаваться в функцию, для заполнения фикстуры
test_json_data = [
    { # мужчина - работает
        "id": 1,
        "name": "person 1",
        "appearance":
        {
            "gender": "Male",
            "race": "Human",
            "height": ["6'8", "20 cm"]
        },
        "work":
        {
            "occupation": "author",
            "base": "-"
        }
    },

    { # мужчина - не работает
        "id": 2,
        "name": "person 2",
        "appearance":
        {
            "gender": "Male",
            "race": "Human",
            "height": ["6'8", "2.5 meters"]
        },
        "work":
        {
            "occupation": "-",
            "base": "-"
        }
    },

    { # женщина - работает
        "id": 3,
        "name": "person 3",
        "appearance":
        {
            "gender": "Female",
            "race": "Human",
            "height": ["6'8", "431 cm"]
        },
        "work":
        {
            "occupation": "Musician",
            "base": "-"
        }
    },

    { # мужчина - работает
        "id": 4,
        "name": "person 4",
        "appearance":
        {
            "gender": "Male",
            "race": "Human",
            "height": ["6'9", "123 cm"]
        },
        "work":
        {
            "occupation": "adventurer",
            "base": "-"
        }
    },

    { # женщина - не работает
        "id": 5,
        "name": "person 5",
        "appearance":
        {
            "gender": "Female",
            "race": "Human",
            "height": ["6'8", "203 cm"]
        },
        "work":
        {
            "occupation": "-",
            "base": "-"
        }
    }
]


# фикстура, которая создается один раз для всей тестовой сессии
@pytest.fixture(scope="session")
def get_json_data():
    json_data = test_json_data
    return json_data

# ОСНОВНОЕ тестирование функции по поиску самого высокого персонажа
def test_find_hero(get_json_data):
    assert find_hero(get_json_data, "Male", True) == ('ID: 4; NAME: person 4; APPEARANCE: gender: Male; WORK: adventurer; height: 123 cm;', 123)
    assert find_hero(get_json_data, "Male", False) == ('ID: 2; NAME: person 2; APPEARANCE: gender: Male; WORK: -; height: 2.5 meters;', 250)
    assert find_hero(get_json_data, "Female", True) == ('ID: 3; NAME: person 3; APPEARANCE: gender: Female; WORK: Musician; height: 431 cm;', 431)
    assert find_hero(get_json_data, "Female", False) == ('ID: 5; NAME: person 5; APPEARANCE: gender: Female; WORK: -; height: 203 cm;', 203)


# ПОБОЧНОЕ тестирование функций ввода входных данных
def test_man_yes(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["мужской", "да"]) # входные данные для input()
    main()
    output = capsys.readouterr() # записываем весь вывод программы
    assert "Ошибка! Неверное значение переменной gender" not in output.out # если сообщения об ошибки нет - тест прошел
    assert "Ошибка! Неверное значение переменной work" not in output.out

def test_man_no(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["мужской", "нет"])
    main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной gender" not in output.out
    assert "Ошибка! Неверное значение переменной work" not in output.out

def test_woman_yes(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["женский", "да"])
    main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной gender" not in output.out
    assert "Ошибка! Неверное значение переменной work" not in output.out

def test_woman_no(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["женский", "нет"])
    main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной gender" not in output.out
    assert "Ошибка! Неверное значение переменной work" not in output.out

def test_register_negative_script(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["МуЖСКОй", "ДА"])
    main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной gender" not in output.out
    assert "Ошибка! Неверное значение переменной work" not in output.out

def test_register_negative_script_2(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["женСКИЙ", "нЕТ"])
    main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной gender" not in output.out
    assert "Ошибка! Неверное значение переменной work" not in output.out

def test_data_negative_script(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["asdasfasf", "да"])
    with pytest.raises(SystemExit): # ловим выход программы, чтобы тест продолжился
        main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной gender" in output.out

def test_data_negative_script_2(capsys, mocker):
    mocker.patch("builtins.input", side_effect=["мужской", "2322186493"])
    with pytest.raises(SystemExit):
        main()
    output = capsys.readouterr()
    assert "Ошибка! Неверное значение переменной work" in output.out

