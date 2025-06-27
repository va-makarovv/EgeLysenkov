from turtle import *
#22591

screensize(2000,2000)
k = 30
lt(90)
down()
tracer(0)
for i in range(4):
    fd(k*50)
    lt(90)
up()
fd(k*50)
lt(135)
down()

for i in range(2):
    fd(k*102)
    lt(120)
    fd(k*182)
    lt(60)

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3,"green")
update()
done()