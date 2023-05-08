# n = print
# n('g')
# print(id(print))
# print(id(55555555))
#
#
# def my_function(value: str) -> str:
#     return value * 2 + 'fff'
#
#
# def decorator(func):
#     return func
#
#
# func = decorator(my_function)('hhh')
# print(func)


def only_int(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return int(result)

    return wrapper


@only_int
def calc_sphere_volume(radius: int):
    return (4 / 3) * 3.1416 * (radius ** 3)


@only_int
def mult_to_to(length: int | float):
    return length * 2


print(calc_sphere_volume(5))
print(mult_to_to(5))
