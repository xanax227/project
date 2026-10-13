t = int(input())

cells = 1

for _ in range(t // 3):
    cells *= 2

print(cells)