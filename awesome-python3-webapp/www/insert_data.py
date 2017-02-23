# !/usr/env/python3
# coding: utf-8

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='lijun', password='li999888', db='awesome')
    users = [
        User(name='lijun', email='lijun@sogou-inc.com', password='li999888', image='about:blank'),
        User(name='gyn', email='gyn@whd.com', password='gyn', image='about:blank'),
    ]
    for u in users:
        await u.save()
    await orm.destroy_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
