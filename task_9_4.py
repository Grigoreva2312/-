# Задача 9. Вариант 4.
#Григорьева Я.В.
#1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
#Вслед за тем игрок должен попробовать отгадать слово.
# 18.04.2017

import random
word = ("помощник","меч","память","цветы","вознаграждение","солнце","вера")
varik=""
comp=random.choice(word)
 
quantity=5
attempt=1 
print('у вас 5 попыток отгадать слово')
print("Угадайте заданное слово из ниже перечисленных")
print (word)

while varik != comp and quantity > 0:
    if quantity == 5 :  
        if (input("Нужна ли Вам подсказка?")) == "да" :
            print("Длина заданного слова = :",len(comp))
    else :
        if quantity <5:
            if (input("Нужна ли Вам ещё подсказка?")) == "да" :
                symbol=input(" Спросите у компьютера любую букву из алфавита, а он ответит, есть ли в слове эта буква: ")
                if symbol in comp :
                    print("Вы угадали!Эта буква присутствует в слове")
                else :
                    print ("Вы не угадали!Буква отсутвует")
    quantity=quantity-1				
 
    varik=input("Попробуйте отгадать слово :")
	
    print("Попытка :",attempt)
    attempt=attempt+1
	
   
if varik==comp :
    print("Да,именно так!Вы отгадали!")
else :
    print('К сожалению,вы не угадали!!! Правильный ответ: ', comp )
     
input ('Нажмите Enter для выхода')
