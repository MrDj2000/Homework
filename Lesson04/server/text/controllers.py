from protocol import make_response, make_400

def presence(request):
    user = request.get('user')
    if not user:
        return make_400(request)
    print(user.get('account_name'))
    return make_response(
        request,
        200,
        'Hello ' + user.get('account_name')
    )

def get_upper_text(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    print(data)
    return make_response(
        request,
        200,
        data.upper()
    )


def get_lower_text(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    print(data)
    return make_response(
        request,
        200,
        data.lower()
    )
