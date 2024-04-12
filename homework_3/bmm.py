num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
            gcd = i

print(gcd)

