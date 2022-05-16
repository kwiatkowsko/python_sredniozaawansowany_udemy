def factors(value):
    result = []
    jojo = 2
    if value == 1:
        pass
    while value > 1:
        if jojo >= value:
            result += [jojo]
            break
        if value % jojo == 0:
            result += [jojo]
            value = value / jojo
        elif value % jojo != 0:
            jojo += 1
    return result


print(factors(625))
print(factors(1))
print(factors(25))
print(factors(34573276))