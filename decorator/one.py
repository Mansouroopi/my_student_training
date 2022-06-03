import functools
import time
# Decorator that takes and print the name of a func.
def decorator_showname(myfunc):
    @functools.wraps(myfunc)
    def wrapper_func(*args, **kwargs):
        print("I am going to execute: ", myfunc.__name__)
        return myfunc(*args, **kwargs)
    return wrapper_func


def time_taken(func):

    def wrap_func(*arg, **kwargs):
        t1 = time.time()
        r = func(*arg, **kwargs)
        t2 = time.time()
        print('time taken {}'.format(t2-t1))
        return r
    return wrap_func

# Compute Hypotenuse
@time_taken
@decorator_showname
def hypotenuse(a, b):
    """Compute the hypotenuse"""
    time.sleep(5)
    return round(float((a*a) + (b*b))**0.5, 2)

print(hypotenuse(3,4))
