# import turtle

# def createLSystem(numIters,axiom):
#     startString = axiom
#     endString = ""
#     for i in range(numIters):
#         endString = processString(startString)
#         startString = endString

#     return endString

# def processString(oldStr):
#     newstr = ""
#     for ch in oldStr:
#         newstr = newstr + applyRules(ch)

#     return newstr

# def applyRules(ch):
#     newstr = ""
#     if ch == 'F':
#         newstr = 'F-F++F-F'   # Rule 1
#     else:
#         newstr = ch    # no rules apply so keep the character

#     return newstr

# def drawLsystem(aTurtle, instructions, angle, distance):
#     for cmd in instructions:
#         if cmd == 'F':
#             aTurtle.forward(distance)
#         elif cmd == 'B':
#             aTurtle.backward(distance)
#         elif cmd == '+':
#             aTurtle.right(angle)
#         elif cmd == '-':
#             aTurtle.left(angle)

# def main():
#     inst = createLSystem(4, "F")   # create the string
#     print(inst)
#     t = turtle.Turtle()            # create the turtle
#     wn = turtle.Screen()

#     t.up()
#     t.back(200)
#     t.down()
#     t.speed(9)
#     drawLsystem(t, inst, 60, 5)   # draw the picture
#                                   # angle 60, segment length 5
#     wn.exitonclick()

# main()

from tridecagonTurtle import tridecagonTurlte
import turtle
import random

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        return   'FFT+F+F+P'
    else:
        return ch
    
def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'T':
            tridecagonTurlte(30, aTurtle.xcor(), aTurtle.ycor (),aTurtle)
        elif cmd == 'P':
            X = random.randint(-250,250)
            Y = random.randint(-250,250)
            aTurtle.penup()
            aTurtle.goto(X,Y)
            aTurtle.pendown()
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(4, "F")   
    print(inst)
    t = turtle.Turtle()            
    wn = turtle.Screen()

    t.up()
    t.back(50)
    t.down()
    t.speed(9)
    drawLsystem(t,inst,60,30)   
                                  

main()
