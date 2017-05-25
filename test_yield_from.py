# python3
# coding: utf-8

import asyncio
import requests
import time
import io

def wait():
    print ("sleep")
    yield from asyncio.sleep(2)
    print ("awake") 

def getsogou():
    print ("begin load sogou")
    session = requests.session()
    response = session.get("http://www.sogou.com")
    with open("www.sogou.com.html", "wb") as f:
        f.write(response.text.encode("utf-8", "ignore"))
        f.close()
    yield
    print ("finish load sogou")

def getwangyi():
    print ("begin load wangyi")
    session = requests.session()
    response = session.get("http://www.163.com")
    with open("www.163.com", "wb") as f:
        f.write(response.text.encode("gb2312", "ignore"))
        f.close()
    yield
    print ("finish load wangyi")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [getsogou(), getwangyi()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()