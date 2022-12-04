# Homework 8 (12.11.2022)

# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".
week = {
     1: 'Monday',
     2: 'Thuesday',
     3: 'Wednesday',
     4: 'Thursday',
     5: 'Friday',
     6: 'Saturday',
     7: 'Sunday',
}
num_of_day = int(input('number of the day?'))
print(week.get(num_of_day, 'error'))


# 2. Опишіть кота (домашня тварина) на основі словника.

kitten = {
    'name': 'Taras',
    'surname': 'Pan Kotsky',
    'body_type': {
        'fur': 'fluffy',
        'length': 'short',
        'weight': 'fatty'
    },
    'mood': 'very kind, never sad',
    'parents': 'yurgendev and vika'
}
cat = input('cat info?')
print(kitten.get(cat))


# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
# скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.

text = input('text here: ')
res = {}

for i in set(text):
    res[i] = text.count(i)
    print(i, text.count(i))

# 4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку. Наприклад, для рядків «Hello»
# та «World» на екрані мають бути літери «l» та «o».


text1 = input('text1: ')
text2 = input('text2: ')
print(set(text1) & set(text2))

# 5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.

list1 = list(range(3, 27, 3))
list2 = list(range(5, 27, 5))
print(list1, list2)

# 6. Створіть список із числами, які є в обох списках.

list3 = list(range(1, 10))
list4 = list(range(1, 12))
print(list3)
print(list4)
print(set(list3) & set(list4))