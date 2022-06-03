import threading
import time
from asyncio.log import logger
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('threading.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def thread_function(name):
    print('thread {} start running'.format(name))
    time.sleep(2)
    print('thread {} finish running'.format(name))



if __name__ == '__main__':

    threads = list()
    for index in range(3):
        logger.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()


    for index, thread in enumerate(threads):
        logger.info("Main    : before joining thread %d.", index)
        thread.join()
        logger.info("Main    : thread %d done", index)
