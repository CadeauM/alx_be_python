size = int(input("Enter the size of the pattern: "))
n = 0
while n < size:
    for i in range(size):
        print("*", end="")
    print()
    n += 1