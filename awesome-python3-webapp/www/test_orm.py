# !/usr/env/python3
# coding: utf-8

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='lijun', password='li999888', database='awesome')
    u = User(name='Test', email='Test@sogou-inc.com', password='123456', image='about:blank')
    await u.save()
    await orm.destroy_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
