#!/usr/bin/python2
import os,sys,time,commands

os.system("dialog --infobox \"CLOUD SERVICES\" 20 30")
time.sleep(2)





os.system("dialog --msgbox \"Click Ok to continue....\" 20 40")
	
os.system("dialog --menu \"LOGIN or SIGN UP\" 20 20 2 1 \"Login\" 2 \"Sine Up\" 2>/tmp/choise.txt")
fo=open('/tmp/choise.txt')
c=fo.read()
	
if c=='1':
	os.system("dialog --inputbox \" Enter your User Name \" 20 30 2>/tmp/user.txt")

	os.system("dialog --insecure --passwordbox \" Enter your Password \" 20 30 2>/tmp/pass.txt")
	ob=open('/tmp/user.txt')

	user=ob.read()

	ob1=open('/tmp/pass.txt')

	passwd=ob1.read()

	if user=='vimal' and passwd=='lw':
		execfile('menu.py')
	
elif c=='2':

	os.system("dialog --inputbox \" Enter your User Name \" 20 30 2>/tmp/user1.txt")

	os.system("dialog --insecure --passwordbox \" Enter your Password \" 20 30 2>/tmp/pass1.txt")

	os.system("dialog --insecure --passwordbox \"Retype Password \" 20 30 2>/tmp/pass2.txt")	
else:
	os.system("dialog --infobox \"Wrong Choise\" 20 30")
		
