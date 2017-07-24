def SunkiReadlines():
    seek = 0
    while True:
        with open('/Users/Pisces/Desktop/mao.txt', 'r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return


for item in SunkiReadlines():
    print item

temp = lambda x, y: x * y
print temp(4, 8)

a = 'gt' if 1 > 3 else 'lt'
print a

b = lambda x: x * 5
print b(9)

print [x * x for x in range(10)]

print map(lambda x: x * 2, range(10))

t1 = 123
print id(t1)
print dir()
print vars()
print divmod(9, 4)
print pow(3,3)
print all([1,4,5,62])
print any([1,4,5,0])
print chr(90)
print ord('B')
li = ['sunki','demi','yuki']
for i in li:
    print i
for i in enumerate(li, 7):
    print i
s='i am {},{},{}'
print s.format('sunki','is','great')
print map(lambda x:x*x, range(4))
l1 = [1,2,3,89]
def foo(arg):
    if arg<22:
        return True
    else:
        return False
temp = filter(foo, l1)
print temp