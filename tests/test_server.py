import socket
import sys

def send(data):
    HOST, PORT = "localhost", 9999

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        return str(sock.recv(1024), "utf-8")
    finally:
        sock.close()

def test_send():
    dummy = "#INSERT:data"
    assert "1" == send(dummy)
    dummy = "#INSERTdata"
    assert "0" == send(dummy)
