n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

used = []
for s in strings:
    if s not in used:
        used.append(s)

used.sort()

for s in used:
    print(s, strings.index(s) + 1)
