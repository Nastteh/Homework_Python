'''
Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
*Пример:
10 -> 1 2 4 8
степень 0 1 2 3 результат не больше 10
'''

n = int(input('Введите целое число больше 1: '))
i=0
while 2 ** i<=n:
    print(2 ** i)
    i += i