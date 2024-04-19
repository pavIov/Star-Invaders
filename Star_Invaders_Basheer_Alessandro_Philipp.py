#import needed libraries  
import turtle
from turtle import *
import time
import random
import math

#Define constants
RIGHT_EDGE = 640
LEFT_EDGE = -640
BOTTOM_EDGE = -360
TOP_EDGE = 360
BALL_SPEED = 5
SDshapesize = 1
AWshapesize = 1
XWshapesize = 1
YWshapesize = 1
LGshapesize = 1
LRshapesize = 1
Score=0

starDestroyer="Star Wars SpaceIn Assets/Sdestroyer.gif"
aWing="Star Wars SpaceIn Assets/Awing.gif"
xWing="Star Wars SpaceIn Assets/Xwing.gif"
yWing="Star Wars SpaceIn Assets/Ywing.gif"
lazerG="Star Wars SpaceIn Assets/GreenLaser.gif"
lazerR="Star Wars SpaceIn Assets/RedLaser.gif"
#Global variables
screen = Screen()
screen.title("Space Invaders")
screen.bgpic("Star Wars SpaceIn Assets/galaxy 2 Large.png")
screen.setup(1280,720)
#Adding images
screen.addshape(starDestroyer)
screen.addshape(aWing)
screen.addshape(xWing)
screen.addshape(yWing)
screen.addshape(lazerG)
screen.addshape(lazerR)



ywingList1=[]
ywingList2=[]
xwingList1=[]
xwingList2=[]
awingList=[]
lazerRList=[]

#spawning enemies
for y1 in range (0,11):
    ywingList1.append(Turtle())
    ywingList1[y1].clear()
    ywingList1[y1].penup()

    ywingList1[y1].shape(yWing)
    ywingList1[y1].shapesize(YWshapesize)
    ywingList1[y1].position()
    ywingList1[y1].speed(0)
    ywingList1[y1].sety(0)
    ywingList1[y1].setheading(0)

for y2 in range (0,11):
    ywingList2.append(Turtle())
    ywingList2[y2].clear()
    ywingList2[y2].penup()

    ywingList2[y2].shape(yWing)
    ywingList2[y2].shapesize(YWshapesize)
    ywingList2[y2].position()
    ywingList2[y2].speed(0)
    ywingList2[y2].sety(0)
    ywingList2[y2].setheading(0)


for x1 in range (0,11):
    xwingList1.append(Turtle())
    xwingList1[x1].clear()
    xwingList1[x1].penup()

    xwingList1[x1].shape(xWing)
    xwingList1[x1].shapesize(XWshapesize)
    xwingList1[x1].position()
    xwingList1[x1].speed(0)
    xwingList1[x1].sety(0)
    xwingList1[x1].setheading(0)

for x2 in range (0,11):
    xwingList2.append(Turtle())
    xwingList2[x2].clear()
    xwingList2[x2].penup()

    xwingList2[x2].shape(xWing)
    xwingList2[x2].shapesize(XWshapesize)
    xwingList2[x2].position()
    xwingList2[x2].speed(0)
    xwingList2[x2].sety(0)
    xwingList2[x2].setheading(0)


for a in range (0,11):
    awingList.append(Turtle())
    awingList[a].clear()
    awingList[a].penup()

    awingList[a].shape(aWing)
    awingList[a].shapesize(AWshapesize)
    awingList[a].position()
    awingList[a].speed(0)
    awingList[a].sety(0)
    awingList[a].setheading(0)


##for r in range (0,55):
##    lazerRList.append(Turtle())
##    lazerRList[r].clear()
##    lazerRList[r].penup()
##
##    lazerRList[r].shape(lazerR)
##    lazerRList[r].shapesize(LRshapesize)
##    lazerRList[r].position()
##    lazerRList[r].speed(0)
##    lazerRList[r].sety(0)
##    lazerRList[r].setheading(90)
##    lazerRList[r].hideturtle()

