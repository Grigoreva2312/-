﻿# Задача 6. Вариант 4.
#Создайте игру, в которой компьютер загадывает название одного из двенадцати подвигов Геракла, а игрок должен его угадать.

# Григорьева Я.В.
# 18.04.17

import random
feats = ["Немецкий лев","Критский бык","Лернейская гидра",
"Кони Диомеда","Керинейская лань","Геракл у Адмета","Стимфалийские птицы","Рождение и Юность Геракла",
"Похищение Цербера","Коровы Гериона",
"Золотые яблоки Гесперид","Пояс Ипполиты."]
Vvodfeats = input("Назовите один из подвигов Геракла: ")
y = random.choice(feats)
if y == "Vvodfeats":
    print("Вы угадали! \nПравильный ответ:", y)
else:
    print("Вы не угадали! \nПравильный ответ:", y)
    input("Нажмите Enter для выхода ")
    
