def num_change(value):
    arr = [(0, ' ₽'), (3, ' тыс. ₽'), (6, ' млн. ₽'), (9, ' млрд. ₽')]
    for n, s in arr[::-1]:
        n = 10**n
        if abs(value) >= n:
            return str(round(value / n)) + s
    return str(value)

def num_print(num_from, num_befor):
    if num_befor == '':
        num_from = int(num_from)
        return f'от {num_change(num_from)}'
    elif num_from == '':
        num_befor = int(num_befor)
        return f'до {num_change(num_befor)}'
    else:
        num_from = int(num_from)
        num_befor = int(num_befor)
        return f'{num_change(num_from)} - {num_change(num_befor)}'

def test_answer():
    assert num_print(20, 30) == '20 ₽ - 30 ₽'

    assert num_print(20, 300000) == '20 ₽ - 300 тыс. ₽'

    assert num_print(2001, '') == 'от 2 тыс. ₽'

    assert num_print('', 100500) == 'до 100 тыс. ₽'

    assert num_print('', 10050000) == 'до 10 млн. ₽'