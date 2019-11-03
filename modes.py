from characters import *
import Tkinter

def highNoonInitFn(data):
    data.initBackground()
    data.initEnemyImage()
    data.initClockImages()
    data.initShotImage()
    data.scoreBoard = Scoreboard()
    data.initEverything()

def initEverything(data)
    #init enemy
    data.enemy = Enemy()
    
    #init clock
    data.clock = Clock()
    data.clock.setSecond()
    
    #init shots
    data.shots = []

    data.timerDelay = 10
    data.shotLegal = False
    
def initBackground(data):
    backgroundURL = https://i.imgur.com/FQarGQA.png
    data.background = data.loadImage(backgroundURL)

def initClockImages(data):
    oneToNoon = data.loadImage(Clock.oneToNoonURL)
    noon = data.loadImage(Clock.noonURL)
    data.clockImages = [oneToNoon, noon]

def initEnemyImage(data):
    enemy = data.loadImage(https://i.imgur.com/rtTxnIb.png)
    data.enemyImage = enemy

def initShotImage(data):
    shotURL = https://i.imgur.com/FQarGQA.png
    data.shotImage = data.loadImage(shotURL)

def timerFired(data):
    data.clock.tick(data)
    if data.clock.isNoon == True:
        data.shotLegal = True
    #sample data from frame here
    data.checkFireGesture()

def checkFireGesture(data):
    if SCREENRHO0 < yaw < SCREENRHO1 and SCREENTHETA0 < pitch < SCREENTHETA1:
        if #middle to pinky are bent:
            shot = Shot(pitch, yaw)
            data.shots.append(shot)

def checkHit(data, shot):
    if shot.checkHit:
        data.scoreboard.addScore()


def redrawAll(data):
    drawBackground(data, canvas)
    drawEnemy(data, canvas)
    drawClock(data, canvas)
    drawShots(data, canvas)

def drawBackground(data, canvas):
    canvas.create_image(0, 0, anchor = 'nw', image = data.background)

def drawEnemy(data, canvas):
    x = data.enemy.x
    y = data.enemy.y
    canvas.create_image(x, y, image = data.enemyImage)

def drawClock(data, canvas):
    clockIndex = 0
    if data.clock.isNoon:
        clockIndex = 1
    clock = data.clockImages[clockIndex]
    canvas.create_image(0, 0, anchor = 'nw', image = clock)

def drawShots(data, canvas):
    for shot in data.shots:
        x = shot.x
        y = shot.y
        canvas.create_image(x, y, image = data.shotImage)


