n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    while n >= 1:
        print(n)
        n -= 1
    print("Blast off!")
