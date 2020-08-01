import requests


def request(login, password):
    r = requests.post('http://127.0.0.1:5000/auth', data={'login': login, 'password': password})
    return r.status_code == 200
