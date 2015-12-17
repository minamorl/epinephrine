import socketserver

l = []

PREFIX = "#"
CMD_RETRIVE = "RETRIVE"

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global l
        data = self.request.recv(1024).strip().decode()
        print("send from {}".format(self.client_address[0]))
        if data.startswith(PREFIX + CMD_RETRIVE):
            try:
                _, line, page = data.split(":")
                ret = l[int(line)*int(page):int(line)*int(page)+int(line)]
                self.request.sendall("\n".join(ret).encode())
            except:
                self.request.sendall(b"0")

            return
        
        l.append(data)
        print("\n".join(l))

        self.request.sendall(b"1")



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
        print("bye.")

