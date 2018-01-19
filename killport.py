import os,sys,re
''' 
python /personal/killport.py 8001
'''
params = sys.argv
if len(params)>1:
    port = params[1]

cinfo = os.popen('lsof -i:%s'%port).read()
if cinfo:
    print cinfo
    gport = re.search(r'/usr/bin/ \d+',cinfo)
    if gport:
        port = gport.group().split(' ')[1]
        print 'kill -9 %s'%port
        os.system('kill -9 %s'%port)
else:
    print 'no port'