#Functions
#moving player
def move_right():
    print(star_dstry.xcor())
    if star_dstry.xcor() <= RIGHT_EDGE:
        star_dstry.forward(5)
    else:
        star_dstry.backward(15)
    return


def move_left():
    print(star_dstry.xcor())
    if star_dstry.xcor() >= LEFT_EDGE:
        star_dstry.backward(5)
    else:
        star_dstry.forward(15)
    return
#shooting Lazer (see approximately lines 470-480 for more info)
def shoot_lazerG():
    global lazer, lazer_in_progress

    #they pressed space so create a new player laser
    # to where the players ship is
    #set laser_in_progress to True

    #lazer.goto(star_dstry.xcor(), star_dstry.ycor())
    lazer_in_progress = True

    return

##def shoot_lazerR():
##    global lazerRList
##    for r in range(0,55):
##        lazerRList[r].penup()
##        lazerRList[r].speed(0)
##        lazerRList[r].setheading(90)
##        lazerRList[r].showturtle()
##    
##        while lazerRList[r].ycor() > BOTTOM_EDGE:
##            lazerRList[r].backward(10)
##        lazerRList[r].hideturtle()
##    return

#locations for ships
def shipstuff():

  #A-Wing Locations
    awingList[0].goto(-450,330)
    awingList[1].goto(-360,330)
    awingList[2].goto(-270,330)
    awingList[3].goto(-180,330)
    awingList[4].goto(-90,330)
    awingList[5].goto(0,330)
    awingList[6].goto(90,330)
    awingList[7].goto(180,330)
    awingList[8].goto(270,330)
    awingList[9].goto(360,330)
    awingList[10].goto(450,330)

    #X-Wing Locations
    xwingList1[0].goto(-450,264)
    xwingList1[1].goto(-360,264)
    xwingList1[2].goto(-270,264)
    xwingList1[3].goto(-180,264)
    xwingList1[4].goto(-90,264)
    xwingList1[5].goto(0,264)
    xwingList1[6].goto(90,264)
    xwingList1[7].goto(180,264)
    xwingList1[8].goto(270,264)
    xwingList1[9].goto(360,264)
    xwingList1[10].goto(450,264)

    xwingList2[0].goto(-450,198)
    xwingList2[1].goto(-360,198)
    xwingList2[2].goto(-270,198)
    xwingList2[3].goto(-180,198)
    xwingList2[4].goto(-90,198)
    xwingList2[5].goto(0,198)
    xwingList2[6].goto(90,198)
    xwingList2[7].goto(180,198)
    xwingList2[8].goto(270,198)
    xwingList2[9].goto(360,198)
    xwingList2[10].goto(450,198)

    #Y-Wing Locations
    ywingList1[0].goto(-450,132)
    ywingList1[1].goto(-360,132)
    ywingList1[2].goto(-270,132)
    ywingList1[3].goto(-180,132)
    ywingList1[4].goto(-90,132)
    ywingList1[5].goto(0,132)
    ywingList1[6].goto(90,132)
    ywingList1[7].goto(180,132)
    ywingList1[8].goto(270,132)
    ywingList1[9].goto(360,132)
    ywingList1[10].goto(450,132)

    ywingList2[0].goto(-450,66)
    ywingList2[1].goto(-360,66)
    ywingList2[2].goto(-270,66)
    ywingList2[3].goto(-180,66)
    ywingList2[4].goto(-90,66)
    ywingList2[5].goto(0,66)
    ywingList2[6].goto(90,66)
    ywingList2[7].goto(180,66)
    ywingList2[8].goto(270,66)
    ywingList2[9].goto(360,66)
    ywingList2[10].goto(450,66)

    # red lazer locations
