#Задача 1

text: str = 'hello, word of word'
chars_popularity = {}
words_popularity = {}

for chars in text:
    if chars != ',' and chars != ' ':
        #Проверяем есть ли символ в ключах если да то к значению добавляем 1
        chars_popularity[chars] = chars_popularity.get(chars, 0) + 1
print(chars_popularity)

#split делит текст учитывая пробел
for words in text.split():
    #Удаляет обозначенный символ в строке в начале или в конце
    words = words.strip(',')
    words_popularity[words] = words_popularity.get(words, 0) + 1
print(words_popularity)

#Задача 2

num_input = int(input())
num_list = []
num_dic = {0: '0',
           1: 'I',
           2: 'II',
           3: 'III',
           4: 'IV',
           5: 'V',
           6: 'VI',
           7: 'VII',
           8: 'VIII',
           9: 'IX',
           10: 'X',
           20: 'XX',
           30: 'XXX',
           40: 'XL',
           50: 'L',
           60: 'LX',
           70: 'LXX',
           80: 'LXXX',
           90: 'XC',
           100: 'C',
           200: 'CC',
           300: 'CCC',
           400: 'CD',
           500: 'D',
           600: 'DC',
           700: 'DCC',
           800: 'DCCC',
           900: 'CM',
           1000: 'M',
           2000: 'MM',
           3000: 'MMM',
}

def num_search(value):
    if value in num_dic:
        return num_dic[value]

for num in str(num_input):
    num_list.append(int(num))

if num_input < 10:
    num_search(num_input)

elif num_input < 100:
    num_list[0] = num_list[0] *10
    print(num_search(num_list[0]), num_search(num_list[1]), sep='')

elif num_input < 1000:
    num_list[0] = num_list[0] * 100
    num_list[1] = num_list[1] * 10
    print(num_search(num_list[0]), num_search(num_list[1]), num_search(num_list[2]), sep='')

elif num_input < 4000:
    num_list[0] = num_list[0] * 1000
    num_list[1] = num_list[1] * 100
    num_list[2] = num_list[2] * 10
    print(num_search(num_list[0]), num_search(num_list[1]), num_search(num_list[2]), num_search(num_list[3]), sep='')

else:
    print('Слишком большое число')

#Задача 3

rates = {'Sberbank': 55.8, 'VTB24': 53.91}
course_list = []

def get_key(rates, value):
    for bank_name, course in rates.items():
        if course == value:
            return bank_name

for course in rates.values():
    course_list.append(course)
    course_list.sort()

print(get_key(rates, course_list[0]), '-->', course_list[0])

#Задача 4

book = {'Petr': '546810',
        'Katya': '241815',
}
book_copy = book.copy()

for name, key in book.items():
    book_copy[key] = name
    del book_copy[name]

print(book_copy)

#Задача 5

dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
result = {}

for date, rate in zip(dates, rates):
    result[date] = rate
print(result)

