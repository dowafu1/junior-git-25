#Задача 1
from os.path import split

input_number: int = int(input("Введите число: "))

if input_number % 3 == 0 and input_number % 5 == 0:
    print("Fizz Buzz")
elif input_number % 3 == 0:
    print("Fizz")
elif input_number % 5 == 0:
    print("Buzz")
else:
     print(input_number)

#Задача 2

input_number_1: int = int(input("\nВведите число: "))
number_even: int = input_number_1 % 2

if number_even != 0:
    print("Плохо")
elif 2 <= input_number_1 <= 5 and number_even == 0:
    print("Неплохо")
elif 6 <= input_number_1 <= 20 and number_even == 0:
    print("Так себе")
elif input_number_1 > 20 and number_even == 0:
    print("Отлично")

#Задача 3

input_value: int = int(input("\nДлина последовательности: "))
end_num: str = ""

for i in range(1, input_value + 1):
    end_num += str(i)
print(end_num)

#Задача 4

input_str: str = input("\nВведите текст: ")
end_str: str = ""

for n in input_str:
    if n.isupper():
        end_str += n
print(end_str)

#Задача 5

input_str_1: str = input("\nВведите текст: ")
bill: int = 0

for b in input_str_1.split():
    if b.isdigit() is False:
        bill += 1
        if bill >= 3:
            print(True)
            break
        else:
            continue
    else:
        bill = 0

if bill < 3:
    print(False)

#Задача 6


