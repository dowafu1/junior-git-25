#Задача №1

elements: list = [1, 3, 5]
sum_item: int = 0
last_item: int = 0

for item in elements:
    if elements.index(item) % 2 == 0:
        sum_item += item
        last_item = elements[-1]
    else:
        continue
print(sum_item * last_item)

#Задача №2

def search_diff(value: list):
    if len(value) > 0:
        item_max = max(value)
        item_min = min(value)
        items_diff = item_max - item_min
        return round(items_diff, 3)
    else:
        return 0

elements: list = [5, -5]
print(search_diff(elements))

#Задача №3

elements = (-20, -5, 10, 15)
list_sort = sorted(elements, key=abs)
print(list_sort)

#Задача №4

elements = [1, 300, 2, 200, 1]
element_index = 0
num_mid = 0
elements.sort()

if len(elements) % 2 == 0:
    element_index = int(len(elements) / 2)
    num_mid = (elements[element_index] + elements[element_index - 1]) / 2
    print(round(num_mid, 3))
else:
    num_mid = int(len(elements) / 2)
    print(elements[num_mid])




