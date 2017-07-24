def foo(name):
    print name, ',', 'you have to be careful'


foo('sunki')
foo('sophia')
foo('demi')


def login(username):
    if username == 'sunki':
        return 'success'
    else:
        return 'failed'


def detail(user):
    print user, 'xxxxxxxxx'


if __name__ == '__main__':
    user = raw_input('please enter your name:')
    a = login(user)
    if a == 'success':
        detail(user)
    else:
        print 'no money left'