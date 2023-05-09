def changing_the_result_to_str(func):
    def wrapper(*args, **kwargs):

        result = str(func(*args, **kwargs))
        return result
    return wrapper


@changing_the_result_to_str
def main_func(first_value, second_value):
    main_func_result = first_value + second_value * 2
    return main_func_result


print(main_func(5, 6))
