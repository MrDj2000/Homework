import json
import socket
import sys
import logging
import select
from log import server_log_config
from handelers import handle_client_request
from settings import (
    HOST, PORT
)

logger = logging.getLogger('server')

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

requests = []
connections = []

try:
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)
    sock.settimeout(0)

    logger.warning(f'Server start with host:{HOST} and port: {PORT}')

    while True:
        try:
            client, address = sock.accept()
            connections.append(client)
            logging.warning(f'Client detected {"%s:%s" % address}')
        except OSError:
            pass

        rlist = []
        wlist = []

        try:
            rlist, wlist, xlist = select.select(
                connections, connections, [], 0
            )
        except:
            pass

        for client in rlist:
            data = client.recv(1024)

            if data:
                sock.close()
                request = json.loads(data.decode('utf-8'))
                requests.append(request)

        if requests:
            for request in requests:
                for client in wlist:
                    response = handle_client_request(request)
                    response_string = json.dumps(response)
                    client.send(response_string.encode('utf-8'))
                    logging.info(
                        f'Response {response_string} sended to {client.getsockname()}'
                    )
                requests.remove(request)

except KeyboardInterrupt:
    logger.info('Shutdown server')
    sock.close()
