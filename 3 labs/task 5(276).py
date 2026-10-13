n = int(input())

i = 1
res = []

while len(res) < n:
    for _ in range(i):
        if len(res) < n:
            res.append(str(i))
    i += 1

print(" ".join(res))