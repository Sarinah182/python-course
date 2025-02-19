import turtle 
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,300)
polygon=turtle.Turtle ()
numsides=6 
side_length=70
angle=360/numsides 
for i in range (numsides) :
    polygon.forward (side_length)
    polygon.right (angle)
turtle.done ()