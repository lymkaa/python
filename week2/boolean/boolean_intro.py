# 1 пример с True / False statement
print(10 > 9)     # True, потому что 10 больше 9
print(10 == 9)    # False, потому что 10 не равно 9
print(10 < 9)     # False, потому что 10 не меньше 9


# 2 тот же True / False, но вместе с условием if-else
a = 200
b = 33

if b > a:
    print("b is greater than a")   # выполнится, если условие True
else:
    print("b is not greater than a")  # выполнится, если условие False


# 3 Оценка значений через bool()
print(bool("Hello"))   # True, строка не пустая
print(bool(15))        # True, число не равно 0


# 4 Значения, которые возвращают False
print(bool(False))     # False
print(bool(None))      # False
print(bool(0))         # False


# 5 Print "YES!" if the function returns True, otherwise print "NO!"
"""
Функция с использованием Boolean.
Внутри функции используется return True — это значит,
что функция возвращает логическое значение True.
Далее в if проверяется результат работы функции.
Если True — выводится "YES!", иначе — "NO!".
"""
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")
