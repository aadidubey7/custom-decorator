def custom_decorator(func):
    def inner(list_of_tuples):
        return [func(val[0], val[1]) for val in list_of_tuples]

    return inner

@custom_decorator
def add_element(a, b):
    return a + b

n = [(1, 2), (3, 4), (5, 6)]
print(add_element(n))