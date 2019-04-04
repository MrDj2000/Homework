import socket
import json
import sys
import time
from presence import json_presence


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
        'time': int(time.time()),
        'type': 'status',
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

        if action == 'upper_text':
            data = input('Data: ')
            request_string = json.dumps(
                {'action': action, 'data': data}
            )
        else:
            request_string = json.dumps(
                {'action': action}
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