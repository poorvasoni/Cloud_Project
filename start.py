#!/usr/bin/python2

import os,sys,time,commands,socket,home

s=socket.socket()
ip="192.168.56.102"
port=4444

s.connect((ip,port))

os.system("dialog --infobox \" ##POORVA CLOUD SERVICES##                                    Welcome to our cloud services ... Here you will get some extra ordinary services which you have never thought of  .... Take your business to the new level and it will be our pleasure to help you in this...... :-) :-)      as our moto is #####DO GOOD AND HAVE GOOD##### :-) :-) \" 20 30")
time.sleep(2)



home.welcome(s)
