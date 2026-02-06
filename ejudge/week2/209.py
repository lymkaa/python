n = int(input())
nm=list(map(int, input().split()))
maxx=nm[0]
minn=nm[0]
for i in range (n):
    if (maxx<nm[i]):
        maxx=nm[i]
    if (minn>nm[i]):
        minn=nm[i]
for i in range (n):
    if(nm[i]==maxx):
        nm[i]=minn
print(*nm)