num = int(input("Enter a number to be factorised:"))  # Take input and convert it to integer

for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
    if num % i == 0:  # Check if i divides num exactly
        print(f"{i} x {num // i}")  # Print factor pair
