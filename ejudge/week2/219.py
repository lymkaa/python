n = int(input())

d = {}

for _ in range(n):
    name, eps = input().split()
    eps = int(eps)
    
    if name in d:
        d[name] += eps
    else:
        d[name] = eps

for name in sorted(d):
    print(name, d[name])
