import re

ip = '12.34.34.ddss.878.hd.43_w342d~192.168.2.1.hjji'
print re.findall('(\d+.)', ip)


import time
print time.time()
print time.gmtime()
print time.strftime('%Y-%m-%d')