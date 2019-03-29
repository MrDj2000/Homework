import sys
import logging
from datetime import datetime
from functools import wraps
from protocol import make_response
from log import server_log_config

logger = logging.getLogger('server')

def stack_logging(message='',parent_func_name=''):
    def decorator(func):
        @wraps(func)
        def wrap(request, *args, **kwargs):
            format_mapping = {
                'parent_func_name': parent_func_name,
                'func_name': func.__name__,
                'date_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                'request_data': request.get('data')
            }
            message_str = message % format_mapping
            logger.warning(message_str)

            return func(request, *args, **kwargs)
        return wrap
    return decorator

def login_required(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        user = request.get('user')
        user_name = user.get('account_name')
        if user_name:
            logger.warning(f'User name - {user_name}')
            return func(request, *args, **kwargs)
        return make_response(request, 403, 'Access denied.')
    return wrap