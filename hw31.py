some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]


def select_numbers_that_more_500(item_in_list):
    if type(item_in_list) in [int, float]:
        if item_in_list > 500:
            return True
    else:
        return False


result = filter(select_numbers_that_more_500, some_data)
print(list(result))
