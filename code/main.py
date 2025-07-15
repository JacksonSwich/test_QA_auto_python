import requests

def get_json_response():
    """Получаем ответ от сервера в виде json файла"""
    response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
    print(f"Ответ сервера - {response}")
    return response.json()


def main(person_gender, is_working):
    """Главная функция вывода результата поиска"""
    file = get_json_response()

    highest_height = 0

    if person_gender == "Male" and is_working == True: # мужчина - работает
        for row in range(0, len(file)):
            if file[row]['appearance']['gender']  == 'Male' and file[row]['work']['occupation'] != '-':

                height = file[row]['appearance']['height'][1]

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

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕго рост = {highest_height}")
        return highest_height, highest_height

    elif person_gender == "Male" and is_working == False: # мужчина - не работает
        for row in range(0, len(file)):
            if file[row]['appearance']['gender'] == 'Male' and file[row]['work']['occupation'] == '-':

                height = file[row]['appearance']['height'][1]

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

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕго рост = {highest_height}")
        return highest_height, highest_height

    elif person_gender == "Female" and is_working == True: # женщина - работает
        for row in range(0, len(file)):
            if file[row]['appearance']['gender'] == 'Female' and file[row]['work']['occupation'] != '-':

                height = file[row]['appearance']['height'][1]

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

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕе рост = {highest_height}")
        return highest_height, highest_height

    elif person_gender == "Female" and is_working == False: # женщина - не работает
        for row in range(0, len(file)):
            if file[row]['appearance']['gender'] == 'Female' and file[row]['work']['occupation'] == '-':

                height = file[row]['appearance']['height'][1]

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

        print(f"\nЭто самый большой персонаж: {highest_hero} \nЕе рост = {highest_height}")
        return highest_height, highest_height

    else:
        print("ERROR")


# глобальная программа
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

main(gender, work)