def powers(n):
    val = 1
    for _ in range(n + 1):
        yield val
        val *= 2

n = int(input())
print(*powers(n))