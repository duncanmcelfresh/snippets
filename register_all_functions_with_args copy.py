all_funcs_by_tag = {
    "red": [],
    "blue": [],
    "green": [],
}


def register_func(tag):
    """decorator to store the name of all functions in a dict entry corresponding to their tag"""

    def decorator(func):
        all_funcs_by_tag[tag].append(func.__name__)
        return func

    return decorator


@register_func("red")
def square(x):
    print(f"red {x*x}")


@register_func("red")
def two(x):
    print(f"red {2*x}")


@register_func("blue")
def banana(x):
    print(f"banana! ({x})")


if __name__ == "__main__":
    print(f"all registered functions: {all_funcs_by_tag}")

    # output:
    # all registered functions by tag: {'red': ['square', 'two'], 'blue': ['banana'], 'green': []}
