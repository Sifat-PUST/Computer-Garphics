import matplotlib.pyplot as plt
points=[]
print("Enter endpoints :")
for i in range(4):
    x=int(input())
    points.append(x)

x1,y1,x2,y2=points
steps=max(abs(y2-y1),abs(x2-x1))
x_points=[]
y_points=[]



x,y=x1,y1

for i in range(steps):
    x_points.append(x)
    y_points.append(y)

    m = (y2 - y) / (x2 - x)

    if(m<=1):
        x=x+1
        y=round(y+m)
    else:
        x=round(x+(1/m))
        y=y+1

print(x_points,y_points)

plt.plot(x_points,y_points)
plt.show()