# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/xml')])
    return [b'<h1>Hello, Web!</h1>']
