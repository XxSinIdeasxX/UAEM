#Space Invaders
#python 2.7.12 on Mac
# Thanks to Christian Thompson 
# Python Game Programming Tutorial: Space Invaders
# http://christianthompson.com/

import turtle
import os
import math
import random
import time
import sys

#Set up the screen
turtle.setup(805,700,None,0)
win = turtle.Screen()
win.bgcolor("black")
win.title("Invasores espaciales")
win.bgpic("space_invaders_background.gif")

#Register the graphics for the game
turtle.register_shape("invader0_0.gif")
turtle.register_shape("invader0_1.gif")

turtle.register_shape("invader1_0.gif")
turtle.register_shape("invader1_1.gif")
turtle.register_shape("invader1_2.gif")

turtle.register_shape("invader2_0.gif")
turtle.register_shape("invader2_1.gif")
turtle.register_shape("invader2_2.gif")
turtle.register_shape("invader2_3.gif")

turtle.register_shape("invader3_0.gif")
turtle.register_shape("invader3_1.gif")
turtle.register_shape("invader3_2.gif")
turtle.register_shape("invader3_3.gif")
turtle.register_shape("invader3_4.gif")

turtle.register_shape("player0.gif")
turtle.register_shape("fondo.gif")
turtle.register_shape("controles.gif")
turtle.register_shape("final1.gif")
turtle.register_shape("final2.gif")
turtle.register_shape("vida.gif")
turtle.register_shape("carga.gif")
turtle.register_shape("ultra_ready.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("super.gif")
turtle.register_shape("ultra.gif")
turtle.register_shape("blast.gif")

#                 Pantalla
#   -355_|__________800_________|_355
#      |                     °°°  |-310
#      |                      °°  |-275
#      |                          |
#    700                          |
#      |                          |
#      |                          |_ -270
#      |                          |_ -250
#       TTTTTTTTTTTTTTTTTTTTTTTTTT

turtle.tracer(0,0)

teclas = [0,0,0,0,0,0,0,0,0]
#  left-right-space-up-down-enter-esc-V-C
#    0    1     2    3   4    5    6  7 8

def tecla(pos,val):
  teclas[pos] = val

_tick2_frame=0
_tick2_fps=20000000 # real raw FPS
_tick2_t0=time.time()

tiempoAnterior = time.time()
tiempoActual = time.time()
deltaTime = tiempoActual-tiempoAnterior

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-379,-328)
border_pen.pensize(3)
border_pen.pendown()
for side in range(2):
  border_pen.fd(757)
  border_pen.lt(90)
  border_pen.fd(657)
  border_pen.lt(90)
border_pen.hideturtle()

score_pen = turtle.Turtle()
player = turtle.Turtle()
bullet = turtle.Turtle()
canon = turtle.Turtle()
ultra = turtle.Turtle()
#blast = turtle.Turtle()

playerspeed = 300
bulletstate = "ready"
canonstate = "ready"
ultrastate = "ready"
bulletspeed = 1000
blastspeed = 200
aum_enemyspeed = 0.018
nivel=1
jugando=False
score = 0
score_segura=0
cont_cargas = 0
cont_cargas_segura = 0
pt_carga=50
cont_ultra = 0
cont_ultra_segura = 0
pt_ultra=150
nivel_ganar=5

cargas=[]
life=[]

#Create the player turtle
player.color("blue")
player.shape("player0.gif")
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)

#Create the player's bullet
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.goto(player.xcor(),player.ycor())
bullet.hideturtle()

#Bala super
canon.color("blue")
canon.shape("super.gif")
canon.speed(0)
canon.penup()
canon.setheading(90)
canon.goto(player.xcor(),player.ycor())
canon.hideturtle()

#Bala ultra
ultra.color("purple")
ultra.shape("ultra.gif")
ultra.speed(0)
ultra.penup()
ultra.setheading(90)
ultra.goto(player.xcor(),player.ycor())
ultra.hideturtle()


#Create an empty list of enemies
enemiesList =[]

