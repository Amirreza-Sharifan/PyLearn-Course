def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    print_pascal_triangle(triangle)
def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))
n = int(input("Enter the number of rows for Pascal's Triangle: "))
generate_pascal_triangle(n)