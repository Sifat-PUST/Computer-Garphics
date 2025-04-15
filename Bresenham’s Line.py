import  matplotlib.pyplot as plt

def Bresenham(x1,y1,x2,y2):
    steps=max(abs(x2-x1),abs(y2-y1))
    p=2*(y2-y1)-(x2-x1)

    x_points,y_points=[x1],[y1]

    for i in range(steps+1):
        if p<0:
            x1+=1
            y1=y1
            p=p+2*(y2-y1)
            x_points.append(x1)
            y_points.append(y1)
        else:
            x1+=1
            y1+=1
            p=p+2*(y2-y1)-2*(x2-x1)
            x_points.append(x1)
            y_points.append(y1)

    return x_points,y_points

points=[]
print("Enter endpoints :")
for i in range(4):
    x=int(input())
    points.append(x)

x1, y1, x2, y2 = points
x_coords,y_coords=Bresenham(x1, y1, x2, y2)

plt.plot(x_coords,y_coords)
plt.grid(True)
plt.show()