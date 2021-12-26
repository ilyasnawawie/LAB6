import sys
import socket

Client1socket = socket.socket()
host = '192.168.56.4'
port = 8080

print("Waiting for connection")

try:
    Client1socket.connect((host, port))
except socket.error as e:
    print(str(e))

msg = Client1socket.recv(1024)
print(msg.decode('utf-8'))
cmsg = "Client 1 has connected successfully"
Client1socket.send(cmsg.encode('utf-8'))

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
        Client1socket.send(str.encode(option))



    elif option == 'q':
        print("Closing connection")
        Client1socket.send(str.encode(option))
        sys.exit()


    else:
        print("Input not recognize")
        sys.exit()

    msg = Client1socket.recv(1024)
    print(msg.decode("utf-8"))

Client1socket.close()
