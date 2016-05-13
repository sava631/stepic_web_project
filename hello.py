#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from cgi import parse_qs

def app(environ, start_response):
    data = b'Hello, World!\n'
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    qs =  parse_qs(environ['QUERY_STRING'])
    #for x in qs:
    #    for y in qs[x]:
    #        print(x, '=', y, sep='')
    return iter([data])

