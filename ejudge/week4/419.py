import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

d1 = math.hypot(x1, y1)
d2 = math.hypot(x2, y2)
d = math.hypot(x2 - x1, y2 - y1)

# check if direct path intersects circle
area = abs(x1*y2 - x2*y1)
h = area / d

if h >= R:
    print("{:.10f}".format(d))
else:
    theta = math.acos((x1*x2 + y1*y2) / (d1*d2))
    alpha1 = math.acos(R/d1)
    alpha2 = math.acos(R/d2)
    arc = R * (theta - alpha1 - alpha2)
    length = math.sqrt(d1*d1 - R*R) + math.sqrt(d2*d2 - R*R) + arc
    print("{:.10f}".format(length))