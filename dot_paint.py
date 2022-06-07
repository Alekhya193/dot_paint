

# angles=[0,90,180,270]
# titu.width(19)
#
# def walk():
#  titu.forward(40)
#  titu.setheading(random.choice(angles))
#
# for i in range(200):
#  titu.color(colour())
#  walk()

titu.speed("fastest")
def spiral():
 titu.circle(100)
 current_heading=titu.heading()
 titu.setheading(current_heading+5)


for i in range(100):
 titu.color(colour())
 spiral()


screen=Screen()
screen.exitonclick()
