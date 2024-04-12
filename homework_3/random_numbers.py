import random

numbers = []
i = 0

while i<=20:
    random_number = random.randint(10,90)
    if random_number not in numbers:
        numbers.append(random_number)
        i +=1
print(numbers)