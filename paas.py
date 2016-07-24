#!/usr/bin/python

def begin(s,user,passwd):

        import os,commands,menu,time
	
	os.system('route add -net 172.17.0.0/16 gw 192.168.56.102')	
	
	os.system('dialog --menu "Choose any Platform" 30 30 5 1 "Python Interpreter" 2 "PHP" 3 "Ruby" 4 "Database" 5 "Other" 2>/tmp/plat.txt')

	pl=open('/tmp/plat.txt')
	plat=pl.read()
	s.send(plat)
#python
	if plat=='1':
		
		ip=s.recv(10)
		print ip
		os.system("route add -net 172.17.0.0/16 gw 192.168.56.102")
		os.system(" ssh  {}@{}".format(user,ip))

		
#pHp
	elif  plat=='2':

                ip=s.recv(10)
                print ip
		os.system("route add -net 172.17.0.0/16 gw 192.168.56.102")
                os.system(" ssh  {}@{}".format(user,ip))
 
#RUBY

	elif plat=='3':

                ip=s.recv(10)
                print ip
		os.system("route add -net 172.17.0.0/16 gw 192.168.56.102")
                os.system(" ssh  {}@{}".format(user,ip))
#database
	elif plat=='4':

                ip=s.recv(10)
                print ip
		os.system("route add -net 172.17.0.0/16 gw 192.168.56.102")
                os.system(" ssh  {}@{}".format(user,ip))



