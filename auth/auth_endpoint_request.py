def auth_endpoint(request):
    auth_token = request.headers['Authorization'].replace('Bearer ', '')
    return process_request(request, auth_token)


def process_request(request, auth_token):
    import os
    from flask import abort
    if os.environ['VALUE_AUTH'] == auth_token:
        return 'OK'
    else:
        return abort(401)