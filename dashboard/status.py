#!/usr/bin/python

import cgi, cgitb, urllib
form = cgi.FieldStorage()

#figure out a way to get the username
status = form.getvalue('status')

user = urllib.urlopen("http://www.cs.mcgill.ca/~eander40/currentUser.txt")

print "Content-type: text/html\n\n"
print ' <a href="http://www.cs.mcgill.ca/~yzhu399/dashboard.py">Back to Dashboard</a>'

currentUser = user.read()

if status: 
	f = open("status.txt", "a")
	f.write(currentUser + ' ' + status + " \n\r")
	f.close()
