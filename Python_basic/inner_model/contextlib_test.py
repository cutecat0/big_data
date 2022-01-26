#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
from contextlib import contextmanager


logging.getLogger().setLevel(logging.INFO)


def contextlib_test():
    """
    try...catch...finally is too much busy...
    use with can be more easily
    :return:
    """
    pass


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        logging.info('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logging.info('Error')
        else:
            logging.info('End')

    def query(self):
        logging.info('Query info about %s ' % self.name)


class QueryV2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        logging.info('Query info about %s ' % self.name)


@contextmanager
def create_query(name):
    """
    @contextmanager this decorator receive a generator
    use yield make with ... as var output
    then with can work normally
    :param name:
    :return:
    """
    logging.info('Begin...')
    q = QueryV2(name)
    yield q
    logging.info('End')


if __name__ == '__main__':

    # contextlib_test()
    # pass

    # with Query('Simba') as q:
    #     q.query()

    # INFO:root:Begin
    # INFO:root:Query info about Simba
    # INFO:root:End
    #
    # Process finished with exit code 0

    with create_query('Simba') as q:
        q.query()

    # INFO:root:Begin...
    # INFO:root:Query info about Simba
    # INFO:root:End
    #
    # Process finished with exit code 0



