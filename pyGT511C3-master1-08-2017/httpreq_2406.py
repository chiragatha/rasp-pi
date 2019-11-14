#!/usr/bin/env python


print 'HTTP Request ...'




import httplib
conn = httplib.HTTPConnection("www.rtpl.co.in")
conn.request("HEAD","/index.html")
res = conn.getresponse()
print res.status, res.reason
    
    
print 'Closing ..'
