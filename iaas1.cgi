#!/usr/bin/python2

import  cgi,cgitb,os,commands,time,subprocess
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_select=web.getvalue('s')
os_Memory(GiB)=web.getvalue('m')
os_vCPUs=web.getvalue('v')
os_Size(GiB)=web.getvalue('s')
 
if os_select == "select":
	priny  os.system('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/hadoop2dnd.qcow2  /var/lib/libvirt/images/rh.qcow2')
	print os.system('sudo  virt-install  --select '+os_select+' --ram '+Memory(GiB)+'  --vcpu '+os_vCPUs+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2  --import  --noautoconsole')
