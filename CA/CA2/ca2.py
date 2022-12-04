'''
Continuous Assessment 2: Space Invaders
Student Name:   Dylan Murray
Student Number: 121747725

I have been using wikis found on pygame.org for help along with any lecture notes.
'''

import pygame, sys, math
from pygame.locals import *


class Game(object):
    '''
    the main class in which the game loop is executed and where the child class are called to run the game.
    '''
    
    def __init__(self):
        pygame.init()
        #defining the screen dimensions and background
        self._size = self._width, self._height = 640, 400
        self._black = 0, 0, 0
        self._screen = pygame.display.set_mode(self._size)

        #loading the image and defining the space ship while referring to the child.
        self._shipimage = pygame.image.load("space_ship.png")
        self._shipimage = pygame.transform.scale(self._shipimage, (60, 60))
        self._shipmodel = ShipState(290, 330, self._width ,3)

        #Tried to have multiple aliens pop up on screen.
      #  self._aliens = []
      #  while len(self._aliens) < 10:
           # timer = pygame.time.get_ticks()
           ## if timer % 2 == 0:
        self._alienimage = pygame.image.load("alien.png")
        self._alienimage = pygame.transform.scale(self._alienimage, (60, 60))
        self._alienmodel = AlienState(0, 0, self._width, 3, 60)
                #self._aliens.append(AlienState)
        self._rocketList = []

    def on_execute(self):
        #When the program executes then carry out these operations
        while True:

            #Move sequence for enemies to move every set amount of ticks
            timer = pygame.time.get_ticks()
            if timer % 1000 == 0:
                if self._alienmodel.getXPos() == self._width:
                        self._alienmodel.moveY(10) 
                else:    
                    self._alienmodel.moveX(10)

            #Key presses and events such as collisions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self._shipmodel.handleMoveLeft()

                    if event.key == pygame.K_RIGHT:
                        self._shipmodel.handleMoveRight()

                    if event.key == pygame.K_SPACE:
                        rocket = Rocket(self._shipmodel.getXPos())
                        self._rocketList.append(rocket)

                if event.type == pygame.KEYUP:
                    self._shipmodel.handleStopMove()

                #if alien collides with ship then game over
                if self._shipmodel.collision(self._alienmodel):
                    print ("Game Over")
                    sys.exit()

                #tried figuring out collison with rockets and enemies but need to figure multiple enemies first
            #    if self._alienmodel.collision(Rocket):
           #         self._alienCount -= 1

                #work in progress code for populating screen with rockets but didnt finish in time
                i = 0
                while i < len(self._rocketList):
                    self._rocketList[i].moveRocket()
                    self._screen.blit(self._rocketList[i].getIcon(),(self._rocketList[i].getXPos(), self._rocketList[i].getYPos()))
                    i += 1

            #draw sprites on screen
            self._screen.fill(self._black)
            self._screen.blit(self._shipimage, (self._shipmodel.getXPos(), self._shipmodel.getYPos()))
            self._screen.blit(self._alienimage, (self._alienmodel.getXPos(), self._alienmodel.getYPos()))
            pygame.display.flip()

class AlienState(object):
    '''
    Alien Object in which is various attributes are define to then be called by its parent "Game" class.
    '''

    def __init__(self, xpos, ypos, maxxpos, change, reset):
        self._xPos = xpos
        self._yPos = ypos
        self._maxXPos = maxxpos
        self._change = change
        self._reset = reset
    
    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def moveX(self, change):
        self._xPos += change
    
    def moveY(self, reset):
        self._yPos += reset
        self._xPos = 0

    #Work in progress rocket collision code
'''
    def collision(self, rocket):
        distance = math.sqrt((math.pow(self._xPos - rocket._xPos, 2)) + (math.pow(self._yPos - rocket._yPos, 2)))
        if distance < 30:
            return True
        else:
            return False
'''

class ShipState(object):
    '''
    Spaceship class to determine attributes as well as 
    functions to handle movement controls and whether or not collision is true when called by the "Game" parent class
    '''

    def __init__(self, xpos, ypos, maxxpos, change):
            self._xPos = xpos
            self._yPos = ypos
            self._maxXPos = maxxpos
            self._change = change

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def handleMoveRight(self):
        if self._xPos - self._change > 0:
            self._xPos += self._change
    
    def handleMoveLeft(self):
        if self._xPos + self._change < self._maxXPos:
            self._xPos -= self._change
    
    def handleStopMove(self):
        self._xPos = self._xPos

    def collision(self, alien):
        distance = math.sqrt((math.pow(self._xPos - alien._xPos, 2)) + (math.pow(self._yPos - alien._yPos, 2)))
        if distance < 30:
            return True
        else:
            return False

class Rocket(object):
    '''
    Rocket class to determine attributes as well as movement functions to be called by the "Game" Parent class.
    '''
    
    def __init__(self, xpos):
        self._xPos = xpos
        self._yPos = 220
        self._icon = pygame.image.load("rocket.png")
        self._icon = pygame.transform.scale(self._icon, (30, 30))
        self._missileYChange = 1

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos
    
    def moveRocket(self):
        self._yPos -= self._missileYChange

    def getIcon(self):
        return self._icon
        

if __name__ == "__main__":
    theGame = Game()
    theGame.on_execute()