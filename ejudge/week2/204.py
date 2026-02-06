n = int(input()) 
nm = list(map(int, input().split()))  
c = 0
for num in nm:
    if num > 0:
        c += 1
print(c)
