import  matplotlib.pyplot as plt
def MidCircle(g,f,r):
    p=1-r
    x=r
    y=0

    x_points,y_points=[],[]

    i=0
    while y<=x:
        x_points.extend([x + g, -x+g , x+g ,-x+g,y+g,-y+g,y+g,-y+g])
        y_points.extend([y+f,y+f,-y+f,-y+f,x+f,x+f,-x+f,-x+f])

        y+=1
        if p<=0:
            x=x
            p=p+2*y+1
        else:
            x = x-1
            p = p + 2 * y - 2*x+ 1

    return x_points,y_points

print("Take g f and r :")
g=int(input())
f=int(input())
r=int(input())

x_coords,y_coords=MidCircle(g,f,r)

plt.scatter(x_coords,y_coords)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()