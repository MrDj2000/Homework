from .controllers import (
    presence, shutdown_server, get_upper_text, get_lower_text
)


routes = [
    {'action': 'presence', 'controller': presence},
    {'action': 'shutdown_server', 'controller': shutdown_server},
    {'action': 'upper_text', 'controller': get_upper_text},
    {'action': 'lower_text', 'controller': get_lower_text}
]