
def move(n, source, target, spare, depth=0):
    print(" " * 3 * depth, "move " + str(n), "from", source, "to", target, "via", spare)

    if n == 1:
        print((" " * 3 * depth), (source, target))
    else:
        move(n - 1, source, spare, target, depth + 1)
        move(1, source, target, spare, depth + 1)
        move(n - 1, spare, target, source, depth + 1)

def towerOfHanoi(n):
    print("Solving Tower of Hanoi with n =", n)
    move(n, 0, 1, 2)
    print()


towerOfHanoi(4)
