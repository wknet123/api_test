import time

t = time.strptime("2016-02-26 23:59:59", "%Y-%m-%d %H:%M:%S")
print int(time.mktime(t))