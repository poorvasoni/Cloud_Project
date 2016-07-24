
def enter(s,user,passwd):
	import os,time,sys,stass,saas,paas,caas,iaas,home

	
	os.system("dialog --menu \"Choose an Option\"  20 40 10 1 \"Storage As Services\n\" 2 \"Infrastructure As Service\n\" 3 \"Platform as Service\n\" 4 \"Software as a Service\n\" 5 \"Container as a Service\n\" 6 \"Network as a Service\" 7 \"Exit\" 8 \"Delete Account\" 9 \" Logout \" 10 'Back'  2>/tmp/choice.txt")

	ob=open('/tmp/choice.txt')

	c=ob.read()
	s.send(c)

	if c=='1':
		stass.begin(s,user,passwd)
		
	elif c=='2':
		iaas.begin(s,user,passwd)
	elif c=='3':
		paas.begin(s,user,passwd)	
	elif c=='4':
		saas.begin(s,user,passwd)
	elif c=='5':
		caas.begin(s,user,passwd)
	elif c=='6':
		fdas.begin(s,user,passwd)
	elif c=='7':
		s.close()
	elif c=='8':

		done=s.recv(10)
	
		if done=='done':
			os.system("dialog --infobox 'Thanks for using our Services Successfully your account has been removed' 30 30")
			time.sleep(5)
			s.close()

	elif c=='9':

		home.welcome(s)

	elif c=='10':

		home.welcome(s)



    
