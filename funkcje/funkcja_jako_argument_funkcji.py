def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

def generate_values(fun_kcj_, x_table):
    talista = []
    for x in x_table:
        talista.append(fun_kcj_(x))
    return talista

x_table = list(range(16))
print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))