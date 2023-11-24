def chessboard(n, m):
    for i in range(n):
        for j in range(m):
            print('*' if (i + j) % 2 == 1 else '#', end='')
        print()
chessboard(8, 16)