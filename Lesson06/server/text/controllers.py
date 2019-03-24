import logging
from protocol import make_response, make_400
from decorators import ( stack_logging, login_required )

logger = logging.getLogger('server')

@login_required
@stack_logging('%(date_time)s Function %(func_name)s was called from %(parent_func_name)s', __name__)
def presence(request):
    user = request.get('user')

    if not user:
        return make_400(request)
#    user_name = user.get('account_name')
#    logger.info(f' User name - {user_name}')
    return make_response(
        request,
        200,
        'Hello ' + user.get('account_name')
    )


@stack_logging('%(date_time)s Function %(func_name)s was called from %(parent_func_name)s', __name__)
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


@stack_logging('%(date_time)s Function %(func_name)s was called from %(parent_func_name)s', __name__)
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


@stack_logging('%(date_time)s Function %(func_name)s was called from %(parent_func_name)s', __name__)
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
