import turtle

size_big = 10
sizes = 5

pet = turtle.Pen()
pet.shape("turtle")

pet.width(3)
pet.left(150)

for i in range(3, 12):
    hight = (((i - 2) * 180) / i) - 180
    
    for j in range(i):
        pet.forward(41 + size_big)
        pet.right(hight)
    
    pet.right(110)
    pet.forward(12.5 + sizes)
    pet.left(110)
    size_big += 15
    sizes += 5



turtle.done()
