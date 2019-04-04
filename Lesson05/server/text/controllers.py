import logging
from protocol import make_response, make_400

logger = logging.getLogger('server')

def presence(request):
    user = request.get('user')

    if not user:
        return make_400(request)
    user_name = user.get('account_name')
    logger.info(f' User name - {user_name}')
    return make_response(
        request,
        200,
        'Hello ' + user.get('account_name')
    )

def shutdown_server(request):
    data = 'Shutdown server'
    if not data:
        return make_400(request)
    logger.info(data)
    return make_response(
        request,
        200,
        data
    )


def get_upper_text(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    logger.info(data.upper())
    return make_response(
        request,
        200,
        data.upper()
    )


def get_lower_text(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    logger.info(data.lower())
    return make_response(
        request,
        200,
        data.lower()
    )
