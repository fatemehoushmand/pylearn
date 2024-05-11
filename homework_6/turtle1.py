import turtle
p = turtle.Pen()
p.shape("turtle")

j=30
h=15

for side in range(6,20):
    degree = ((side-2)*180)/side
    p.left(180-(degree/2))
 
    j=j+12
    h+=4
    for i in range(side):
        p.forward(j)
        p.left(180-degree)
    p.right(180-(degree/2))
    p.penup()
    p.forward(h)
    p.down()

turtle.done()


