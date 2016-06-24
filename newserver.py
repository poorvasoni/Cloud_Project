#!/usr/bin/python2

import socket,commands

s=socket.socket()

s.bind(("",4444))

s.listen(5)

c,addr=s.accept()

c.send("Welcome to MY CLOUD \n")

c.send("Press 1:To Login \n Press 2:To Register ")



ch= c.recv(10)

print ch

if ch.strip()=='1':
	c.send("enter your user name : ")
	user=c.recv(20)
	c.send("enter your password : ")
	passwd=c.recv(20)
	if user.strip()=="vimal" and passwd.strip()=="lw":
		c.send("successful \n")
		c.send(" Press 1:To take STASS \n Press 2: To take SAAS \n Press 3: To take IAAS \n Press 4: To take PAAS" )
		cmd=c.recv(100)
		acmd=cmd.strip()
		if acmd=='1':
			stass.main()
		elif acmd=='2':
			saas.main()
		elif acmd=='3':
			iaas.main()
		elif acmd=='4':
			paas.main()
		else:
			c.send("wrong choice")
		
		c.close()
	else: 
		c.send("Authentication failed")
		c.close()

elif ch.strip()=='2':
	c.send("enter your user name : ")
	user1=c.recv(10)
	c.send("enter your password : ")
	passwd1=c.recv(10)

	out1=commands.getstatusoutput("useradd {}".format(user1))
	print out1
	#out2=commands.getstatusoutput("echo {} | passwd {} --stdin".format(user1,passwd1))
	
	#print out2[0]
	if out1[0]==0:
		c.send("\n user added successfully")
else:
	c.send("wrong entery  \n")	
c.close()

