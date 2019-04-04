import json
import socket
import sys
import logging

from protocol import (
    validate_request, make_response,
    make_400, make_404
)
from routes import resolve

logger = logging.getLogger('default')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('default.log')

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

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

try:
    while True:
        client, address = sock.accept()
        print(f'Client detected {address}')
        data = client.recv(1024)
        request = json.loads(data.decode('utf-8'))

        if validate_request(request):
            controller = resolve(request.get('action'))
            if controller:
                try:
                    response = controller(request)
                except Exception:
                    response = make_response(
                        request,
                        500,
                        'Internal server error.'
                    )
            else:
                response = make_404(request)
        else:
            response = make_400(request)

        response_string = json.dumps(response)
        client.send(response_string.encode('utf-8'))
        print(response_string)
#        client.close()

except KeyboardInterrupt:
    sock.close()


