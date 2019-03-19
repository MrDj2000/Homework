from .controllers import (
    get_upper_text, get_lower_text, presence
)


routes = [
    {'action': 'presence', 'controller': presence},
    {'action': 'upper_text', 'controller': get_upper_text},
    {'action': 'lower_text', 'controller': get_lower_text}
]