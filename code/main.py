import requests

def get_json_response():
    """Получаем ответ от сервера в виде json файла"""
    response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка! Ответ сервера - {response}")


def find_hero(file, person_gender, is_working):
    """Главная функция вывода результата поиска"""
    #file = get_json_response() # получаем json файл

    highest_height = 0

    # мужчина - работает
    if person_gender == "Male" and is_working == True: # проверяем входные данные в функции
        for row in range(0, len(file)): # цикл перебирает всех персонажей из json файла
            if file[row]['appearance']['gender']  == 'Male' and file[row]['work']['occupation'] != '-': # проверяем значения в строке героя

                height = file[row]['appearance']['height'][1] # получаем рост

                # форматирование вывода переменной роста
                if height[-2:] == "cm":
                    height = height[:-3]
                    height = int(height)
                elif height[-6:] == "meters":
                    height = height[:-7]
                    height = float(height) * 100
                    height = int(height)
                else:
                    print("ERROR")

                # ищем самого высокого персонажа из группы
                if height > highest_height:
                    highest_height = height
                    highest_hero = f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};"

                # вывод всех подходящих из группы
                print(f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};")
            else:
                continue

        # результат
        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕго рост = {highest_height} см\n")
        return highest_hero, highest_height

    # мужчина - не работает
    elif person_gender == "Male" and is_working == False:
        for row in range(0, len(file)):
            if file[row]['appearance']['gender'] == 'Male' and file[row]['work']['occupation'] == '-':

                height = file[row]['appearance']['height'][1]

                # форматирование вывода переменной роста
                if height[-2:] == "cm":
                    height = height[:-3]
                    height = int(height)
                elif height[-6:] == "meters":
                    height = height[:-7]
                    height = float(height) * 100
                    height = int(height)
                else:
                    print("ERROR")

                if height > highest_height:
                    highest_height = height
                    highest_hero = f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};"

                print(f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};")
            else:
                continue

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕго рост = {highest_height} см\n")
        return highest_hero, highest_height

    # женщина - работает
    elif person_gender == "Female" and is_working == True:
        for row in range(0, len(file)):
            if file[row]['appearance']['gender'] == 'Female' and file[row]['work']['occupation'] != '-':

                height = file[row]['appearance']['height'][1]

                # форматирование вывода переменной роста
                if height[-2:] == "cm" or height[-2:] == "kg": # в записи с номером 198 "height": ["-", "0 kg"]
                    height = height[:-3]
                    height = int(height)
                elif height[-6:] == "meters":
                    height = height[:-7]
                    height = float(height) * 100
                    height = int(height)
                else:
                    print("ERROR")

                if height > highest_height:
                    highest_height = height
                    highest_hero = f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};"

                print(f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};")
            else:
                continue

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕе рост = {highest_height} см\n")
        return highest_hero, highest_height

    # женщина - не работает
    elif person_gender == "Female" and is_working == False:
        for row in range(0, len(file)):
            if file[row]['appearance']['gender'] == 'Female' and file[row]['work']['occupation'] == '-':

                height = file[row]['appearance']['height'][1]

                # форматирование вывода переменной роста
                if height[-2:] == "cm":
                    height = height[:-3]
                    height = int(height)
                elif height[-6:] == "meters":
                    height = height[:-7]
                    height = float(height) * 100
                    height = int(height)
                else:
                    print("ERROR")

                if height > highest_height:
                    highest_height = height
                    highest_hero = f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};"

                print(f"ID: {file[row]['id']}; NAME: {file[row]['name']}; APPEARANCE: gender: {file[row]['appearance']['gender']}; WORK: {file[row]['work']['occupation']}; height: {file[row]['appearance']['height'][1]};")
            else:
                continue

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕе рост = {highest_height} см\n")
        return highest_hero, highest_height

    else:
        print("ERROR")


# Функция main; Запрашиваем данные
def main():
    print("Введите входные данные для поиска:")

    gender = input("Введите пол (мужской/женский): ")
    if gender.lower() == "мужской":
        gender = "Male"
    elif gender.lower() == "женский":
        gender = "Female"
    else:
        print("Ошибка! Неверное значение переменной gender")
        exit()

    work = input("Наличие работы (да/нет): ")
    if work.lower() == "да":
        work = True
    elif work.lower() == "нет":
        work = False
    else:
        print("Ошибка! Неверное значение переменной work")
        exit()

    print(find_hero(get_json_response(), gender, work)) # вывод результата функции поиска персонажей


# Глобальная программа
if __name__ == '__main__':
    main()