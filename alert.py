#!/usr/bin/env python
"""A simple script to send
and instant message via Google
Talk on the xmpp server"""

import sys, xmpp, datetime, os, re

now = datetime.datetime.now()

username = sys.argv[1]
password = sys.argv[2]
to = 'uwmadisondmc@gmail.com'
msg = "Someone is at the front door. \n %s" % now.strftime("%Y-%m-%d %H:%M:%S")
#(now.year(), now.month(), now.day(), now.hour(), now.minute(), now.second())


client = xmpp.Client('gmail.com')
client.connect(server=('talk.google.com',5223))
client.auth(username, password, 'botty')
client.sendInitPresence()
message = xmpp.Message(to, msg)
message.setAttr('type', 'chat')
client.send(message)

folder = '/home/pi/motion'
for x in os.listdir(folder):
    file_path = os.path.join(folder, x)
    try:
        if re.search(r'[\d\d-\d+[-\d\d]?\..*', x) is not None:
            os.remove(file_path)
    except Exception, e:
        print e

sys.exit(0)
