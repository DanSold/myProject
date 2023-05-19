def foo():
    yield 5


print(next(foo()))
print(foo())

some_data = foo()
print(some_data)
print(some_data)
