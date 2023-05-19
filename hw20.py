def ukrainian_presidents():
    presidents = [
        ("Леонід", "Кравчук"),
        ("Леонід", "Кучма"),
        ("Віктор", "Ющенко"),
        ("Віктор", "Янукович"),
        ("Петро", "Порошенко"),
        ("Володимир", "Зеленський")
    ]
    for president in presidents:
        yield president


for president in ukrainian_presidents():
    print(president)
