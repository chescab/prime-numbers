# Produce a programme that displays the prime numbers between 1 and 100
# Prime number only has two factors, 1 and itself

# Variables created that takes input
# Converted string to integer
lower = int(input("Enter the minimum number: "))
upper = int(input("Enter the maximum number: "))

# Outer for loop to iterate from lower to upper values
# If condition to check if number is greater than 1
# If yes, inner for loop will run to check if each number is prime number
# Break statement to come out loop if not prime number and move to next number
# Else, print num if prime number, then check for next number
# Loop will finish until upper value is reached
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            print(num)


