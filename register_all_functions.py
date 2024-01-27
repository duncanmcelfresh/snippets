all_funcs = []


def register_func(func):
    """decorator to store the name of all functions with decorator"""
    all_funcs.append(func.__name__)
    return func


@register_func
def square(x):
    print(f"red {x*x}")


@register_func
def two(x):
    print(f"red {2*x}")


@register_func
def banana(x):
    print(f"banana! ({x})")


if __name__ == "__main__":
    print(f"all registered functions: {all_funcs}")

    # output:
    # all registered functions: ['square', 'two', 'banana']
