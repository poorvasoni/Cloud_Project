#!/usr/bin/python2
import os,sys,time,commands

os.system("dialog --infobox \"CLOUD SERVICES\" 20 30")
time.sleep(2)
os.system("dialog --msgbox \"Click OK to Continue....\" 20 40")

os.system("dialog --inputbox \" Enter your User Name \" 20 30 2>/tmp/user.txt")
