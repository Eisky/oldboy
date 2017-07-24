def tour(name, action='diving', where='Puti'):
    print name, 'go to', where, action


print tour('sunki')
print tour('demi', where='hainan', action='honeymoon')
print tour('emily', where='greece')
print tour('yuki', action='sightseeing')


def show(*args):
    for item in args:
        print item


b = show('sunki', 'demo', 'suji')
print b


def exhibit(**kargs):
    for item in kargs.items():
        print item


c = exhibit(name='sunki',age=18,city='shanghai',hometown='henan')
print c
