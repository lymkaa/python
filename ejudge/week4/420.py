g = 0

def outer(commands):
    n = 0

    def inner():
        nonlocal n
        global g
        for scope, value in commands:
            value = int(value)
            if scope == "global":
                g += value
            elif scope == "nonlocal":
                n += value
            else:
                x = value  # local change only
        return n

    return inner()

m = int(input())
commands = [input().split() for _ in range(m)]

n = outer(commands)
print(g, n)