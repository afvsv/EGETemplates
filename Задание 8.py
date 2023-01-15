'''
Борис составляет 6-буквенные коды из букв Б, О, Р, И, С.
Буквы Б и Р нужно обязательно использовать ровно по одному разу,
букву С можно использовать один раз или не использовать совсем,
буквы О и И можно использовать произвольное количество раз или не использовать совсем.
Сколько различных кодов может составить Борис?
Ответ: 1440
'''

import itertools
# itertools - библиотека для работы с комбинаторикой
# product() - функция, получающая все возможные перестановки элементов длины repeat из букв, которые в неё переданы
listString = itertools.product('БОРИС', repeat=6)
count = 0
for str in listString:
    # join() - функция соединяющая массив строк в одну строку при помощи разделителя, который указан до точки
    line = ''.join(str)
    # count() - строковая функция, которая определяет кол-во вхождений букв или слов в строку
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)
