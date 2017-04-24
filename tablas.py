for n in range(1, 10, 3):
    print()
    for m in range(1, 11):
        mult1 = m * n
        mult2 = m * (n + 1)
        mult3 = m * (n + 2)
        print("%2d x %2d = %2d    %2d x %2d = %2d    %2d x %2d = %2d " % (n, m, mult1, n + 1, m, mult2, n + 2, m, mult3))

            


