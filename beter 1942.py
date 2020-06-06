import turtle
import random
import sys
import os

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=500, height=600)
wn.bgcolor("lightblue")
wn.tracer(0)

path = os.getcwd()

pPlane = "{}/resources/plane.gif".format(path)
sEnemyplane = "{}/resources/senemyplane.gif".format(path)
bEnemyplane = "{}/resources/benemyplane.gif".format(path)

wn.addshape(pPlane)
wn.addshape(sEnemyplane)
wn.addshape(bEnemyplane)


player = turtle.Turtle()
player.speed(0)
player.shape(pPlane)
player.penup()
player.goto(0, -250)
player.direction = "stop"

sEnemies = []
pMissiles = []
eMissiles = []


for i in range(7):
    sEnemy = turtle.Turtle()
    sEnemy.speed(0)
    sEnemy.shape(sEnemyplane)
    sEnemy.penup()
    sEnemy.goto(random.randint(-220, 220), random.randint(200, 500))
    sEnemy.speed = 1
    sEnemy.setheading(270)
    sEnemies.append(sEnemy)


for i in range(3):
    pMissile = turtle.Turtle()
    pMissile.hideturtle()
    pMissile.speed(0)
    pMissile.color("yellow")
    pMissile.shape("square")
    pMissile.turtlesize(0.3)
    pMissile.penup()
    pMissile.speed = 3
    pMissile.state = "ready"
    pMissiles.append(pMissile)

for i in range(2):
    eMissile = turtle.Turtle()
    eMissile.hideturtle()
    eMissile.speed(0)
    eMissile.color("orange")
    eMissile.shape("square")
    eMissile.turtlesize(0.4)
    eMissile.penup()
    eMissile.speed = 2
    eMissile.state = "ready"
    eMissiles.append(eMissile)



bEnemy = turtle.Turtle()
bEnemy.speed(0)
bEnemy.shape(bEnemyplane)
bEnemy.turtlesize(3)
bEnemy.penup()
bEnemy.goto(random.randint(-250, 250), 250)
bEnemy.speed = 0.25
bEnemy.setheading(270)


def left():
    player.direction = "left"
    
def right():
    player.direction = "right"

def up():
    player.direction = "up"

def down():
    player.direction = "down"

def firepMissile():
    for pMissile in pMissiles:
        if pMissile.state == "ready":
            pMissile.setx(player.xcor())
            pMissile.sety(player.ycor() + 15)
            pMissile.showturtle()
            pMissile.state = "fire"
            break

def fireeMissile():
    for eMissile in eMissiles:
        if eMissile.state == "ready":
            eMissile.setx(bEnemy.xcor())
            eMissile.sety(bEnemy.ycor() - 30)
            eMissile.showturtle()
            eMissile.state = "fire"
            break
    
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(firepMissile, "space")



while True:
    wn.update()
    
    if player.direction == "left" and player.xcor() > -230:
        player.setx(player.xcor() - 0.6)
    
    elif player.direction == "right" and player.xcor() < 230:
        player.setx(player.xcor() + 0.6)
    
    elif player.direction == "up" and player.ycor() < 270:
        player.sety(player.ycor() + 0.6)
    
    elif player.direction == "down" and player.ycor() > -270:
        player.sety(player.ycor() - 0.6)

    for pMissile in pMissiles:
        if pMissile.state == "fire":
            pMissile.sety(pMissile.ycor() + 2)

        if pMissile.xcor() > 250 or pMissile.xcor() < -250 or pMissile.ycor() > 300 or pMissile.ycor() < -300:
            pMissile.hideturtle()
            pMissile.state = "ready"

    fireeMissile()

    for eMissile in eMissiles:
        if eMissile.state == "fire":
            eMissile.sety(eMissile.ycor() - 2)

        if eMissile.xcor() > 250 or eMissile.xcor() < -250 or eMissile.ycor() > 300 or eMissile.ycor() < -300:
            eMissile.hideturtle()
            eMissile.state = "ready"

    for sEnemy in sEnemies:    
        sEnemy.sety(sEnemy.ycor() - random.uniform(0.5, 1.3))
        sEnemy.setx(sEnemy.xcor() + random.uniform(-2, 2))
    
        if sEnemy.ycor() < -300:
            sEnemy.goto(random.randint(-300, 300), random.randint(400, 800))
    
        if player.distance(sEnemy) < 20:
            sys.exit(0)

        for pMissile in pMissiles:
            if pMissile.distance(sEnemy) < 10:
                sEnemy.hideturtle()
                sEnemy.goto(random.randint(-300, 300), random.randint(400, 800))
                sEnemy.showturtle()

                pMissile.goto(player.xcor(), player.ycor())
                pMissile.hideturtle()
                pMissile.state = "ready"
    
    bEnemy.sety(bEnemy.ycor() - 0.5)
    bEnemy.setx(bEnemy.xcor() + random.uniform(-1, 1))

    if bEnemy.ycor() < -300:
        bEnemy.goto(random.randint(-220, 220), random.randint(400, 800))

    for pMissile in pMissiles:
        if pMissile.distance(bEnemy) < 20:
            bEnemy.hideturtle()
            bEnemy.goto(random.randint(-300, 300), random.randint(400, 800))
            bEnemy.showturtle()

    for eMissile in eMissiles:
        if eMissile.distance(player) < 10:
            sys.exit(0)
    
    if player.distance(bEnemy) < 30:
            sys.exit(0)

 
    
        
            
    
        
        
        
        
