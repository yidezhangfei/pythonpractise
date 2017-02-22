# coding: utf-8

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

import orm
from coroweb import add_routes, add_static

def init_jinja2(app, **kw):
    logging.info('init jinja2 ...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_stirng', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

async def logger_factory(app, handler):
    async def logger(request):
        logging.info('request: %s %s' % (request.method, request.path))
        return (await handler(request))
    return logger

async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startwith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startwith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        return (await handler(request))
    return parse_data


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='utf-8')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