##    lazerRList[0].goto(-450,330)
##    lazerRList[1].goto(-360,330)
##    lazerRList[2].goto(-270,330)
##    lazerRList[3].goto(-180,330)
##    lazerRList[4].goto(-90,330)
##    lazerRList[5].goto(0,330)
##    lazerRList[6].goto(90,330)
##    lazerRList[7].goto(180,330)
##    lazerRList[8].goto(270,330)
##    lazerRList[9].goto(360,330)
##    lazerRList[10].goto(450,330)
##    lazerRList[11].goto(-450,264)
##    lazerRList[12].goto(-360,264)
##    lazerRList[13].goto(-270,264)
##    lazerRList[14].goto(-180,264)
##    lazerRList[15].goto(-90,264)
##    lazerRList[16].goto(0,264)
##    lazerRList[17].goto(90,264)
##    lazerRList[18].goto(180,264)
##    lazerRList[19].goto(270,264)
##    lazerRList[20].goto(360,264)
##    lazerRList[21].goto(450,264)
##    lazerRList[22].goto(-450,198)
##    lazerRList[23].goto(-360,198)
##    lazerRList[24].goto(-270,198)
##    lazerRList[25].goto(-180,198)
##    lazerRList[26].goto(-90,198)
##    lazerRList[27].goto(0,198)
##    lazerRList[28].goto(90,198)
##    lazerRList[29].goto(180,198)
##    lazerRList[30].goto(270,198)
##    lazerRList[31].goto(360,198)
##    lazerRList[32].goto(450,198)
##    lazerRList[33].goto(-450,132)
##    lazerRList[34].goto(-360,132)
##    lazerRList[35].goto(-270,132)
##    lazerRList[36].goto(-180,132)
##    lazerRList[37].goto(-90,132)
##    lazerRList[38].goto(0,132)
##    lazerRList[39].goto(90,132)
##    lazerRList[40].goto(180,132)
##    lazerRList[41].goto(270,132)
##    lazerRList[42].goto(360,132)
##    lazerRList[43].goto(450,132)
##    lazerRList[44].goto(-450,66)
##    lazerRList[45].goto(-360,66)
##    lazerRList[46].goto(-270,66)
##    lazerRList[47].goto(-180,66)
##    lazerRList[48].goto(-90,66)
##    lazerRList[49].goto(0,66)
##    lazerRList[50].goto(90,66)
##    lazerRList[51].goto(180,66)
##    lazerRList[52].goto(270,66)
##    lazerRList[53].goto(360,66)
##    lazerRList[54].goto(450,66)

    return

#Collisions for enemies
# A wing collisions
def check_Awing():
    global hit,LGy,Score,AWy,AWx,LGx,lazer_in_progress,W

    if (LGy!=AWy):
        return
    else:
        hit=False
        for currentShip in range(0,len(awingList)):
            Left=awingList[currentShip].xcor()-W/2
            Right=Left+W
            if (LGx<=Right)and(LGx>=Left):
                hit=True
                awingList[currentShip].hideturtle()
                lazer_in_progress=False
                awingList.remove(awingList[currentShip])
                Score=Score+20 #added score; increases if you hit a ship
                print("Score: ",Score)
                return
#Y wing collisions
def check_Ywing1():
    global hit,LGy,Score,YWy1,YWx1,LGx,lazer_in_progress,W

    if (LGy!=YWy1):
        return
    else:
        hit=False
        for currentShip in range(0,len(ywingList1)):
            Left=ywingList1[currentShip].xcor()-W/2
            Right=Left+W
            if (LGx<=Right)and(LGx>=Left):
                hit=True
                ywingList1[currentShip].hideturtle()
                lazer_in_progress=False
                ywingList1.remove(ywingList1[currentShip])
                Score=Score+10 #added score; increases if you hit a ship
                print("Score: ",Score)
                return

def check_Ywing2():
    global hit,LGy,Score,YWy2,YWx2,LGx,lazer_in_progress,W

    if (LGy!=YWy2):
        return
    else:
        hit=False
        for currentShip in range(0,len(ywingList2)):
            Left=ywingList2[currentShip].xcor()-W/2
            Right=Left+W
            if (LGx<=Right)and(LGx>=Left):
                hit=True
                ywingList2[currentShip].hideturtle()
                lazer_in_progress=False
                ywingList2.remove(ywingList2[currentShip])
                Score=Score+10 #added score; increases if you hit a ship
                print("Score: ",Score)
                return

