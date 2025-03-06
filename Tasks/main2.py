#Задача 1

from random import  randint

number1 = randint(0, 100)
number2 = randint(0, 100)
number3 = randint(0, 100)
number_avg = (number1 + number2 + number3) / 3

print(f"Число 1 - {number1} \nЧисло 2 - {number2} \nЧисло 3 - {number3}")
print(f"Среднее значение чисел: \n({number1} + {number2} + {number3}) / 3 = {number_avg:.3}")

#Задача 2

number_1 = randint(0, 100)
number_2 = randint(1, 100) #На ноль делить нельзя

print(f"\nЧисло один - {number_1} \nЧисло два - {number_2}") #В переди написал n чтобы визуально разделить задачи
print("Частное от деления -", number_1 // number_2, "\nОстаток от деления -", number_1 % number_2)

#Задача 3

number_float = 23.723

print(f"\n1. {number_float:.4} \n2.", round(number_float), f"\n3. {number_float:=011}")

#Задача 4

input_value: str = input("\nВведите число: ")
value: int = int(input_value)
reversed_value: str = str(abs(value))[::-1]

if value < 0:
    reversed_value = '-' + reversed_value

print(f"Инвертированное число: {int(reversed_value)}")

#Задача 5

input_value_1: str = input("\nВведите число: ")
value_1: int = int(input_value_1)
reversed_value_1: str = str(abs(value_1))[::-1]

if value_1 < 0:
    reversed_value_1 = '-' + reversed_value_1
if int(reversed_value_1).bit_length() > 32 or int(reversed_value_1).bit_length() < -32:
    reversed_value_1 = "0"

print(f"Инвертированное число: {reversed_value_1}")