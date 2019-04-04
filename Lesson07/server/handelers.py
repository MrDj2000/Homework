import logging
from log import server_log_config
from routes import resolve
from protocol import (
    validate_request, make_response,
    make_400, make_404
)

logger = logging.getLogger('server')

def handle_client_request(request):
    action_name = request.get('action')
    if validate_request(request):
        controller = resolve(action_name)
        if controller:
            try:
                return controller(request)
                # if action_name == 'shutdown_server':
                #     logger.info('Shutdown server')
                #     response_string = json.dumps(response)
                #     client.send(response_string.encode('utf-8'))
                #     break

            except Exception as err:
                logger.critical(err, exc_info=True)
                return make_response(
                    request,
                    500,
                    'Internal server error.'
                )
        else:
            logger.error(f'Action not found: {action_name}')
            return make_404(request)
    else:
        logger.error(f'Bad request: {request}')
        return make_400(request)