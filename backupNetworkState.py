import time
import pexpect
#This script iterates through each host in text file and performs some commands on each of them. 
#Reading a file containing one host per line.

#Creating command for foldername to be created with current date and time. 
path='/tmp/backup/'
time=time.strftime("%Y%m%d%H%M%S")
foldername=path+time
mkdir='mkdir '
commandmkdir=mkdir+foldername
#Reading all lines from text file and storing in list x
f = open('hostList.txt', 'r') 
x = f.readlines()
ssh_newkey = 'Are you sure you want to continue connecting'
password = '/chicago/'
commands=[commandmkdir,'cd %s' %foldername,'ip route show >> iprouteshow.txt','ifconfig -a >>ifconfig.txt','netstat -topn >>netstat.txt','netstat -ulpn >>netstat.txt','netstat -gn>>netstat.txt']
count=0
for host in x:
 print host
 p = pexpect.spawn ('ssh root@%s' %host)
 i=p.expect([ssh_newkey,'assword:',pexpect.EOF])
 if i==0:
    p.sendline('yes')
    i=p.expect([ssh_newkey,'assword:',pexpect.EOF])
 if i==1:
    p.sendline(password)
    i=p.expect('#')
 if i==0:
    print "login successful"
    count=count+1
    for command in commands:
     p.sendline(command)
     print "command executed"
     p.expect('#')
print "Summary:\nTotal hosts:%d" %len(x)
print "Successful Backup:%d" %count
