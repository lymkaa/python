def ev(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

first = True
for num in ev(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False