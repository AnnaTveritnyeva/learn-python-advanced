import functools


def add_stars(fun):
    stars = "********************"

    @functools.wraps(fun)
    def wrap(*args, **kvargs):
        print(stars)
        fun(*args, **kvargs)
        print(stars)

    return wrap


@add_stars
def hello():
    print("Hello!!")


hello()
