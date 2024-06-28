calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(a):
    count_calls()
    return (len(a), a.upper(), a.lower())


def is_contains(q, w):
    count_calls()
    q = q.lower()
    w = [i.lower() for i in w]
    return q in w


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('parade', ['paradigma', 'separating', 'prepare']))
print(calls)