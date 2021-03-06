def power(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return power(base, exp // 2) ** 2
    else:
        return base * power(base, exp // 2) ** 2

print(power(2, 0))
print(power(2, 1))
print(power(2, 2))
print(power(2, 3))
print(power(2, 4))