import json

l1 = ['sunki', 'ate', 'sth', 'good']
s = json.dumps(l1)
print json.loads(s)
d = json.dump(l1, open('/Users/Pisces/Desktop/t.txt', 'w'))
print d
f = json.load(open('/Users/Pisces/Desktop/t.txt', 'r'))
print f