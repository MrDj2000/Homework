import socket
import json
from datetime import datetime
from settings import (
    HOST, PORT
)


def request(action):
    sock = socket.socket()
    sock.connect((HOST, PORT))

    if action == 'presence':
        request_string = json.dumps(
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

    elif action == 'upper_text' or action == 'lower_text':
        data = input('Data: ')
        request_string = json.dumps(
            {
                'action': action,
                'time': datetime.now().timestamp(),
                'data': data
            }
        )

    else:
        request_string = json.dumps(
            {
                'action': action,
                'time': datetime.now().timestamp()
            }
        )

    sock.send(request_string.encode())
    response = sock.recv(1024)

    if response:
        return response
    else:
        sock.close()
        return





