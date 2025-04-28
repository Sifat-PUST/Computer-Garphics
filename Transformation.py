import matplotlib.pyplot as plt
import numpy as np
def Transformation(x,y,dx,dy):
    xn=x+dx
    yn=y+dy
    return xn,yn

n=int(input("How many points? :"))
x,y=np.array([]),np.array([])


for i in range(n):
    print("Point "+str(i+1)+" :")
    k=int(input())
    l=int(input())
    x=np.append(x,k)
    y=np.append(y,l)
x=np.append(x,x[0])
y=np.append(y,y[0])
print("Enter Transformation Parameters :")
dx=int(input("dx:"))
dy=int(input("dy:"))
xn,yn=Transformation(x,y,dx,dy)

print(x)
print(y)
print(xn)
print(yn)

plt.subplot(1,2,1)
plt.plot(x, y)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(xn, yn )
plt.title('Plot 2')

plt.show()
