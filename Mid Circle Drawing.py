import  matplotlib.pyplot as plt

def MidCircle(g,f,r):
    p=1-r

    x=g+r
    y=0+f
    x_points,y_points=[x,-x,y,-y],[y,-y,x,-x]

    i=0
    while i<r:
        if p<=0:
            x=x
            y+=1
            p=p+2*y+1
            x_points.append(x)
            x_points.append(-x)
            x_points.append(y)
            x_points.append(-y)
            y_points.append(y)
            y_points.append(-y)
            y_points.append(x)
            y_points.append(-x)
        else:
            x = x-1
            y += 1
            p = p + 2 * y - 2*x+ 1
            x_points.append(x)
            x_points.append(-x)
            x_points.append(y)
            x_points.append(-y)
            y_points.append(y)
            y_points.append(-y)
            y_points.append(x)
            y_points.append(-x)

    return x_points,y_points

points=[]
print("Enter endpoints :")
for i in range(3):
    c=int(input())
    points.append(c)

g,f,r = points
x_coords,y_coords=MidCircle(g,f,r)

plt.plot(x_coords,y_coords)
plt.grid(True)
plt.show()