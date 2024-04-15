print("Welcome to the Carpet Generator, please input a number for generating your carpet")
while True:
    n = int(input("Your n must be a odd number, please inter your (n), or press (0) for exiting: "))
    if n != 0:
        def generate_carpet(n):
            if n % 2 == 0:
                return "n must be an odd number."
            
            carpet = []
            center = n // 2
            for i in range(n):
                row = []
                for j in range(n):
                    if max(abs(center - i), abs(center - j)) == center:
                        row.append("🟦")
                    else:
                        row.append("⬜️")
                carpet.append(''.join(row))
            
            return '\n'.join(carpet)

        print(generate_carpet(n))
    
    else:
        break