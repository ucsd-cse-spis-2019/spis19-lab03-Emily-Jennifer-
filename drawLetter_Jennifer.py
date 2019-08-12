#Jennifer - This program draws my first initial, J. For realz this time.
import turtle

def drawJ(theTurtle):

    """Draws J in another window, taking a turtle as the input """
    theTurtle.pensize(10)
    theTurtle.color("green")

    theTurtle.pendown()
    theTurtle.right(90)
    theTurtle.forward(200)
    theTurtle.circle(-60, 180)  # draw a semicircle
    theTurtle.penup()

#Creating a turtle to do our dirty work
turtwig=turtle.Turtle()
drawJ(turtwig)

torterra=turtle.Turtle()
torterra.penup()
torterra.setpos(-300,-200)
drawJ(torterra)
