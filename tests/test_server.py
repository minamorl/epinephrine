import socket
import sys
import os
import functools

result = None


import functools
@functools.lru_cache()
def get_storage():
    from epinephrine.__main__ import Storage
    def _(x):
        global result
        result = x
    return Storage(sendall=_)

def send(data):
    storage = get_storage().handle(data)
    return result.decode()
    


def test_send():
    assert "1" == send("#CLEAR")
    dummy = "#INSERT:data"
    assert "1" == send(dummy)
    dummy = "#INSERTdata"
    assert "0" == send(dummy)

def test_clear():
    assert "1" == send("#CLEAR")
    assert "0" == send("#LENGTH")

def test_pagination():
    assert "1" == send("#CLEAR")
    dummy = "#INSERT:data"
    assert "1" == send(dummy)
    assert "1" == send(dummy)
    assert "1" == send(dummy)
    assert "data\ndata\ndata" == send("#RETRIVE:3:0")
    assert "" == send("#RETRIVE:3:1")

def test_dump():
    assert "1" == send("#DUMP")
    dummy = "#INSERT:data"
