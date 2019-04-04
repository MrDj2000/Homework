import json
import socket
import sys
import logging

from protocol import (
    validate_request, make_response,
    make_400, make_404
)
from routes import resolve
from log import server_log_config


port = 7777
address = '0.0.0.0'

if len(sys.argv) == 3:
    if sys.argv[1] == '-p':
        port = sys.argv[2]
    elif sys.argv[1] == '-a':
        address = sys.argv[2]
elif len(sys.argv) == 5:
    if sys.argv[1] == '-p' and sys.argv[1] == '-a':
        port = sys.argv[2]
        address = sys.argv[4]
    elif sys.argv[1] == '-a' and sys.argv[1] == '-p':
        address = sys.argv[2]
        port = sys.argv[4]

sock = socket.socket()
sock.bind((address, port))
sock.listen(5)

logger = logging.getLogger('server')
logger.info(f'Server start with host:{ address } and port: { port }')
try:
    while True:
        client, address = sock.accept()
        logger.info(f'Client detected {address}')
        data = client.recv(1024)
        request = json.loads(data.decode('utf-8'))

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)

            if controller:
                try:
                    response = controller(request)

                    if action_name == 'shutdown_server':
                        logger.info('Shutdown server')
                        response_string = json.dumps(response)
                        client.send(response_string.encode('utf-8'))
                        break

                except Exception as err:
                    logger.critical(err, exc_info=True)
                    response = make_response(
                        request,
                        500,
                        'Internal server error.'
                    )
            else:
                logger.error(f'Action not found: {action_name}')
                response = make_404(request)
        else:
            logger.error(f'Bad request: {request}')
            response = make_400(request)

        response_string = json.dumps(response)
        client.send(response_string.encode('utf-8'))

except KeyboardInterrupt:
    logger.info('Shutdown server')
    sock.close()


