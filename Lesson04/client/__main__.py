import socket
import json
import sys
from datetime import datetime


if len(sys.argv) == 2:
    port = 7777
elif len(sys.argv) == 3:
    port = int(sys.argv[2])

address = str(sys.argv[1])

sock = socket.socket()
sock.connect((address, port))

presence = json.dumps(
    {
        'action': 'presence',
        'time': datetime.now().timestamp(),
        'type': 'status',
        'code': 100,
        'user': {
            'account_name': 'MrDj2000',
            'status': 'Yep, I am here!'
        }
    }
)

sock.send(presence.encode())
response_hello = sock.recv(1024)

if not response_hello:
    sock.close()
else:
    print(response_hello.decode())

    while True:
        sock = socket.socket()
        sock.connect((address, port))

        action = str(input('Enter action: '))
        data = input('Data: ')
        request_string = json.dumps(
            {
                'action': action,
                'time': datetime.now().timestamp(),
                'data': data
            }
        )

        sock.send(request_string.encode())
        response = sock.recv(1024)

        if response:
            print(response.decode())
            if action == 'quit' or action == 'stop_server':
                break
        else:
            sock.close()
            break
