
# 1. Пример с True / False statement
print(10 > 9)     
print(10 == 9)   
print(10 < 9)     

# 2. Тот же True / False, но вместе с условием if-else
a = 200
b = 33
if b > a:
    print("b is greater than a")   
else:
    print("b is not greater than a") 

# 3. Оценка значений через bool()
print(bool("Hello"))   
print(bool(15))        

# 4. Значения, которые возвращают False
print(bool(False))   
print(bool(None))     
print(bool(0))         

# 5. Print "YES!" if the function returns True, иначе "NO!"
def myFunction():
    return True
if myFunction():
    print("YES!")     
else:
    print("NO!")

