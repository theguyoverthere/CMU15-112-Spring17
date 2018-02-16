def power(base, exp):
    # Base Case
    if exp == 0:
        return 1

    #Recursive Case
    if exp < 0:
        return 1 / (base * power(base, abs(exp) - 1))
    else:
        return base * power(base, exp - 1)

print(power(2, -5)) # 32
print(power(2, 5)) # 32