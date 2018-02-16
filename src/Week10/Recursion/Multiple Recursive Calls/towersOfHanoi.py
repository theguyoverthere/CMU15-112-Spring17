#  A
#  B                      A
#  C                      B
#  D          D           C
# ===        ===         ===
#  x          y           z
# ===        ===         ===
# from        to         via
#
# move(n - 1 disks, x, z, y)
# move(    1 disk,  x, y, z)
# move(n - 1 disk,  z, y, x)


def move(n, frm, to, via):
    if n == 1:
        print((frm, to), end=" ")
    else:
        move(n - 1, frm, via, to)
        move(1, frm, to, via)
        move(n - 1, via, to, frm)

def hanoi(n):
    print("Solving Tower of Hanoi with n =", n)
    move(n, 0, 1, 2)
    print()

