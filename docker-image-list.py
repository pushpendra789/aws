#!/usr/bin/python36

import subprocess as sp

print("content-type: text/html")
print("")

print("<b>")
print("<body bgcolor='#E3E4FA'>")
print("<marquee hspace=10 vspace=10 height=40><font> CONTAINER AS A SERVICE</font></marquee>")
print("</b>")
print("<center>")
print("<h2><u>AVAILABLE DOCKER IMAGES</u></h2>")
print("<pre>")
print("<h3>")
dockerImageList = sp.getoutput("sudo docker images")
print(dockerImageList)
print("</h3>")
print("</pre>")
print("<h4>Launch Single Containers</h4><br/>")
print("</center>")
dockerimage = dockerImageList.split("\n")






print("""
<form action='CAAS-launch.py'>
<table align="center" width='80%' border='1'>
<tr>
<td>Enter ur container name :</td> 
<td><input name='cname' /></td>
</tr>

<tr>
<td>Enter ur image name :</td> 
<td>

<select name='imgname'>

""")


for i in dockerimage[1:] :
	print("<option>")
	j = i.split()
	print(j[0] + ":"  +  j[1])
	print("</option>")


print("""
</select>

</td>
</tr>

<tr>
<td><input type='submit' /></td> 
<td><input type='reset' /></td>
</tr>

</table>
</form>
""")

print("<br></br>")
print("<marquee hspace=10 vspace=10 height=40><font>MULTIPLE CONTAINER AS A SERVICE</font></marquee>")
print("<br></br>")

print("<center>")

print("<h2><u>Launch Multiple Containers</u></h2><br/>")

print("</center>")

print("<form action='mcontainer-launch.py'>")
print("<select name='image'>")
for i in dockerimage[1:] :
        print("<option>")
        j = i.split()
        print(j[0] + ":"  +  j[1])
        print("</option>")
print("</select>")
print("""
      Enter the Number : <input name='n' />
      Unique Id: <input name='id' />
      <input type='submit' value='start' />      
      """)

print("</form>")


