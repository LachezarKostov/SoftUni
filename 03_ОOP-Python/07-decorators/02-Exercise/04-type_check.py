def type_check(types):
    def decorator(func):
        def wrapper(element):
            if not isinstance(element, types):
                return "Bad Type"
            return func(element)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2
print(times2(2))
print(times2("str"))
