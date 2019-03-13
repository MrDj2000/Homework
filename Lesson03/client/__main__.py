import socket
import json
import sys

while True:
    s = socket.socket()

    address = str(sys.argv[1])  # 'localhost'

    if len(sys.argv) == 2:
        port = 7777
    elif len(sys.argv) == 3:
        port = int(sys.argv[2])

    s.connect((address, port))

    action = str(input('Enter action: '))
    data = input('Data: ')
    request_string = json.dumps(
        {'action': action, 'data': data}
    )

    s.send(request_string.encode())
    response = s.recv(1024)

    if response:
        print(response.decode())
        if action == 'stop_client' or action == 'stop_server':
            #s.close()
            break
    else:
        s.close()
        break
