#1. A turtle you can control without declaring a turtle object
#2. turtle is the library and Turtle() is a constructor for the turtle object
#3. myTurtle.sety(100)

#Draws the letter E with 2 turtles
import turtle

def drawE(theTurtle, posX, posY, size):
    '''Draw the letter E with specified x position, y position, and size using a turtle'''
    
    theTurtle.color("red")
    theTurtle.pensize(size)

    theTurtle.setx(posX)
    theTurtle.sety(posY)

    theTurtle.pendown()

    rightLine(theTurtle)
    downLine(theTurtle)
    rightLine(theTurtle)
    downLine(theTurtle)
    theTurtle.forward(200)

    theTurtle.penup()

def rightLine(theTurtle):
    '''Draws a right line using a turtle'''
    theTurtle.forward(200)
    theTurtle.right(180)
    theTurtle.forward(200)

def downLine(theTurtle):
    '''Draws a line down using a turtle'''
    theTurtle.right(270)
    theTurtle.forward(200)
    theTurtle.right(270)


myTurtle1 = turtle.Turtle()
myTurtle2 = turtle.Turtle()

drawE(myTurtle1, 0, 0, 15)

myTurtle2.penup()


drawE(myTurtle2, -300, 100, 10)