def iniciarJuego(n):  
  global enemyspeed
  enemyspeed=2

  global vidas
  if n>3:
    n=3
  vidas=n

  #Draw the score on stage
  score_pen.speed(0)
  score_pen.color("white")
  score_pen.penup()
  score_pen.setposition(-370,295)
  scorestring = "Score: %s" %score
  score_pen.write(scorestring, False, align="left", font = ("Space Invaders", 14, "bold"))
  score_pen.hideturtle()

  player.showturtle()

  #Add enemies to the list
  #We need to create more turtle objects

  #Creacion de enemigos y posiciones iniciales por cada nivel
  if nivel==1:
    for i in range(10):
      #             objeto - tipo - reapariciones
      enemiesList.append([turtle.Turtle(),0,1])

    mapa=[]
    for i in range(5):
      mapa.append([0]*7)
    for i,enemy in enumerate (enemiesList):
      while True:
        y = random.randint(0,4)
        x = random.randint(-3, 3)
        
        if mapa[y][x+3]==0:
          mapa[y][x+3]=1
          y = y*55
          x = x*60
          enemy[0].shape("invader0_1.gif")
          enemy[0].speed(0)
          enemy[0].penup()
          enemy[0].setposition(x, y)
          #print(i,x,",",y)
          break
 
  if nivel==2:
    for i in range(8):
      enemiesList.append([turtle.Turtle(),1,2])
      #   [0] objeto - [1] tipo - [2] reapariciones
    for i in range(8):
      enemiesList.append([turtle.Turtle(),0,1])
  
    for i, enemy in enumerate(enemiesList):
      if enemy[1]==0:
        enemy[0].shape("invader0_1.gif")
        x=210-60*(i-8)
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 110)
        
      elif enemy[1]==1:
        enemy[0].shape("invader1_2.gif")
        x=-210+60*i
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 220)

  if nivel==3:
    for i in range(6):
      enemiesList.append([turtle.Turtle(),0,1])
    
    for i in range(6):
      enemiesList.append([turtle.Turtle(),1,2])
      #   [0] objeto - [1] tipo - [2] reapariciones
  
    for i in range(4):
      enemiesList.append([turtle.Turtle(),2,3,"null",turtle.Turtle()])
      #   [0] objeto - [1] tipo - [2] reapariciones - [3] blast

    for i, enemy in enumerate(enemiesList):
      if enemy[1]==0:
        enemy[0].shape("invader0_1.gif")
        x=200-80*i
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 80)
        
      elif enemy[1]==1:
        enemy[0].shape("invader1_2.gif")
        x=200-80*(i-6)
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 150)

      elif enemy[1]==2:
        enemy[0].shape("invader2_3.gif")
        x=195-130*(i-12)
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 220)

        #Bala enemiga 'Blast'
        enemy[4].shape("blast.gif")
        enemy[4].speed(0)
        enemy[4].penup()
        enemy[4].setheading(90)
        enemy[4].goto(enemy[0].xcor(),enemy[0].ycor())

      #print(i,x,",",enemy[0].ycor())
  
  if nivel==4:
    global nodrisaspeed
    nodrisaspeed=150
    for i in range(3):
      enemiesList.append([turtle.Turtle(),3,4,i])
      #   [0] objeto - [1] tipo - [2] reapariciones - [3] clave de nodrisa

    for i, enemy in enumerate(enemiesList):
      if enemy[1]==3:
        enemy[0].shape("invader3_4.gif")
        x=-200+200*i
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 190)
        for j in range(3):
          enemiesList.append([turtle.Turtle(),1,2,i])
          #Los enemigos de la nave tienen la [3] clave de la nave
          enemiesList[-1][0].shape("invader1_2.gif")
          x=random.randint(-200+140*i,-220+140*(i+1))
          enemiesList[-1][0].speed(0)
          enemiesList[-1][0].penup()
          enemiesList[-1][0].setposition(x, 110-70*j)
    for i in range (len(enemiesList)):
      print(enemiesList[i])

  if nivel==5:
    nodrisaspeed=150
    for i in range(3):
      enemiesList.append([turtle.Turtle(),3,4,i])
      #   [0] objeto - [1] tipo - [2] reapariciones - [3] clave de nodrisa

    for i, enemy in enumerate(enemiesList):
      if enemy[1]==3:
        enemy[0].shape("invader3_4.gif")
        x=-200+200*i
        enemy[0].speed(0)
        enemy[0].penup()
        enemy[0].setposition(x, 190)
      
        enemiesList.append([turtle.Turtle(),2,3,i,turtle.Turtle()])
        #Los enemigos de la nave tienen la [3] clave de la nave
        enemiesList[-1][0].shape("invader2_3.gif")
        x=random.randint(-200+140*i,-220+140*(i+1))
        enemiesList[-1][0].speed(0)
        enemiesList[-1][0].penup()
        enemiesList[-1][0].setposition(x, 110)
        #Bala enemiga 'Blast'
        enemiesList[-1][4].shape("blast.gif")
        enemiesList[-1][4].speed(0)
        enemiesList[-1][4].penup()
        enemiesList[-1][4].setheading(90)
        enemiesList[-1][4].goto(enemy[0].xcor(),enemy[0].ycor())

        enemiesList.append([turtle.Turtle(),1,2,i])
        #Los enemigos de la nave tienen la [3] clave de la nave
        enemiesList[-1][0].shape("invader1_2.gif")
        x=random.randint(-200+140*i,-220+140*(i+1))
        enemiesList[-1][0].speed(0)
        enemiesList[-1][0].penup()
        enemiesList[-1][0].setposition(x, 40)

        enemiesList.append([turtle.Turtle(),0,1,i])
        #Los enemigos de la nave tienen la [3] clave de la nave
        enemiesList[-1][0].shape("invader0_1.gif")
        x=random.randint(-200+140*i,-220+140*(i+1))
        enemiesList[-1][0].speed(0)
        enemiesList[-1][0].penup()
        enemiesList[-1][0].setposition(x, -30)

  for i in range (vidas):
    life.append(turtle.Turtle())
    life[-1].color("green")
    life[-1].shape("vida.gif")
    life[-1].speed(0)
    life[-1].penup()
    life[-1].setposition(360-(i*30), 310)
    life[-1].setheading(90)


