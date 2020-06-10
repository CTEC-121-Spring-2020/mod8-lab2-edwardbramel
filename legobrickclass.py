# legobrickclass.py
from graphics import *


class legobrick:
    # constructor
    def __init__(self, win, lowerleftcorner, length, color):
        self.win = win
        self.color = color
        self.lengthIN = length

        # create internal respresntation
        self.x = lowerleftcorner.getX()
        self.y = lowerleftcorner.getY()
        self.length = length * 7.5
        self.height = length * 2.5
        self.nibLen = length * .75
        self.nibHt = length * .3
        self.nibXOffset = length * .375
        self.nibYOffset = self.height
        self.myobjs = []

        # create brick body
        body = Rectangle(lowerleftcorner, Point(
            self.x+self.length, self.y+self.height))
        body.setOutline(3)
        self.myobjs.append(body)

        # create fist nib
        nib = Rectangle(Point(self.x + self.nibXOffset, self.y + self.height), Point(
            self.x + self.nibXOffset + self.nibLen, self.y + self.height + self.nibHt))
        nib.setWidth(3)
        self.myobjs.append(nib)

        # creat the rest of the nibs using cloning
        for i in range(1, 5):
            nibTemp = nib.clone()
            nibTemp.move(self.nibXOffset * 4 * i, 0)
            self.myobjs.append(nibTemp)

        # set fill color
        self.setfill(self.color)


def setFill(self, color):
    self.color = color
    for obj in self.myobjs:
        obj.setFill(color)


def draw(self, win):
    for obj in self.myobjs:
        obj.draw(win)


def clone(self):
    newbrick = legobrick(self.win, Point(self.x, self.y),
                         self.lengthIN, self.color)
    return newbrick


def move(self, XOffset, YOffset):
    for obj in self.myobjs:
        obj.move(XOffset, YOffset)


def main():
    win = GraphWin("lego Bricks", 500, 375)
    win.setCoords(0.0, 0.0, 20.0, 15.0)
    win.setBackground("light gray")

    brick1 = legobrick(win, Point(1, 1), 1, "blue")
    win.getMouse()

    brick2 = brick1.clone()
    brick2.setFill("black")
    brick2.move(8.5, 0)
    brick2.draw(win)


main()
