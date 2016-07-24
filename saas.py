#!/usr/bin/python2
import os,sys,time,commands

def begin(s,user,passwd):
	os.system("dialog --menu \"Choose an Option\"  20 40 10 1 \"FIREFOX\n\" 2 \"VLC media Player\n\" 3 \"GEDIT\n\" 4 \"VNC Viewer\n\" 5 \"Music Player\n\" 6 \"WebCam\" 7 \"KVM(virtual machine)\" 8 \"Other\" 9 \" Back\" 10 \" Exit \" 2>/tmp/choice.txt")

        ob=open('/tmp/choice.txt')

        c=ob.read()


#firefox

        if c=='1':
		s.send(c)
		username=s.recv(10)
		
                ok=commands.getstatusoutput(" sshpass -p {} ssh -X -l {} 192.168.56.102".format(passwd,username))
		print ok[0]
		if ok[0]==0:
			s.send("firefox")
			os.system('dialog --infobox "Successfully Firefox has been shared " 20 20')
		else:
			os.system('dialog --infobox "Sorry Some error has occured " 20 20') 
		


#VLC		
		
        elif c=='2':
                ok1=commands.getstatusoutput("sshpass -p {} ssh -X  {}@192.168.56.102 vlc".format(passwd,user))
		print ok1[0]
		if ok1[0]==0:
			s.send("vlc")
			os.system('dialog --infobox "Successfully VLC MEDIA has been shared " 20 20')
                else:
                        os.system('dialog --infobox "Sorry Some error has occured " 20 20')

#GEDIT
        elif c=='3':
                ok2=commands.getstatusoutput("sshpass -p {} ssh -X  {}@192.168.56.102 gedit".format(passwd,user))
                print ok2[0]
                if ok2[0]==0:
                        s.send("gedit")
                        os.system('dialog --infobox "Successfully GEDIT has been shared " 20 20')
			begin(s,user,passwd)
			
                else:
                        os.system('dialog --infobox "Sorry Some error has occured " 20 20')
			begin(s,user,passwd)
		
#vnc viewer
        elif c=='4':
                execfile("saas.py")


        elif c=='5':
                execfile("naas.py")

	elif c=='6':
		menu.enter(s,user,passwd)


        else:
                os.system("dialog --infobox \"Wrong Input\" 10 10")
		begin(s,user,passwd)    