#X wing collisions
def check_Xwing1():
    global hit,LGy,Score,XWy1,XWx1,LGx,lazer_in_progress,W

    if (LGy!=XWy1):
        return
    else:
        hit=False
        for currentShip in range(0,len(xwingList1)):
            Left=xwingList1[currentShip].xcor()-W/2
            Right=Left+W
            if (LGx<=Right)and(LGx>=Left):
                hit=True
                xwingList1[currentShip].hideturtle()
                lazer_in_progress=False
                xwingList1.remove(xwingList1[currentShip])
                Score=Score+15 #added score; increases if you hit a ship
                print("Score: ",Score)

def check_Xwing2():
    global hit,LGy,Score,XWy2,XWx2,LGx,lazer_in_progress,W

    if (LGy!=XWy2):
        return
    else:
        hit=False
        for currentShip in range(0,len(xwingList2)):
            Left=xwingList2[currentShip].xcor()-W/2
            Right=Left+W
            if (LGx<=Right)and(LGx>=Left):
                hit=True
                xwingList2[currentShip].hideturtle()
                lazer_in_progress=False
                xwingList2.remove(xwingList2[currentShip])
                Score=Score+15 #added score; increases if you hit a ship
                print("Score: ",Score)

##def shooting_lazerR():
##
##    while True:
##        shootsec=random.randint(1,5)
##        time.sleep(shootsec)
##        shoot_lazerR()
##
##    return

# spawning star destroyer 
star_dstry = Turtle()
star_dstry.clear()
star_dstry.penup()

star_dstry.shape(starDestroyer)
star_dstry.shapesize(SDshapesize)
star_dstry.position()
star_dstry.speed(0)
star_dstry.sety(0)
star_dstry.setheading(0)
star_dstry.goto(0,-180)

# spawning lazer
lazer = Turtle()
lazer.clear()
lazer.penup()

lazer.shape(lazerG)
lazer.position()
lazer.speed(0)
lazer.sety(0)
lazer.setheading(90)
lazer.goto(0,-180)
lazer.hideturtle()

# calling movement 
listen()
shipstuff()
onkey(move_right,"d")
onkey(move_left,"a")
onkey(shoot_lazerG,"space")
lazer_in_progress = False

# defining enemie's corrdinates
for a in range(0,11):
    AWx=awingList[a].xcor()
    AWy=awingList[a].ycor()
for x1 in range(0,11):
    XWx1=xwingList1[x1].xcor()
    XWy1=xwingList1[x1].ycor()
for x2 in range(0,11):
    XWx2=xwingList2[x2].xcor()
    XWy2=xwingList2[x2].ycor()
for y1 in range(0,11):
    YWx1=ywingList1[y1].xcor()
    YWy1=ywingList1[y1].ycor()
for y2 in range(0,11):
    YWx2=ywingList2[y2].xcor()
    YWy2=ywingList2[y2].ycor()
G=90
W=12

#MAIN GAME LOOP ###
while True:
    SDx=star_dstry.xcor()
    SDy=star_dstry.ycor()
    LGx=lazer.xcor()
    LGy=lazer.ycor()

    if (lazer_in_progress==True)and(LGy<=TOP_EDGE):
        #move the laser
        lazer.penup()
        lazer.speed(0)
        lazer.showturtle()
        lazer.forward(6)
        #if laser is above screen, then set laser_in_progress to False
        check_Ywing1()
        check_Ywing2()
        check_Xwing1()
        check_Xwing2()
        check_Awing()
    else:
        lazer.setx(star_dstry.xcor())
        lazer.sety(star_dstry.ycor())
        lazer.hideturtle()
        lazer_in_progress=False
    #shooting_lazerR()
    screen.update()
