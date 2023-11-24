def multiplication_table(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result = i * j
            print(f'{i} x {j} = {result}\t', end='')
        print()
multiplication_table(8, 8)