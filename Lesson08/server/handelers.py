import json
from routes import resolve
from protocol import (
    validate_request, make_response,
    make_400, make_404
)
import logging
from log import server_log_config


logger = logging.getLogger('server')

def read_request(client, requests):
    try:
        data = client.recv(1024)

        if data:
            request = json.loads(data.decode('utf-8'))
            requests.append(request)
    except:
        pass

def write_response(client, request):
    action_name = request.get('action')
    if validate_request(request):
        controller = resolve(action_name)
        if controller:
            try:
                response = controller(request)
                # if action_name == 'shutdown_server':
                #     response_string = json.dumps(response)
                #     client.send(response_string.encode('utf-8'))
                #     break
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