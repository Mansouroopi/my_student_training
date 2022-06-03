class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


class my_timer(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs) :
        import time
        t1 = time.time();
        result = self.original_function(*args, **kwargs)
        t2 = time.time()
        print("spend {} seconds".format(t2-t1))
        return result

class MyLogger(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        import logging
        logging.basicConfig(filename='{}.log'.format(self.original_function.__name__), level=logging.INFO)
        logging.info('call with args {} and kwargs {}'.format(args, kwargs))
        return self.original_function(*args, **kwargs)



def my_func_timer(func):
    import time
    def wrapper(*a, **b):
        t1 = time.time();
        result =  func(*a, **b)
        t2 = time.time()
        print('spend {} s'.format(t2-t1))
        return result
    return wrapper

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info('Run with args {} and kwargs {}'.format(args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper

def decorate_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('called before {} '.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorate_function
def display():
    print('display info')

# @decorator_class
# @my_timer
@my_func_timer
@MyLogger
def display_info(name, age):
    print("My name is {} and i am {} old".format(name,age))

display_info('mansour', 34)