# 1. Арифметический оператор +
print(10 + 5)   # 1. 15

sum1 = 100 + 50      # 2. 150 (100 + 50)
sum2 = sum1 + 250    # 3. 400 (150 + 250)
sum3 = sum2 + sum2   # 4. 800 (400 + 400)

print(sum1)
print(sum2)
print(sum3)

# 2. Логические операторы and / or / not
x = 5
print(x > 0 and x < 10)   
x = 5
print(x < 5 or x > 10)    
x = 5
print(not(x > 3 and x < 10))  

# 3. Операторы идентичности is / is not

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # 8. True, одна ссылка на объект
print(x is y)   # 9. False, разные объекты
print(x == y)   # 10. True, значения равны

print(x is not y)  # 11. True, объекты разные

# 4. Разница между is и ==

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # 12. True, значения равны
print(x is y)   # 13. False, разные объекты

# 5. Операторы принадлежности in / not in

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)    # 14. True
print("pineapple" not in fruits)   # 15. True


# 6. Побитовые операторы

print(6 & 3)   # 19. 2 (бит AND)
print(6 | 3)   # 20. 7 (бит OR)
print(6 ^ 3)   # 21. 5 (бит XOR)

