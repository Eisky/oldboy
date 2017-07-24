'''
import sqlserverhelper
print sqlserverhelper.count()
'''

temp = 'mysqlhelper'
func = 'count'
model = __import__(temp)
Function = getattr(model, func)
model.count()