#Move the player 
def move_left():
  global player
  x = player.xcor()
  x = x - playerspeed*(deltaTime)
  if x < -350:
    x = -350
  player.setx(x)
def move_right():
  x = player.xcor()
  x = x + playerspeed*deltaTime
  if x > 350:
    x = 350
  player.setx(x)
def move_up():
  y = player.ycor()
  y = y + playerspeed*deltaTime
  if y > 10:
    y = 10
  player.sety(y)
def move_down():
  y = player.ycor()
  y = y - playerspeed*deltaTime
  if y < -270:
    y = -270
  player.sety(y)

def fire_bullet():
  #Declare bulletstate as a global if it needs change
  global bulletstate
  if bulletstate == "ready":
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x,y+5)
    bullet.showturtle()
    bulletstate = "fire"

def fire_canon():
  global canonstate
  if canonstate == "ready":
    cargas[-1].ht()
    cargas.pop(-1)
    x = player.xcor()
    y = player.ycor()
    canon.setposition(x,y+5)
    canon.showturtle()
    canonstate = "fire"

def fire_ultra():
  global ultrastate
  if ultrastate == "ready":
    x = player.xcor()
    y = player.ycor()
    ultra.setposition(x,y+5)
    ultra.showturtle()
    ultrastate = "fire"


def isCollision(t1,t2,d):
  distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
  if distance <= d:
    return True
  else:
    return False

#create keyboard bindings
turtle.listen()

turtle.onkeypress(lambda: tecla(0,1), "Left")
turtle.onkeypress(lambda: tecla(1,1), "Right")
turtle.onkeypress(lambda: tecla(2,1), "space")
turtle.onkeypress(lambda: tecla(3,1), "Up")
turtle.onkeypress(lambda: tecla(4,1), "Down")
turtle.onkeypress(lambda: tecla(5,1), "Return")
turtle.onkeypress(lambda: tecla(6,1), "Escape")
turtle.onkeypress(lambda: tecla(7,1), "v")
turtle.onkeypress(lambda: tecla(8,1), "c")

