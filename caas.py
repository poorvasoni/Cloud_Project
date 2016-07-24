#!/usr/bin/python2

def begin(s,user,passwd):

	import os,commands,time
	
	os.system('route add -net 172.17.0.0/16 gw 192.168.56.102')
	
	os.system("dialog --menu \"Choose your Desired Container\"  20 40 10 1 \"Ubuntu Container\n\" 2 \"Cent-os Container\" 3 \"MintOS Container\" 4 \"Back\" 5 \" Exit \"  2>/tmp/choice.txt")

	c=open('/tmp/choice.txt')
	
	container=c.read()

	#Ubuntu as Container

	if container=='1':

		s.send(container)

		ip=s.recv(10)

		print ip

		os.system("ssh {}@{}".format(user,ip))

		


