#!/usr/bin/python2
import os,time,sys

os.system("dialog --menu \"Choose an Option\"  20 40 10 1 \"Storage As Services\n\" 2 \"Infrastructure As Service\n\" 3 \"Platform as Service\n\" 4 \"Software as a Service\n\" 5 \"Network as a Service\n\" 2>/tmp/choice.txt")

ob=open('choice.txt')

c=ob.read()

if c=='1':
	execfile("stass.py")
elif c=='2':
	execfile("iaas.py")
elif c=='3':
	execfile("paas.py")
elif c=='4':
	execfile("saas.py")
elif c=='5':
	execfile("naas.py")
else:
	os.system("dialog --infobox \"Wrong Input\" 10 10")



    
