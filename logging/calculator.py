import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('calculator.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add( x, y):
    """adding x to y"""
    return x + y

def sub( x, y):
    """subtracting y from y"""
    return x - y

def multi( x, y):
    """multiply x and y"""
    return x*y

def div( x, y):
    """dividing x to y"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Trying to divide by zero')
    else:
        return result

number_1 = 100
number_2 = 3



add_result = add(number_1, number_2)
logger.debug('Add: {} + {} = {}'.format(number_1, number_2, add_result))

sub_result = sub(number_1, number_2)
logger.debug('Sub: {} - {} = {}'.format(number_1, number_2, sub_result ))

multi_result = multi(number_1, number_2)
logger.debug('Multi: {} * {} = {}'.format(number_1, number_2, multi_result))

div_result = div(number_1, number_2)
logger.debug('Div: {} / {} = {}'.format(number_1, number_2, div_result))