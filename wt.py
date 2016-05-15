#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def app(environ, start_response):
    data = ''
    x = random.randint(0,4)
    y = random.randint(0,1)
    z = random.randint(0,1)
    nac = ['США', 'Германия', 'СССР', 'Великобритания', 'Япония']
    teh = ['Танки', 'Самолёты']
    tip = [' (Аркада)', ' (Реалистичные)']
    data = nac[x]
    if x != 4:
        data = nac[x] + ' - ' + teh[y]
    else:
        data = nac[x] + ' - Самолёты'
    if y == 0:
        data += tip[z]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain;charset=utf-8'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [data]
