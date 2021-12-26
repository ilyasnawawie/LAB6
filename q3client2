import sys
import socket

Client2socket = socket.socket()
host = '192.168.56.4'
port = 8080

print("Waiting for connection")

try:
    Client2socket.connect((host, port))
except socket.error as e:
    print(str(e))

msg = Client2socket.recv(1024)
print(msg.decode('utf-8'))
cmsg = "Client 2 has connected successfully"
Client2socket.send(cmsg.encode('utf-8'))

while True:

    print("[1] Logarithmic function (LOG)")
    print("[2] Square Root function (SQRT)")
    print("[3] Exponential function (EXP)")
    print("[4] Logarithmic function 10 (LOG10)")

    print("[q] Exit system")
    option = input('Please choose the option you would like to use:  ')

    if option == '1' or option == '2' or option == '3' or option == '4':
        value = input("Enter a value: ")
        option = option + ":" + value
        Client2socket.send(str.encode(option))

    elif option == 'q':
        print("Closing connection")
        Client2socket.send(str.encode(option))
        sys.exit()

    else:
        print("Input not recognize")
        sys.exit()

    msg = Client2socket.recv(1024)
    print(msg.decode("utf-8"))

Client2socket.close()
