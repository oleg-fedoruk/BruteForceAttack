states = {
    #state_key: 0
}

with open('generators/users.txt') as user_file:
    s = user_file.read()
    logins = s.split('\n')


def get_next_str(state_key):
    if state_key not in states:
        states[state_key] = 0
    if states[state_key] >= len(logins):
        return None

    login = logins[states[state_key]]
    states[state_key] += 1

    return ''.join(login)


if __name__ == '__main__':
    for step in range(1000000):
        print(get_next_str('1'))
