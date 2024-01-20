import turtle
import random
import sys
import os
from time import sleep

#get current path
path = os.getcwd()

#define variables
sEnemies = []
pMissiles = []
eMissiles = []
score = 0
bEnemylives = 3
gOver = False

#set up window
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=500, height=600)
wn.bgpic("{}/resources/bg.gif".format(path))
wn.tracer(0)

#get path to textures
pPlane = "{}/resources/plane.gif".format(path)
sEnemyplane = "{}/resources/senemyplane.gif".format(path)
bEnemyplane = "{}/resources/benemyplane.gif".format(path)
pMissilepic = "{}/resources/playermissile.gif".format(path)
eMissilepic = "{}/resources/enemymissile.gif".format(path)

#add textures
wn.addshape(pPlane)
wn.addshape(sEnemyplane)
wn.addshape(bEnemyplane)
wn.addshape(pMissilepic)
wn.addshape(eMissilepic)


#set up writing pen and write the score
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.setpos(0, 270)
pen.write("Score: " + str(score), move=False, align="center", font=("Comic Sans MS", 12)) 

#player turtle
player = turtle.Turtle()
player.shape(pPlane)
player.penup()
player.goto(0, -250)
player.direction = "stop"

#small enemy turtles
for i in range(7):
    sEnemy = turtle.Turtle()
    sEnemy.shape(sEnemyplane)
    sEnemy.penup()
    sEnemy.goto(random.randint(-220, 220), random.randint(200, 500))
    sEnemy.speed = 1
    sEnemy.setheading(270)
    sEnemies.append(sEnemy)


#player missiles 
for i in range(3):
    pMissile = turtle.Turtle()
    pMissile.penup()
    pMissile.setpos(1000, 1000)
    pMissile.shape(pMissilepic)
    pMissile.turtlesize(0.3)
    pMissile.state = "ready"
    pMissiles.append(pMissile)

#enemy missiles
for i in range(3):
    eMissile = turtle.Turtle()
    eMissile.hideturtle()
    eMissile.color("orange")
    eMissile.shape(eMissilepic)
    eMissile.turtlesize(0.4)
    eMissile.penup()
    eMissile.state = "ready"
    eMissiles.append(eMissile)

#big enemy turtle
bEnemy = turtle.Turtle()
bEnemy.shape(bEnemyplane)
bEnemy.turtlesize(3)
bEnemy.penup()
bEnemy.setpos(random.randint(-220, 220), 250)
bEnemy.setheading(270)

#player directions
def left():
    player.direction = "left"
    
def right():
    player.direction = "right"

def up():
    player.direction = "up"

def down():
    player.direction = "down"

#fire player missile if ready
def firepMissile():
    for pMissile in pMissiles:
        if pMissile.state == "ready":
            pMissile.setx(player.xcor())
            pMissile.sety(player.ycor() + 15)
            pMissile.showturtle()
            pMissile.state = "fire"
            break

#fire enemy missile if ready
def fireeMissile():
    for eMissile in eMissiles:
        if eMissile.state == "ready":
            eMissile.setx(bEnemy.xcor())
            eMissile.sety(bEnemy.ycor() - 30)
            eMissile.showturtle()
            eMissile.state = "fire"
            break


#listen for keystrokes
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(firepMissile, "space")

