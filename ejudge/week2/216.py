n=int(input())
arr=list(map(int, input().split()))
se=set()
for x in arr:
    if x in se:
        print("NO")
    else:
        print("YES")
        se.add(x)