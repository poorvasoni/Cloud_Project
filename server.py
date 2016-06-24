#!/usr/bin/python2

import socket,commands

s=socket.socket()

ip="192.168.43.8"

port=1234
s.bind( (ip,port) )

p=s.recvfrom(10)

cdata=p[0]

print cdata

if cdata=='1':
	x=raw_input("enter your user name : ")

	s.sendto(x, ("192.168.43.8",1234) )

	y=raw_input(" enter your password : ")

	s.sendto(y, ("192.168.43.8",1234) )


else:

	x=raw_input("enter your user name : ")

	s.sendto(x, ("192.168.43.8",1234) )
	p1=s.recvfrom(10)

	y=raw_input(" enter your password : ")

	s.sendto(y, ("192.168.43.8",1234) )
	
	p2=s.recvfrom(10)
	
	


	y=commands.getstatusoutput("useradd {}".format(p1[0]))

	if y[0]==0:
		print "successful"











	z=commands.getstatusoutput("echo {} | passwd {} --stdin".format(p2[0],p1[0]))



	s.sendto( "user added successfully", p2[1] )




p3=s.recvfrom(10)
if(p3[0]=='1'):
	da=commands.getstatusoutput("date")
	s.sendto(da[1], p3[1])
elif(p3[0]=='2'):
	ca=commands.getoutputstatus("cal")
	s.sendto(ca[1],p3[1])	
elif(p3[0]=='3'):
	s.sendto( "you have choosen Storage as a Services", p3[1])
elif(p3[0]=='4'):
	s.sendto("you have choosen Software as a Services", p3[1])
else:
	s.sendto("Wrong Input",p3[1])

