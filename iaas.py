#!/usr/bin/python

def begin(s,user,passwd):
	
	import os,commands,menu,time

	os.system("dialog --menu 'Choose What you want' 50 50 15 1 'Operating System via VNC' 2 'Operating System in Browser ' 3 'Operating System using QR code Scanner' 4 'In Android Mobile' 5 'My Instances' 6 'Back' 7 'Exit' 8 'Shut Down an Instance' 9 'Delete an Instance' 10 'Start your Instance' 11 'Os Gallery' 2>/tmp/hii.txt")

	oss=open('/tmp/hii.txt')

	ko=oss.read()

	s.send(ko)
#Browser
	if ko=='2':

		os.system("dialog --menu 'Choose Your Falour' 40 40 10 1 'Ubuntu' 2 'RedHat 7 ' 3 'MintOS' 4 'Cirros OS' 5 'Back' 6 'Exit'  2>/tmp/fla.txt")

		no=open('/tmp/fla.txt')

		mo=no.read()

		s.send(mo) 

		if mo=='1':

			os.system("dialog --inputbox \"Enter the RAM in mbs \" 40 40 2>/tmp/os.txt")

			ramm=open('/tmp/os.txt')

			rr=ramm.read()

			s.send(rr)

			os.system("dialog --inputbox \" Enter the no of cpu  \" 40 40 2>/tmp/os1.txt")

			cp=open('/tmp/os1.txt')

			cpuu=cp.read()

			s.send(cpuu)
	
			os.system("dialog --inputbox \"Enter HardDisk in GBs \" 40 40  2>/tmp/hd.txt")
 

			h=open('/tmp/hd.txt')

        		hd1=h.read()

       			s.send(hd1)

			portvnc=s.recv(10)

			ok=s.recv(10)
			os.system("dialog --msgbox 'Connect to the port no {}' 30 30 2>/tmp/lll.txt".format(portvnc))

			if ok=='done':
		

				done=commands.getstatusoutput("firefox 192.168.56.102/vnc/vnc.html")

				print done[0]
#Cirros OS
		elif mo=='4':

			os.system("dialog --inputbox \"Enter the RAM in mbs \" 40 40 2>/tmp/os.txt")

			ramm=open('/tmp/os.txt')

			rr=ramm.read()

			s.send(rr)

			os.system("dialog --inputbox \" Enter the no of cpu  \" 40 40 2>/tmp/os1.txt")

			cp=open('/tmp/os1.txt')

			cpuu=cp.read()

			s.send(cpuu)
	
			os.system("dialog --inputbox \"Enter HardDisk in GBs \" 40 40  2>/tmp/hd.txt")
 

			h=open('/tmp/hd.txt')

        		hd1=h.read()

       			s.send(hd1)

			portvnc=s.recv(10)

			os.system("dialog --msgbox 'Connect to the port no {}' 30 30 2>/tmp/lll.txt".format(portvnc))

			ok=s.recv(10)

			if ok=='done':
		

				done=commands.getstatusoutput("firefox 192.168.56.102/vnc/vnc.html")

				print done[0]

#Using QR code

	elif ko=='3':

		os.system("dialog --inputbox 'Enter the ID of the Instance to Start and view using QR code' 20 40 2>/tmp/ins.txt")

                si = open('/tmp/ins.txt')

                stain=si.read()

                s.send(stain)

		ok=s.recv(10)
		
		if ok=='done':
		
			#os.system("firefox 192.168.56.102/qr.html")

			os.system("dialog --msgbox 'use any qr code scanner' 30 30")
			os.system("firefox 192.168.56.102/{}.html".format(user))


					
#in Tiger VNC
	elif ko=='1':

	

		os.system("dialog --menu 'Choose Your Falour' 40 40 10 1 'Ubuntu' 2 'RedHat 7 ' 3 'MintOS' 4 'Cirros OS' 5 'Back' 6 'Exit' 2>/tmp/fla.txt")

		no=open('/tmp/fla.txt')

		mo=no.read()

		s.send(mo) 

		os.system("dialog --inputbox \"Enter the RAM in mbs \" 40 40 2>/tmp/os.txt")

		ramm=open('/tmp/os.txt')

		rr=ramm.read()

		s.send(rr)

		os.system("dialog --inputbox \" Enter the no of cpu  \" 40 40 2>/tmp/os1.txt")

		cp=open('/tmp/os1.txt')

		cpuu=cp.read()

		s.send(cpuu)
	
		os.system("dialog --inputbox \"Enter HardDisk in GBs \" 40 40  2>/tmp/hd.txt")
 

		h=open('/tmp/hd.txt')

        	hd1=h.read()

       		s.send(hd1)

		portos=s.recv(10)

		ok=s.recv(10)

		if ok=='done':
		

			done=commands.getstatusoutput("vncviewer 192.168.56.102:{}".format(portos))
			print done[0]
