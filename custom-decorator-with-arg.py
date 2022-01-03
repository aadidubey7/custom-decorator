def meta_decorator(arg):
    def decorator_list(func):
        def inner(list_of_tuples):
            return [func(value[0], value[1]) ** power for value in list_of_tuples]

        return inner

    
    if callable(arg):
        power = 1
        return decorator_list(arg)
    else:
        power = arg
        return decorator_list


@meta_decorator(2)
def add_element(a, b):
    return a + b

n = [(1, 2), (3, 4), (5, 6)]
print(add_element(n))