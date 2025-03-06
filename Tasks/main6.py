#Задание 1

def non_unique_elements(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    result = [num for num in arr if count[num] > 1]
    return result

print(non_unique_elements([1, 2, 3, 1, 3]))

#Задание 2

from itertools import permutations

def valid_permutations(x, y, z, n):
    # Генерируем все перестановки
    perm = permutations([x, y, z])

    # Фильтруем перестановки по условию x + y - z > n
    result = [list(p) for p in perm if p[0] + p[1] - p[2] > n]

    return result

print(valid_permutations(1, 2, 4, 2))

#Задание 3

n = 5
result = [x*2 for x in range(0, n) if x%2 != 0]
print(result)
