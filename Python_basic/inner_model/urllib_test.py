#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import ssl
from urllib import request, parse

logging.getLogger().setLevel(logging.INFO)

ssl._create_default_https_context = ssl._create_unverified_context


def urllib_test(url):
    """
    Get
    :return:
    """
    with request.urlopen(url) as f:
        data = f.read()
        logging.info(f'Status: {f.status}, {f.reason}')

        for k, v in f.getheaders():
            logging.info(f'({k}:{v})')

        logging.info(f'Data: {data.decode("utf-8")}')


def get_test(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    urllib_test(url)


def post_test():
    """
    if use POST send a request, just need to input parameter 'data'
    as bytes style
    :return:
    """
    logging.info('Login to weibo.cn...')

    email = input('Email: ')


if __name__ == '__main__':

    # urllib_test()
    """
    result:
    INFO:root:Status: 200, OK
    INFO:root:(Connection:close)
    INFO:root:(Content-Length:49704)
    INFO:root:(Server:nginx)
    INFO:root:(Content-Type:text/html; charset=utf-8)
    INFO:root:(X-Frame-Options:DENY)
    INFO:root:(Via:1.1 vegur, 1.1 varnish, 1.1 varnish)
    INFO:root:(Accept-Ranges:bytes)
    INFO:root:(Date:Wed, 26 Jan 2022 06:36:57 GMT)
    INFO:root:(Age:655)
    INFO:root:(X-Served-By:cache-iad-kjyo7100127-IAD, cache-qpg1256-QPG)
    INFO:root:(X-Cache:HIT, HIT)
    INFO:root:(X-Cache-Hits:5, 9)
    INFO:root:(X-Timer:S1643179017.043127,VS0,VE0)
    INFO:root:(Vary:Cookie)
    INFO:root:(Strict-Transport-Security:max-age=63072000; includeSubDomains)
    INFO:root:Data: <!doctype html>
    <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
    <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
    <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
    <!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->
    
    <head>
    ...
    ...
    ...
    long text 
    """

    url = 'https://www.python.org/'
    get_test(url)
