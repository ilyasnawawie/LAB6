import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 Not Found\n\n'


def mathcalc(s_sock):
    msg = "\nWelcome to the Server!"
    s_sock.send(msg.encode('utf-8'))

    msg2 =s_sock.recv(1024)
    print(msg2.decode('utf-8')) 
    while True:
        data = s_sock.recv(2048).decode("utf-8").split(":")

        if data[0] == "1":
            reply = math.log(float(data[1]))

        elif data[0] == "2":
            reply = math.sqrt(float(data[1]))

        elif data[0] == "3":
            reply = math.exp(float(data[1]))

        elif data[0] == "4":
            reply = math.log10(float(data[1]))

        else:
            sys.exit()

        s_sock.sendall(str.encode(str(reply)))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8080))
    print("\nListening to an incoming connection...")
    s.listen(3)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=mathcalc, args=(s_sock,))
                p.start()
            except socket.error:
                print("An error has occured on the socket")
    except Exception as e:
        print("An exception has occured!")
        print(e)
