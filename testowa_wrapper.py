import datetime


def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('Changing salary for {} to {} as bonus = {}'.format(emp_name, new_salary, is_bonus))
    return new_salary

print(ChangeSalary("Jan", 2500, True))

def CreateFunctionWithWrapper (func):
    def func_with_wrapper(*args, **kwargs):
        print("Ta funkcja wystartowała o {}".format(datetime.datetime.now().isoformat()))
        print("%" * 10)
        result = func(*args, **kwargs)
        print("Ta funkcja zakończyła się o {}".format(datetime.datetime.now().isoformat()))
        return result
    return func_with_wrapper

ChangeSalaryWithLog = CreateFunctionWithWrapper(ChangeSalary)
print(ChangeSalaryWithLog("Jan", 2500, True))