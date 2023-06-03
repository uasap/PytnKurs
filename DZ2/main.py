'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''

n = int(input('Введите число монеток: '))
from random import randint

list_coins = []
for i in range(n):
    list_coins.append(randint(0, 1))
print(list_coins)
zero = list_coins.count(0)
if len(list_coins) - zero < zero:
    print(f'Нужно перевернуть {len(list_coins) - zero} монеток')
else:
    print(f'Нужно перевернуть {zero} монеток')
    
'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает
                                            две подсказки. Он называет сумму этих чисел S и их произведение P. 
                                            Помогите Кате отгадать задуманные Петей числа.
                                            '''
s = int(input('Введите сумму числа: '))
p = int(input('Введите произведение: '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(x, y)

if a == 0:
    print('Вы ввели не корректные данные!')

'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

n = int(input('Введите число N: '))
k = 0
res = 1
while res < n+1:
    print(res, end=' ')
    k += 1
    res = 2 ** k