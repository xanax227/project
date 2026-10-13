n = int(input())

a, b = 1, 1
res = []

while a <= n:
    res.append(str(a))
    a, b = b, a + b

print(" ".join(res))