import socket
import json
import sys
from datetime import datetime
import logging
from log import client_log_config

port = 7777
address = 'localhost'

if len(sys.argv) == 2:
    address = str(sys.argv[1])
elif len(sys.argv) == 3:
    address = str(sys.argv[1])
    port = int(sys.argv[2])

logger = logging.getLogger('client')
logger.info(f'Client start with host:{ address } and port: { port }')
try:
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
        logger.info(f'Message send server - {response_hello.decode()}')

        while True:
            sock = socket.socket()
            sock.connect((address, port))

            action = str(input('Enter action: '))
            if action == 'upper_text' or\
               action == 'lower_text':
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
                logger.info(f'Response from server - {response.decode()}')
                if action == 'quit' or action == 'shutdown_server':
                    break
            else:
                logger.warning(f'Did not response from server')
                sock.close()
                break
except Exception as err:
    logger.error(f'Error - {err}')
