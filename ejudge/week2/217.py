n = int(input())
freq = {}
    
for x in range(n):
    x = input()
    freq[x] = freq.get(x, 0) + 1

c = freq.values()    
th = 0
for f in c:
    if f == 3:
        th += 1    
print(th)


