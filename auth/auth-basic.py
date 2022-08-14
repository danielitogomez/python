from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "username": "password"
}

@auth.get_password
def get_password(username):
    return users.get(username)

@auth.login_required
def test_basic_auth(request):
    return f"{auth.username()}, you may pass!"