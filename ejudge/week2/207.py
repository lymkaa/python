n = int(input())
nm=list(map(int, input().split()))
s=nm[0]
x=0
for i in range (len(nm)):
    if(s<nm[i]):
        s=nm[i]
        x=i
print(x+1)