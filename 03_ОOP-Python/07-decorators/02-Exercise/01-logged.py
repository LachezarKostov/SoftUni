def logged(func):
    def wrapper(*args):
        res = func(*args)
        args = [str(x) for x in args]
        return \
            f"""you called {func.__name__}({", ".join(args)})
it returned {res}"""
    return wrapper



@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
