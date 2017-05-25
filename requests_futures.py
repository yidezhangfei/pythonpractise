# python3
# coding: utf-8

import asyncio
from requests_futures.sessions import FuturesSession

async def getsogouinternal():
    print ("begin load sogou")
    session = FuturesSession()
    response = session.get("http://www.sogou.com")
    with open("www.sogou.com", "wb") as f:
        f.write(response.text.encode("utf-8", "ignore"))
        f.close()
    print ("finish load sogou")

async def getsogou():
    return await getsogouinternal()

async def wait():
    print ("sleep")
    await asyncio.sleep(3)
    print ("awake")

if __name == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [getsogou(), wait()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()