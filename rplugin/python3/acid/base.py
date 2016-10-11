# encoding:utf-8
""" Acid stands for Asynchronous Clojure Interactive Development. """
import nrepl
from collections import deque
import asyncio

def _connect(port_no):
    return nrepl.connect("nrepl://localhost:{}".format(port_no()))

def _write(ch, op="eval", ns="user", **data):
    data.update({"op": op, "ns": ns})
    ch.write(data)
    return ch

async def send(port_no_fn, **data):
    ch = _write(_connect(port_no_fn), **data)

    yield data

    async for out in ch:
        yield out
        if "status" in out:
            break

    return queue

def sync_send(port_no_fn, handler,  **data):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(send(port_no_fn, handler, **data))
