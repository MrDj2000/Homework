import json
import socket
import sys
import logging
import select
import threading
from log import server_log_config
import collections
from handelers import (
    read_request, write_response
)
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

requests = collections.deque()
connections = []

try:
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)
    sock.settimeout(0.5)

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
            read_thread = threading.Thread(
                target=read_request,
                args=(client, requests)
            )
            read_thread.start()
            if requests:
                logging.warning(
                    f'Read request {requests} from {client.getsockname()}'
                )

        if requests:
            request = requests.popleft()
            for client in wlist:
                write_thread = threading.Thread(
                    target=write_response,
                    args=(client, request)
                )
                write_thread.start()
                logging.warning(
                    f'Send request {request} to {client.getsockname()}'
                )

except KeyboardInterrupt:
    logger.info('Shutdown server')
    sock.close()
