#!/usr/bin/python2

import  cgi
import subprocess as sp

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')

#print(cname , imgname)

docker_launch_output = sp.getstatusoutput("sudo docker run -dit -p 29000:4200 --name  {c} {i}".format(c=cname, i=imgname))
print(docker_launch_output)
if docker_launch_output[0]  == 0:
	print("container named {c} launched ..".format(c=cname))
	print("<a href='docker-manage.py'>click here to manage Container</a>")
else:
	
	print("container named {c} failed ..".format(c=cname))