turtle.onkeyrelease(lambda: tecla(0,0), "Left")
turtle.onkeyrelease(lambda: tecla(1,0), "Right")
turtle.onkeyrelease(lambda: tecla(2,0), "space")
turtle.onkeyrelease(lambda: tecla(3,0), "Up")
turtle.onkeyrelease(lambda: tecla(4,0), "Down")
turtle.onkeyrelease(lambda: tecla(5,0), "Return")
turtle.onkeyrelease(lambda: tecla(6,0), "Escape")
turtle.onkeyrelease(lambda: tecla(7,0), "v")
turtle.onkeyrelease(lambda: tecla(8,0), "c")

def tick(fps=60):
 global _tick2_frame,_tick2_fps,_tick2_t0
 n=_tick2_fps/fps
 _tick2_frame+=n
 while n>0: n-=1
 if time.time()-_tick2_t0>1:
  _tick2_t0=time.time()
  _tick2_fps=_tick2_frame
  _tick2_frame=0

imgInicio = turtle.Turtle() 
imgInicio.color("blue")
imgInicio.shape("fondo.gif")
imgInicio.penup()
imgInicio.setposition(0, 0)

#Loop de inicio
while True:
  turtle.update()
  tick(60) #1 frame per second
  if teclas[2] == 1:
    break
imgInicio.hideturtle() 

imgControl = turtle.Turtle() 
imgControl.color("blue")
imgControl.shape("controles.gif")
imgControl.penup()
imgControl.setposition(0, 0)

#Loop de controles
while True:
  turtle.update()
  tick(60) #1 frame per second
  if teclas[5] == 1:
    break
imgControl.hideturtle() 

#                         Main game loop
#==============================================================
jugando=True
iniciarJuego(nivel)

ultraReady = turtle.Turtle() 
ultraReady.color("purple")
ultraReady.shape("ultra_ready.gif")
ultraReady.penup()
ultraReady.setposition(0, 280)
ultraReady.hideturtle()

