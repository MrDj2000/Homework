import json
import socket
import sys
from datetime import datetime

sock = socket.socket()

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

sock.bind((address, port))

sock.listen(5)

while True:
    client, address = sock.accept()
    print(f'Client detected {address}')
    data = client.recv(1024)
    request = json.loads(
        data.decode('utf-8')
    )

    if request.get('action') == 'get_time':
        date = datetime.now()
        response_string = date.strftime('%d-%m-%y T%H:%M:%S')
        client.send(response_string.encode('utf-8'))
    elif request.get('action') == 'upper_text':
        client_data = request.get('data')
        response_string = client_data.upper()
        client.send(response_string.encode('utf-8'))
    elif request.get('action') == 'stop_client':
        response_string = 'The client has been closed connect'
        client.send(response_string.encode('utf-8'))
        client.close()
    elif request.get('action') == 'stop_server':
        response_string = 'The server has been stopped'
        print(response_string)
        client.send(response_string.encode('utf-8'))
        client.close()
        break
    else:
        response_string = 'Action not supported'
        client.send(response_string.encode('utf-8'))

    print(response_string)

#    client.close()


