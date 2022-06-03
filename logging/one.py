import logging
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.INFO, file='sample.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5


kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}
logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))
logging.error("a={a} and b={b} cannot be negative".format(**kwargs))
logging.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))