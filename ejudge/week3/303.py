s = input().strip()

to_digit = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}

to_word = {}

for k, v in to_digit.items():
    to_word[v] = k


op = None
for ch in "+-*":
    if ch in s:
        op = ch
        break

left, right = s.split(op)

def parse_num(part):
    digits = ""
    for i in range(0, len(part), 3):
        triplet = part[i:i+3]
        digits += to_digit[triplet]
    return int(digits)

a = parse_num(left)
b = parse_num(right)

if op == "+":
    res = a + b
elif op == "-":
    res = a - b
else:
    res = a * b

def encode_num(num):
    if num == 0:
        return "ZER"
    
    sign = ""
    if num < 0:
        sign = "-"
        num = abs(num)

    digits = str(num)
    out = ""
    for d in digits:
        out += to_word[d]
    return sign + out

print(encode_num(res))
