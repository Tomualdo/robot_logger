import re
from mpl_toolkits import mplot3d
import numpy as np
from numpy  import array
import matplotlib.pyplot as plt
with open("/home/tom/Projects/proface/robotFiles/mainQl02/20200429/0001.JOB") as fjob:
    job = fjob.read()
#print (job)
x=[]
y=[]
z=[]
for line in job.splitlines():
    if(line.startswith("S")):
        doRegex = re.search ("\(([-0-9]+.[0-9]+),([-0-9]+.[0-9]+),([-0-9]+.[0-9]+)",line)
        print ("X: ",doRegex.group(1),"Y: ",doRegex.group(2),"Z: ",doRegex.group(3))
        x.append(float(doRegex.group(1)))
        y.append(float(doRegex.group(2)))
        z.append(float(doRegex.group(3)))

print ("x: ",x,"y: ",y,"z: ",z)
x=array(x)
y=array(y)
z=array(z)
print ("x: ",x,"y: ",y,"z: ",z)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'gray')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
