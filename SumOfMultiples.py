def sum(num1, num2, limit):
    total = 0
    for i in range(1, limit):
        if i % num1 == 0 or i % num2 == 0:
            total += i
    return total


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
limit = int(input("Enter the limit: "))

result = sum(num1, num2, limit)
print(f"The sum of multiples of {num1} or {num2} up to {limit} is {result}.")
