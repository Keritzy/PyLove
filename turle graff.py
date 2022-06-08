import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")
frame = turtle.Turtle()
frame.color("blue")

def sqrfunc(size):
    for x in range(10):
        frame.fd(size)
        frame.left(50)
        size = size + 6

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
sqrfunc(166)
sqrfunc(186)
sqrfunc(206)
sqrfunc(226)
sqrfunc(246)
sqrfunc(266)
sqrfunc(286)
sqrfunc(306)
sqrfunc(326)
sqrfunc(346)
sqrfunc(366)
sqrfunc(386)
