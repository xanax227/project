n = int(input("Введіть натуральне число n: "))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10

print(count)