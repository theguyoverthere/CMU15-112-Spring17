def lockerProblem(lockers):
    isOpen = [False] * (lockers + 1)
    students = lockers

    for students in range(1, students + 1):
        for locker in range(students, lockers + 1, students):
            isOpen[locker] = not isOpen[locker]

    openLockers = [ ]

    for locker in range(1, lockers + 1):
        if isOpen[locker]:
            openLockers.append(locker)

    return openLockers

print(lockerProblem(20000))
