n = int(input())
num = list(map(int, input().split()))
sm=0
for i in range(n):
    sm+=num[i]
print(sm)