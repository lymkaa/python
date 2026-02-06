n = int(input())
arr = list(map(int, input().split()))

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
maxx = max(freq.values())


cand = [num for num, count in freq.items() if count == maxx]


print(min(cand))