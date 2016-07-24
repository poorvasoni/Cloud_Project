#!/usr/bin/python2

def begin(s,user,passwd):
	
	import os,commands,time,menu
	os.system('dialog --menu "Choose the Protocol" 30 30 5 1 "SSh" 2 "Samba" 3 "Want to Share a file" 4 "Exit"  2>/tmp/option.txt')
	
	sh=open("/tmp/option.txt")
	share=sh.read(10)

	s.send(share)
#SCP Directory Share	
	if share=='1':
		pass
#Samba Sharing
	elif share=='2':
		pass
#file Sharing

	elif share=='3':
		pass

#exit
	else:
		menu.enter(s,user,passwd)
		
		 
