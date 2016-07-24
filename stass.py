#!/usr/bin/python2

import os,sys,time,commands,menu
def begin(s,user,passwd):
	os.system("dialog --menu \"Choose any Option\" 40 40 10 1 \"Want an Object Storage\" 2 \"Want a Block Storage\" 3 \"Want to extend previous storage\" 4 \"Want to remove a storage \" 5 \"To Take Snapshot\" 6 \"To watch your partitions till date \" 7 \"Exit\" 8 'Back'  2>/tmp/choi.txt")

	ch=open('/tmp/choi.txt')

	mc=ch.read()
   	print "coming here"
	s.send(mc)
	print "coming here"
#OBJECT STORAGE
	
	if mc=='1':
		os.system('dialog --menu "Please choose the protocol" 30 30 8 1 "NFS Protocol" 2 "SSHFS Protocol" 3 "In Mobile" 4 "SAMBA Protocol" 2>/tmp/serv.txt')
		se=open("/tmp/serv.txt")
		sd=se.read()
		s.send(sd)
#NFS Protocol
		if sd=='1':
			os.system("dialog --inputbox \" Enter the size use 'K' for kb 'M' for mb 'G' for gb \" 40 40 2>/tmp/size.txt")
			su=open('/tmp/size.txt')
			hd=su.read()
			s.send(hd)
			done=s.recv(10)
			print done
			if done=="done":
			
				os.system("mkdir /media/{}".format(user))
				os.system("mount 192.168.56.102:/media/{} /media/{}".format(user,user))
		
		
				os.system('dialog --msgbox "Successsfully the Given Size Storage has been Shared" 10 40 ')

				
				
			else:
				os.system('dialog --msgbox "Sorry an error has Occured" 10 40 ')

# SSHFS Protocol

		elif sd=='2':
			os.system("dialog --inputbox \" Enter the size use 'K' for kb 'M' for mb 'G' for gb \" 40 40 2>/tmp/size.txt")
                        su=open('/tmp/size.txt')
                        hd=su.read()
                        s.send(hd)
                        done=s.recv(10)
                        print done
	#Successful from server Side
                        if done=="done":
				y=commands.getstatusoutput("mkdir /media/{}sshfs".format(user))
				print y[0]
				y1=commands.getstatusoutput("sshpass -p {} sshfs {}@192.168.56.102:/media/{}sshfs /media/{}sshfs".format(passwd,user,user,user))
				print y1[0]

#Successful or not
				if y[0]==y1[0]:
					os.system('dialog --msgbox "Successsfully the Given Size Storage has been Shared" 10 40 ')
					menu.enter(s,user,passwd)
				else:
					os.system('dialog --msgbox "Sorry an error has Occured" 10 40 ')

#IN MObile Protocol
		elif sd=='3':
			
			os.system("dialog --inputbox \" Enter the size use 'K' for kb 'M' for mb 'G' for gb \" 40 40 2>/tmp/size.txt")

			os.system("dialog --inputbox \" Enter your Email Id \" 40 40 2>/tmp/size2.txt")
                        su=open('/tmp/size.txt')
                        hd=su.read()
                        s.send(hd)
                        done=s.recv(10)
                        print done
        #Successful from server Side
                        if done=="done":
				

#Successful or not
                                
				os.system('dialog --infobox "Successsfully the Given Size Storage has been Shared" 10 40 ')
				tims.sleep(5)
				os.system('dialog --infobox "Please Check your Email For further actions" 30 30 ')

#SAMBA Protocol
		elif sd=='4':

			os.system("dialog --inputbox 'Enter the size of the storage use M for mbs K for kbs and G for gbs' 40 40  2>/tmp/samba.txt")

			sam=open('/tmp/samba.txt')
                        samba=sam.read()
                        s.send(samba)

			done=s.recv(10)
			print done
			if done=='done':
				os.system("mkdir /media/{}samba".format(user))

				os.system("mount -o username={}samba //192.168.56.102/{} /media/{}samba".format(user,user,user))

				os.system('dialog --msgbox "Given Sized Storage Has Been Shared Successfully" 10 40 ') 

		else:
			os.system('dialog --msgbox "Sorry an error has Occured" 10 40 ')
				
				 	
			 	
#BLOCK STORAGE	

	elif mc=='2':
		os.system("dialog --inputbox \" Enter the size use 'K' for kb 'M' for mb 'G' for gb \" 40 40 2>/tmp/size1.txt")
		bs=open('/tmp/size1.txt')
		block=bs.read()
		s.send(block)
		done=s.recv(10)
		print done
		
		if done=="done":
			os.system("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.56.102 --discover")
			


			
			os.system("iscsiadm --mode node --targetname {}block --portal 192.168.56.102:3260 --login".format(user))
			

			
			os.system('dialog --infobox "Successsfully the Given Size Storage has been Shared" 10 40 ')
	
				

		else:
			os.system('dialog --msgbox "Sorry an error has Occured" 10 40 ')

#EXTEND PREVIOUS STORAGE

	elif mc=='3':
		os.system("dialog --inputbox \" Enter the name of the exixting partition \" 40 40 2>/tmp/name.txt")
                name=open('/tmp/name.txt')
                pname=name.read()
		print pname
                s.send(pname)
		
		
		os.system("dialog --inputbox \" Enter the size to extend use 'K' for kb 'M' for mb 'G' for gb \" 40 40 2>/tmp/size1.txt")
                size=open('/tmp/size1.txt')
                psize=size.read()
                s.send(psize)
		print psize

                done=s.recv(10)


		if done=='done':
			os.system('dialog --msgbox "Successfully extended the partition" 10 40')
		else:
			os.system('dialog --msgbox "Please Enter Valid Partition Name" 10 40')

#REMOVE PARTOTION
	elif mc=='4':
		os.system("dialog --inputbox \" Enter the name of the Object Storage  Partition \" 40 40 2>/tmp/size3.txt")
                su=open('/tmp/size3.txt')
                hd=su.read()
		
		full=commands.getstatusoutput("umount /media/{}".format(hd))
		print full[0]

		full1=commands.getstatusoutput("rmdir /media/{}".format(hd))
		print full1[0]


                s.send(hd)

		
		
		done=s.recv(10)
		print done
		if done=="done":
                	os.system('dialog --infobox "Successfully removed the partition" 10 40 ')

#To take the Snapshot
	elif mc=='5':
		os.system("dialog --inputbox \" Enter the name of the storage to take SnapShot \" 40 40 2>/tmp/snap.txt")

		snap=open('/tmp/snap.txt')

		ss=snap.read()

		s.send(ss)

		done=s.recv(10)
		if done=='done':
		
			os.system("mkdir /media/{}sd".format(ss))
			os.system("mount 192.168.56.102:/media/{}sd /media/{}sd".format(ss,ss))

			
			os.system('dialog --msgbox "Successsfully the Snapshot has been Shared" 10 40 ')
			
			

		
#Back
		
	elif mc=='8':

		menu.enter(s,user,passwd)
#ELSE PART
	else:
		os.system('dialog --infobox "Wrong Choice Please Select again" 10 30')
		begin(s,user,passwd)

