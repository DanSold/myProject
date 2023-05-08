def checking_for_correct_data(func):
    def wrapper(*args, **kwargs):
        data = list(args) + list(kwargs.values())
        control_list = []
        for item in data:
            if type(item) == str:
                control_list.append(item)
                if len(control_list) == len(data):
                    return func(*args, **kwargs)
        else:
            return 'Error: incorrect data'

    return wrapper


@checking_for_correct_data
def main_func(first_value, second_value) -> str:
    return first_value + second_value * 2


print(main_func(5, 6))
print(main_func('5', 6))
print(main_func('5', '6'))
