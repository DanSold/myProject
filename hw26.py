from secrets import token_urlsafe


def returning_products_maximum_allowable_price(incoming_products_list: list[dict],
                                               max_value: float | int) -> list[str]:
    result = []
    for item in incoming_products_list:
        if item['price'] <= max_value:
            result.append(item['product'])
    return result


def receives_number_and_generates_a_tape_of_this_length(number: int) -> str:
    add_txt = 'danKo'
    our_string = token_urlsafe(number)
    result_string = our_string + add_txt
    return result_string