#mainloop
while True:
    wn.update() #update the window

    #move the player 
    if player.direction == "left" and player.xcor() > -230:
        player.setx(player.xcor() - 0.7)
    
    elif player.direction == "right" and player.xcor() < 230:
        player.setx(player.xcor() + 0.7)
    
    elif player.direction == "up" and player.ycor() < 270:
        player.sety(player.ycor() + 0.7)
    
    elif player.direction == "down" and player.ycor() > -270:
        player.sety(player.ycor() - 0.7)

    #move player missile and remove it if it is off the screen
    for pMissile in pMissiles:
        if pMissile.state == "fire":
            pMissile.sety(pMissile.ycor() + 2)

        if pMissile.xcor() > 250 or pMissile.xcor() < -250 or pMissile.ycor() > 300 or pMissile.ycor() < -300:
            pMissile.hideturtle()
            pMissile.setpos(1000, 1000) #move missile out of the way of the game
            pMissile.state = "ready"

    #fire enemy missike
    fireeMissile()

    #move enemy missile and remove it if it is off the screen
    for eMissile in eMissiles:
        if eMissile.state == "fire":
            eMissile.sety(eMissile.ycor() - 2.5)

        if eMissile.xcor() > 250 or eMissile.xcor() < -250 or eMissile.ycor() > 300 or eMissile.ycor() < -300:
            eMissile.hideturtle()
            eMissile.state = "ready"

    #move small enemies, go to the top if they are off the screen
    for sEnemy in sEnemies:    
        sEnemy.sety(sEnemy.ycor() - random.uniform(0.5, 1.3))
        sEnemy.setx(sEnemy.xcor() + random.uniform(-2, 2))
    
        if sEnemy.ycor() < -300:
            sEnemy.goto(random.randint(-300, 300), random.randint(400, 800))

        if player.distance(sEnemy) < 25: #check for collisions between player and small enemy
            gOver = True
            
        #check for collision between player missiles and small enemies
        for pMissile in pMissiles:
            if pMissile.distance(sEnemy) < 10:
                sEnemy.hideturtle()
                sEnemy.goto(random.randint(-250, 250), random.randint(400, 800))
                sEnemy.showturtle()
                score += 10
                pen.clear()
                pen.write("Score: " + str(score), move=False, align="center", font=("Comic Sans MS", 12)) 
                

                pMissile.setpos(1000, 1000) #move missile out of the way of the game
                pMissile.hideturtle()
                pMissile.state = "ready"
    
    #move big enemy 
    bEnemy.sety(bEnemy.ycor() - 0.25)
    bEnemy.setx(bEnemy.xcor() + random.uniform(-1, 1))

    if player.distance(bEnemy) < 40: #check for collisions between player and big enemy
        gOver = True
            
    #move big enemy to the top if it goes off the screen and reset its lives 
    if bEnemy.ycor() < -300:
        bEnemy.goto(random.randint(-220, 220), random.randint(400, 800))
        bEnemylives = 3

    #check for collision between player missiles and big enemy
    for pMissile in pMissiles:
        if pMissile.distance(bEnemy) < 35:
            bEnemylives -= 1 #remove a life if there has been a collosion 
            print(bEnemylives)
            if bEnemylives > 0: 
                pass
            else: #kill the enemy if it out of lives and reset it 
                bEnemy.hideturtle()
                bEnemy.goto(random.randint(-300, 300), random.randint(400, 800))
                bEnemy.showturtle()
                bEnemylives = 3
                print(bEnemylives)
                score += 30
                pen.clear()
                pen.write("Score: " + str(score), move=False, align="center", font=("Comic Sans MS", 12))
                print(score)
            
            pMissile.setpos(1000, 1000) #move missile out of the way of the game
            pMissile.hideturtle()
            pMissile.state = "ready"

    for eMissile in eMissiles:
        if eMissile.distance(player) < 10: #check for collisions between player and enemy missiles
            gOver = True

    if gOver: #if game is over display game over screen and reset everything
        pen.setpos(0, 0)
        pen.write("Game Over!", move=False, align="center", font=("Comic Sans MS", 24))
        pen.setpos(0, -25)
        pen.write("Your Score Was: " + str(score), move=False, align="center", font=("Comic Sans MS", 16))
        pen.setpos(0, 0)

        bEnemy.setpos(random.randint(-220, 220), 250)
        for sEnemy in sEnemies:
            sEnemy.goto(random.randint(-300, 300), random.randint(400, 800))

        for eMissile in eMissiles:
            eMissile.setpos(1000, 1000)

        for pMissile in pMissiles:
            pMissile.setpos(1000, 100)
        
        player.direction = "stop"
        player.goto(0, -250)
        
        sleep(2)
        score = 0
        pen.clear()
        pen.setpos(0, 270)
        pen.write("Score: " + str(score), move=False, align="center", font=("Comic Sans MS", 12)) 
        gOver = False
        

      

    
    

 
    
        
            
    
        
        
        
        
