import math

SCREENSIZE = 38 #CM
SCREENHEIGHT = 18.5 #CM
SCREENTHETA0 = -30
SCREENTHETA1 = 30
SCREENRHO0 = -20
SCREENRHO1 = 20

class Shot(object):
    def __init__(self, theta, rho):
        self.screenDistance = 100 #cm
        self.screenHeight = 140 #cm
        self.leapHeight = 90 #cm
        self.screenWidth = 1200 #pixel
        dx = self.screenDistance * math.tan(theta)
        dy = self.screenDistance * math.tan(rho)
        self.y = self.screenHeight - (self.leapHeight + dy)
        self.x = self.screenWidth // 2 + dx

    def checkHit(self, enemy):
        if (enemy.x0 < self.x < enemy.x1) and (enemy.y0 < self.y < enemy.y1):
            return True

class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x =
        self.y = 
        self.width = 
        self.height = 
        self.x0 = self.x - self.width // 2
        self.y0 = self.y - self.height // 2
        self.x1 = self.x + self.width // 2
        self.y1 = self.y + self.height // 2

import random

#init a clock, then 
class Clock(object):
    oneToNoonURL = https://i.imgur.com/Q6DcaE3.jpg
    noonURL = https://i.imgur.com/DsGirKg.jpg
    #credit: clipartmag http://clipartmag.com/a-picture-of-a-clock

    @staticmethod
    def setSecond():
        secondsToNoon = random.randint(5, 20)
        self.second = 60 - secondsToNoon

    def __init__(self):
        self.hour = 11
        self.minute = 59
        self.second = 0
        self.noon = False
        self.size = 250
        self.x = 0 + self.size // 2
        self.y = 0 + self.size // 2

    def tick(self, data):
        self.second += 1 / data.timerDelay
        if self.second >= 60:
            self.hour = 12
            self.minute = 0
            self.noon = True

class Scoreboard(object):
    def __init__(self):
        self.scores = {}
        self.tempScore = 0

    def saveScore(self):
        name = getUserInput('What do you go by, ranger?')
        self.scores[self.tempScore] = self.scores.get(self.tempScore, []) + [name]
        self.tempScore = 0
        if len(self.scores) > 5:
            lowestScore = 7
            for score in self.scores:
                if score < lowestScore:
                    lowestScore = score
            del self.scores[lowestScore]

    def addScore(self):
        self.tempScore += 1

        
