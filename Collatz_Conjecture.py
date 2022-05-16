def steps(number):
    iteration = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number == 1:
        break
    while number > 1:
        if number % 2 == 0:
            number = number /2
            iteration += 1
            continue
        elif number % 2 == 1:
            number = number*3 + 1
            iteration += 1
    return iteration

print(steps(15))