import matplotlib.pyplot as plt
import numpy as np
def Scalling(x,y,t,h,k):
    xn=(x-h)*np.cos(np.radians(t))-(y-k)*np.sin(np.radians(t))+h
    yn=(y-k)*np.cos(np.radians(t))+(x-h)*np.sin(np.radians(t))+k
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


print("Enter Angle of Rotation :")
t=int(input("Thita :"))
print('Enter Base point of Rotation :')
h=int(input('h :'))
k=int(input('k :'))

xn,yn=Scalling(x,y,t,h,k)

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
