# import sys
import select
import socket
import logging
import argparse
from request import request
from log import client_log_config
from settings import (
    HOST, PORT
)


# if len(sys.argv) == 2:
#     address = str(sys.argv[1])
# elif len(sys.argv) == 3:
#     address = str(sys.argv[1])
#     port = int(sys.argv[2])

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', type=str, default='w')
cmd_args = parser.parse_args()

logger = logging.getLogger('client')
logger.warning(f'Client start with host:{ HOST } and port: { PORT }')

try:
#    presence = request('presence')

#    if presence:
#    logger.warning(f'Message send server - {presence.decode()}')

    if cmd_args.mode == 'w':
        while True:
            action = str(input('Enter action: '))
            response = request(action)

            if response:
                logger.info(f'Response from server - {response.decode()}')
                if action == 'quit' or action == 'shutdown_server':
                    break
            else:
                logger.warning(f'Did not response from server')
                break
    else:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        logger.warning(f'Client Read')
        while True:
            rlist, wlist, xlist = select.select([], [sock], [], 0)
            response = sock.recv(1024)
            if response:
                logger.warning(response.decode())
                break

except Exception as err:
    logger.error(f'Error - {err}')