#In Android Mobile
	elif ko=='4':

	

		os.system("dialog --menu 'Choose Your Falour' 40 40 10 1 'Ubuntu' 2 'RedHat 7 ' 3 'MintOS' 4 'Cirros OS' 5 'Exit' 6 'Back' 2>/tmp/fla.txt")

		no=open('/tmp/fla.txt')

		mo=no.read()

		s.send(mo) 

		if mo=='1':

			os.system("dialog --inputbox \"Enter the RAM in mbs \" 40 40 2>/tmp/os.txt")


			ramm=open('/tmp/os.txt')

			rr=ramm.read()

			s.send(rr)

			os.system("dialog --inputbox \" Enter the no of cpu  \" 40 40 2>/tmp/os1.txt")

			cp=open('/tmp/os1.txt')

			cpuu=cp.read()

			s.send(cpuu)
	
			os.system("dialog --inputbox \"Enter HardDisk in GBs \" 40 40  2>/tmp/hd.txt")
 

			h=open('/tmp/hd.txt')

        		hd1=h.read()

       			s.send(hd1)

			ok=s.recv(10)

			if ok=='done':

				port=s.recv(20)
		

				os.system("dialog --msgbox 'Install VNC VIEWER app in your Mobile and type 192.168.43.135:{}' 30 30 ".format(port))
	


#MY Instances 

	elif ko=='5':
		
		no=s.recv(10)

		i=0
		
		out=[]
		
		while i<no:
			
			out.append(s.recv(10))
			os.system("dialog --msgbox 'Your instances are {}' 30 30".format(out))
			

	#Back

	elif ko=='6':

		menu.enter(s,user,passwd)
	#Shut Down an Instance

	elif ko=='8':

		os.system("dialog --inputbox 'Enter the ID of the Instance to shut Down' 20 40 2>/tmp/ins.txt")

		ins=open('/tmp/ins.txt')

		idd=ins.read()

		s.send(idd)

		s.recv(10)

		os.system("dialog --msgbox 'Your Instance has been Shut Down Successfully' 30 30 ")	

#delete an Instance
	elif ko=='9':
		os.system("dialog --inputbox 'Enter the ID of the Instance to Delete' 20 40 2>/tmp/ins.txt")
		
		ins = open('/tmp/ins.txt')
		
		ide=ins.read()
	
		s.send(ide)
		s.recv(10)
		
		
		os.system("dialog --msgbox 'Your Instance has been removed Successfully' 30 30 ")	
#Start An Instance
	elif ko=='10':
	
		os.system("dialog --inputbox 'Enter the ID of the Instance to Start' 20 40 2>/tmp/ins.txt")

                si = open('/tmp/ins.txt')

                stain=si.read()

                s.send(stain)
                

		portvnc=s.recv(10)

		os.system("dialog --msgbox 'Connect to the port no {}' 30 30 2>/tmp/lll.txt".format(portvnc))

		ok=s.recv(10)

		if ok=='done':

			done=commands.getstatusoutput("firefox 192.168.56.102/vnc/vnc.html")
	#OS Gallery

	elif ko=='11':

		os.system("dialog --inputbox 'Enter the no of OS to watch in the Gallery' 30 30 2>/tmp/gal.txt")
		no=open("/tmp/gal.txt")
		n=no.read()
		i=0
		portvnc=[]
		while i<n:
			os.system("dialog --inputbox 'Enter the Id of OS to watch in the Gallery' 30 30 2>/tmp/idos.txt")

			no1=open("/tmp/idos.txt")
                	n1=no1.read()
			s.send('{}'.format(n1))
			portvnc.append(s.recv(10))
			i=i+1
		s=""
		i=0
		while i<n:
			
			strn=strn+" 192.168.56.102/vnc/?ip='192.168.56.102'&port={}".format(portvnc[i])
			i=i+1


		os.system("firefox {}".format(strn))