while True:
  turtle.update()
  tick(60)
  tiempoAnterior = tiempoActual
  tiempoActual = time.time()
  deltaTime = tiempoActual-tiempoAnterior

  #movimiento del jugador y disparos
  if jugando:
    if teclas[0] == 1:
      move_left()
    if teclas[1] == 1:
      move_right()
    if teclas[2] == 1:
      fire_bullet()
    if (teclas[7]==1) and len(cargas)!=0:
      fire_canon()
    if teclas[8]==1 and ultraReady.isvisible():
      fire_ultra()
      ultraReady.hideturtle()
      cont_ultra=0
      cont_cargas_segura=0
  if jugando and nivel>2:
    if teclas[3] == 1:
      move_up()
    if teclas[4] == 1:
      move_down()

  for indice, enemy in enumerate(enemiesList):
    #print(indice, enemy[0].xcor(),",",enemy[0].ycor())
    #This is a forever loop
    #Move the enemy

    if enemy[1]!=3:
      x = enemy[0].xcor()
      x = x + enemyspeed
      enemy[0].setx(x)

      #Move enemy back and down
      if enemy[0].xcor() > 355:
        enemy[0].setx(355)
        enemyspeed*=-1
        for e in (enemiesList):
          if e[1]!=3:
            y=e[0].ycor()
            y = y - 55
            e[0].sety(y)

      if enemy[0].xcor() < -355:
        enemy[0].setx(-355)
        enemyspeed*=-1
        for e in (enemiesList):
          if e[1]!=3:
            y=e[0].ycor()
            y = y - 55
            e[0].sety(y)
    else:
      if enemy[1]==3:
        x = enemy[0].xcor()
        x = x + nodrisaspeed*deltaTime
        enemy[0].setx(x)

        if enemy[0].xcor() > 345:
          enemy[0].setx(345)
          nodrisaspeed*=-1
        if enemy[0].xcor() < -345:
          enemy[0].setx(-345)
          nodrisaspeed*=-1
   
    #Movimiento y colisiones entre las balas enemigas
    blastCollision=False
    if enemy[1]==2:
      if isCollision(player, enemy[4],20):
        blastCollision=True
     
      y=enemy[4].ycor()
      y=y-blastspeed*deltaTime
      enemy[4].sety(y)
      if enemy[4].ycor()<-270:
        enemy[4].penup()
        enemy[4].setposition(enemy[0].xcor(),enemy[0].ycor()-10)

    #Check for collision between enemy and player
    #o que el enemigo llego a la Tierra
    if isCollision(player, enemy[0],35) or (enemy[0].ycor()<-235) or blastCollision:
      
      if cont_ultra_segura<pt_ultra:
        ultraReady.ht()
      ultra.ht()
      canon.ht()
      bullet.ht()

      for i in range (len(cargas)):
        cargas[0].ht()
        cargas.pop(0)

      cont_cargas=score_segura
      while cont_cargas>pt_carga:
        cont_cargas-=pt_carga

      for i in range (cont_cargas_segura):
        cargas.append(turtle.Turtle())
        cargas[-1].color("blue")
        cargas[-1].shape("carga.gif")
        cargas[-1].speed(0)
        cargas[-1].penup()
        if len(cargas)==1:
          cargas[-1].setposition(360,275)
        else:
          cargas[-1].setposition(360-((len(cargas)-1) *16), 275)

      vidas-=1
      for i in range(len(life)):
        life[0].hideturtle()
        life.pop(0)

      while len(enemiesList)!=0:
        enemiesList[0][0].hideturtle()
        if enemiesList[0][1]==2:
          enemiesList[0][4].ht()
        enemiesList.pop(0)
      if vidas==0:
        jugando=False
        break
      score = score_segura
      cont_ultra=cont_ultra_segura
      score_pen.clear()
      player.reset()
      player.clear()
      player.penup()
      player.setposition(0,-240)
      player.hideturtle()
      iniciarJuego(vidas)
      break
    
    ultraCollision=False
    canonCollision=False
    bulletCollision=False
    if enemy[1]==3:
      if isCollision(ultra,enemy[0],50):
        ultraCollision=True 
      if isCollision(canon,enemy[0],45):
        canonCollision=True 
      if isCollision(bullet,enemy[0],40):
        bulletCollision=True 

    if isCollision(ultra, enemy[0],37) or ultraCollision:

      if enemyspeed>0:
        enemyspeed+=aum_enemyspeed
      elif enemyspeed<0:
        enemyspeed-=aum_enemyspeed

      #Update the score
      if enemy[1]==0:
        score += 10
        cont_cargas += 10
        cont_ultra += 10
      elif enemy[1]==1:
        score += 20
        cont_cargas += 20
        cont_ultra += 20
      elif enemy[1]==2:
        score += 30
        cont_cargas += 30
        cont_ultra += 30
        enemy[4].ht()
      elif enemy[1]==3:
        score += 40
        cont_cargas += 40
        cont_ultra += 40
      scorestring = "Score: %s" %score
      score_pen.clear()
      score_pen.write(scorestring, False, align="left", font = ("Space Invaders", 14, "bold"))
      
      if nivel<4:
        enemy[0].ht()
        enemiesList.pop(indice)
      else:
        if enemy[1]==3:
          clave=enemy[3]
          noLimpio=True
          while noLimpio:
            noLimpio=False
            for i in range (len(enemiesList)):
              if clave==enemiesList[i][3]:
                enemiesList[i][0].hideturtle()
                if enemiesList[i][1]==2:
                  enemiesList[i][4].ht()
                enemiesList.pop(i)
                noLimpio=True
                break

        else:
          x=random.randint(-200+140*enemy[3],-220+140*(enemy[3]+1))
          y=random.randint(0,1)
          y=110-70*y
          enemy[0].penup()
          enemy[0].setposition(x,y)

      if cont_cargas>=pt_carga:
        cont_cargas-=pt_carga
        cargas.append(turtle.Turtle())
        cargas[-1].color("blue")
        cargas[-1].shape("carga.gif")
        cargas[-1].speed(0)
        cargas[-1].penup()
        if len(cargas)==1:
          cargas[-1].setposition(360,275)
        else:
          cargas[-1].setposition(360-((len(cargas)-1) *16), 275)

    if isCollision(canon, enemy[0],35) or canonCollision:
      #Reset the bullet
      canon.hideturtle()
      canonstate = "ready"
      canon.setposition(0, -400)
      
      if enemy[2]<=1:
        
        if enemyspeed>0:
          enemyspeed+=aum_enemyspeed
        elif enemyspeed<0:
          enemyspeed-=aum_enemyspeed

        #Update the score
        if enemy[1]==0:
          score += 10
          cont_cargas += 10
          cont_ultra += 10
        elif enemy[1]==1:
          score += 20
          cont_cargas += 20
          cont_ultra += 20
        elif enemy[1]==2:
          score += 30
          cont_cargas += 30
          cont_ultra += 30
          enemy[4].ht()
        elif enemy[1]==3:
          score += 40
          cont_cargas += 40
          cont_ultra += 40
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font = ("Space Invaders", 14, "bold"))
        
        if nivel<4:
          enemy[0].ht()
          enemiesList.pop(indice)
        else:
          if enemy[1]==3:
            clave=enemy[3]
            noLimpio=True
            while noLimpio:
              noLimpio=False
              for i in range (len(enemiesList)):
                if clave==enemiesList[i][3]:
                  enemiesList[i][0].hideturtle()
                  if enemiesList[i][1]==2:
                    enemiesList[i][4].ht()
                  enemiesList.pop(i)
                  noLimpio=True
                  break

          else:
            if enemy[1]==0:
              enemy[0].shape("invader0_1.gif")
            elif enemy[1]==1:
              enemy[0].shape("invader1_2.gif")
            elif enemy[1]==2:
              enemy[0].shape("invader2_3.gif")
            x=random.randint(-200+140*enemy[3],-220+140*(enemy[3]+1))
            y=random.randint(0,1)
            y=110-70*y
            enemy[0].penup()
            enemy[0].setposition(x,y)

        if cont_cargas>=pt_carga:
          cont_cargas-=pt_carga
          cargas.append(turtle.Turtle())
          cargas[-1].color("blue")
          cargas[-1].shape("carga.gif")
          cargas[-1].speed(0)
          cargas[-1].penup()
          if len(cargas)==1:
            cargas[-1].setposition(360,275)
          else:
            cargas[-1].setposition(360-((len(cargas)-1) *16), 275)
        
      else:
        enemy[2]-=2
      
        if enemy[1]==0:
          enemy[0].shape("invader0_"+str(enemy[2])+".gif")
        elif enemy[1]==1:
          enemy[0].shape("invader1_"+str(enemy[2])+".gif")
        elif enemy[1]==2:
          enemy[0].shape("invader2_"+str(enemy[2])+".gif")
        elif enemy[1]==3:
          enemy[0].shape("invader3_"+str(enemy[2])+".gif")

    #Check for collision between bullet and enemy
    if isCollision(bullet, enemy[0],30) or bulletCollision:
      #Reset the bullet
      bullet.hideturtle()
      bulletstate = "ready"
      bullet.setposition(0, -400)
      
      if enemy[2]<=0:
        
        if enemyspeed>0:
          enemyspeed+=aum_enemyspeed
        elif enemyspeed<0:
          enemyspeed-=aum_enemyspeed

        #Update the score
        if enemy[1]==0:
          score += 10
          cont_cargas += 10
          cont_ultra += 10
        elif enemy[1]==1:
          score += 20
          cont_cargas += 20
          cont_ultra += 20
        elif enemy[1]==2:
          score += 30
          cont_cargas += 30
          cont_ultra += 30
          enemy[4].ht()
        elif enemy[1]==3:
          score += 40
          cont_cargas += 40
          cont_ultra += 40
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font = ("Space Invaders", 14, "bold"))
        
        if nivel<4:
          enemy[0].ht()
          enemiesList.pop(indice)
        else:
          if enemy[1]==3:
            clave=enemy[3]
            noLimpio=True
            while noLimpio:
              noLimpio=False
              for i in range (len(enemiesList)):
                if clave==enemiesList[i][3]:
                  enemiesList[i][0].hideturtle()
                  if enemiesList[i][1]==2:
                    enemiesList[i][4].ht()
                  enemiesList.pop(i)
                  noLimpio=True
                  break
            
          else:
            if enemy[1]==0:
              enemy[0].shape("invader0_1.gif")
            elif enemy[1]==1:
              enemy[0].shape("invader1_2.gif")
            elif enemy[1]==2:
              enemy[0].shape("invader2_3.gif")
            x=random.randint(-200+140*enemy[3],-220+140*(enemy[3]+1))
            y=random.randint(0,1)
            y=110-70*y
            enemy[0].penup()
            enemy[0].setposition(x,y)

        if cont_cargas>=pt_carga:
          cont_cargas-=pt_carga
          cargas.append(turtle.Turtle())
          cargas[-1].color("blue")
          cargas[-1].shape("carga.gif")
          cargas[-1].speed(0)
          cargas[-1].penup()
          if len(cargas)==1:
            cargas[-1].setposition(360,275)
          else:
            cargas[-1].setposition(360-((len(cargas)-1) *16), 275)

      else:
        enemy[2]-=1
        if enemy[1]==0:
          enemy[0].shape("invader0_"+str(enemy[2])+".gif")
        elif enemy[1]==1:
          enemy[0].shape("invader1_"+str(enemy[2])+".gif")
        elif enemy[1]==2:
          enemy[0].shape("invader2_"+str(enemy[2])+".gif")
        elif enemy[1]==3:
          enemy[0].shape("invader3_"+str(enemy[2])+".gif")
  
  if cont_ultra>=pt_ultra:
    ultraReady.showturtle()

  #Perder
  if not jugando:
    for i in range(len(cargas)):
      cargas[0].hideturtle()
      cargas.pop(0)
    
    ultraReady.ht()
    score=0
    cont_cargas=0
    cont_cargas_segura=0
    cont_ultra=0
    cont_ultra_segura=0
    score_segura=0
    score_pen.clear()
    player.reset()
    player.clear()
    player.penup()
    player.setposition(0,-240)
    player.hideturtle()
    
    imgPerder = turtle.Turtle() 
    imgPerder.color("blue")
    imgPerder.shape("final2.gif")
    imgPerder.penup()
    imgPerder.setposition(0, 0)
    imgPerder.showturtle()
    
    while True:
      tick(60)
      turtle.update()
      if teclas[6]==1:
        sys.exit()
      if teclas[5]==1:
        nivel=1
        imgPerder.hideturtle()
        iniciarJuego(nivel)
        jugando=True
        break

  #Ganar o pasar de nivel
  if len(enemiesList)==0:
    bullet.ht()
    canon.ht()
    ultra.ht()

    for i in range(len(life)):
      life[0].hideturtle()
      life.pop(0)
    cont_cargas_segura = len(cargas)
    cont_ultra_segura=cont_ultra
    nivel+=1
    player.reset()
    player.clear()
    player.penup()
    player.setposition(0,-240)
    player.hideturtle()
    if nivel>=nivel_ganar+1:
      for i in range(len(cargas)):
        cargas[0].hideturtle()
        cargas.pop(0)
      score=0
      cont_cargas=0
      cont_ultra=0
      score_pen.clear()
      imgGanar = turtle.Turtle()
      imgGanar.color("blue")
      imgGanar.shape("final1.gif")
      imgGanar.penup()
      imgGanar.setposition(0, 0)
  
      while True:
        tick(60)
        turtle.update()
        if teclas[6]==1:
          sys.exit()
        if teclas[5]==1:
          ultraReady.ht()
          imgGanar.hideturtle()
          nivel=1
          break
    score_segura=score
    iniciarJuego(nivel)   

  #Move the bullet only when bulletstate is "fire"
  if bulletstate == "fire":
    y = bullet.ycor()
    y = y + bulletspeed*deltaTime
    bullet.sety(y)
  #Check to see if bullet has reached the top
  if bullet.ycor() > 280:
    bullet.hideturtle()
    bulletstate = "ready"

  if (canonstate == "fire"):
    y=canon.ycor()
    y=y+bulletspeed*deltaTime
    canon.sety(y)
  if canon.ycor()>280:
    canon.ht()
    canonstate="ready"

  if (ultrastate == "fire"):
    y=ultra.ycor()
    y=y+bulletspeed*deltaTime
    ultra.sety(y)
  if ultra.ycor()>280:
    ultra.ht()
    ultrastate="ready"
