#!/usr/bin/python
def welcome(s):
	import os,commands,time,menu

	os.system("dialog --msgbox \"Click Ok to continue....\" 20 40")
	
	os.system("dialog --menu \"LOGIN or SIGN UP\" 20 20 2 1 \"Login\" 2 \"Register\" 2>/tmp/choise.txt")
	fo=open('/tmp/choise.txt')
	ch=fo.read()

	s.send(ch)
	
	if ch=='1':
		os.system("dialog --inputbox \" Enter your User Name \" 20 30 2>/tmp/user.txt")
	
		os.system("dialog --insecure --passwordbox \" Enter your Password \" 20 30 2>/tmp/pass.txt")
		ob=open('/tmp/user.txt')

		user=ob.read()
		s.send(user)
		ob1=open('/tmp/pass.txt')

		passwd=ob1.read()
		s.send(passwd)
		
		done=s.recv(10)


		

		if done=='done':

			#while True:
			menu.enter(s,user,passwd)
		else:
			os.system('dialog --infobox  "Wrong user Name or Password" 30 30 2>/tmp/kk.txt')
			welcome(s)

			
	elif ch=='2':
		def input():
			os.system("dialog --inputbox \" Enter your User Name \" 20 30 2>/tmp/user1.txt")
			ob=open('/tmp/user1.txt')
			user=ob.read()
			
			os.system("dialog --insecure --passwordbox \" Enter your Password \" 20 30 2>/tmp/pass1.txt")
			ob1=open('/tmp/pass1.txt')
			pas1=ob1.read()
			os.system("dialog --insecure --passwordbox \"Retype Password \" 20 30 2>/tmp/pass2.txt")	
			ob2=open('/tmp/pass2.txt')
			pas=ob2.read()
			if pas1!=pas:
				os.system("dialog --infobox \"Password does not match\" 20 30")
				time.sleep(5)
				input()
			else:
				s.send(user)
				s.send(pas1)
				done=s.recv(10)
				print done
				if done=="done":
					os.system("dialog --msgbox \"You have successfully got the ticket to enter  in the magiacal world now press ok to Enter....\" 20 40")
					welcome(s)
		input()						
		

