#!/usr/bin/python
# This python script runs when the user wants to add the friends checked
import cgitb # lets us interpret cgi formating
import sys
import cgi
import fileinput
cgitb.enable() # enables some debuggin???

print "Content-type: text/html\n\n" # line that lets the client browser know we write html
form = cgi.FieldStorage()

# need the currentUser
currentUser = ""
with open ( "currentUser.txt" , "r" ) as uF: # currentUser is just the username. uF is for userFile
	currentUser = uF.readline()
#print currentUser + " is current user <br>"

# put the contents of the form into a list called addfriend
addfriend = form.getvalue ( 'fullname' ) # get the fullname stored in value attribute of html. html form name="fullname" has value


# this is the string of friends we will add to the friends.txt file
toAdd = ""
toAdd += currentUser + " "

# open the friends.txt file for reading and writing
friendList = open ( "friends.txt" , "r+" )

# below we loop through selected friends in form. !!! addfriend is what the current userchecked
# we create a string we will insert ie toAdd
newFriend = ""

for friend in addfriend:
	if friend.endswith ( "\r\n" ):
		if friend != currentUser:
			friend = friend.strip ( "\r\n" )
			toAdd += friend
			toAdd += " "
	elif friend.endswith ( "" ):
		print friend
		toAdd += friend

toAdd += " "
print "This is toAdd : " + toAdd + "<br>"


# loops through friends.txt
# inserts toAdd which is of format username friend1 friend2 etc into friends.txt file
for line in fileinput.input ( "friends.txt" , inplace = 1 ):
	if line.startswith ( currentUser ):
		print toAdd, # comma prevents the new line?
	else:
		print line,  
	#print line + "<br>"

