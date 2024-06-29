number = int(input("Enter a number to see its multiplication table:"))
X = number
for num in range (1,11):
    Y = num
    Z = Y * X
    print(f"{X} * {Y} = {Z}")