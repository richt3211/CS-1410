import pygame
import froggerlib

class Frogger:

    def __init__( self, width, height ,size):
        self.mSize = size
        self.mWidth = width
        self.mHeight = height
        self.mReducedSize = 0.8 * size
        column = self.mWidth / self.mSize
        row = self.mHeight / self.mSize
        # frog
        frogSize = self.mReducedSize * .2
        frogX = self.mSize * 6 - self.mReducedSize /2
        frogY = self.mSize * 12 + (self.mSize - self.mReducedSize) / 2
        self.mFrog = froggerlib.Frog(frogX,frogY,self.mReducedSize,self.mReducedSize,frogX,frogY,20, self.mSize, self.mSize)

        #stage1

        self.mStage1 = froggerlib.Stage(0, self.mHeight - size, self.mWidth, self.mHeight)

        #stage2

        self.mStage2 = froggerlib.Stage(0, size * 6 , self.mWidth, size)

        #road

        self.mRoad = froggerlib.Road(0, size * 7, self.mWidth, size * 5)

        #water

        self.mWater = froggerlib.Water(0, size * 1, self.mWidth, size * 5)

        #home

        self.mHome = froggerlib.Home(0, 0, self.mWidth, size)

        #grass 

        grassX = size * 2 - self.mReducedSize / 2 - size * 0.1
        grassY = 0

        self.mGrass = []
        for x in range(5):
            grass = froggerlib.Grass( grassX, grassY, self.mReducedSize, self.mSize)
            grassX += size * 2
            self.mGrass.append(grass)

        # dozers

        dozerX = size * 2
        dozerY = frogY - size
        self.mDozers = []
        for x in range(3):
            dozer = froggerlib.Dozer( dozerX, dozerY, self.mReducedSize, self.mReducedSize, dozerX, dozerY, 1)
            dozerX += size * 4
            self.mDozers.append(dozer)

        #car

        carX = size * 4
        carY = dozerY - size
        self.mCars = []
        for x in range(4):
            car = froggerlib.Car( carX, carY, self.mReducedSize, self.mReducedSize, carX, carY, 5)
            carX += size * 4
            self.mCars.append(car)

        # truck

        truckX = size * 3
        truckY = carY - size
        self.mTrucks = []
        for x in range(4):
            truck = froggerlib.Truck( truckX, truckY, self.mReducedSize, self.mReducedSize, truckX, truckY, 3)
            truckX += size * 3
            self.mTrucks.append(truck)

        #raceCar
        raceCarX = size * 3
        raceCarY = truckY - size
        self.mRaceCars = []
        for x in range(4):
            raceCar = froggerlib.RaceCar( raceCarX, raceCarY, self.mReducedSize, self.mReducedSize, raceCarX, raceCarY, 3, 10)
            raceCarX += size * 3
            self.mRaceCars.append(raceCar)

        #dozers1
        dozerX = size * 4
        dozerY = raceCarY - size
        self.mDozers1 = []
        for x in range(4):
            dozer = froggerlib.Dozer( dozerX, dozerY, self.mReducedSize, self.mReducedSize, dozerX, dozerY, 1)
            dozerX += size * 3
            self.mDozers1.append(dozer)

        #logs1
        self.mLog1_size = self.mReducedSize * 4
        log1X = size * 3
        log1Y = dozerY - size * 2
        self.mLogs1 = []
        for x in range(3):
            log = froggerlib.Log(log1X, log1Y, self.mLog1_size, self.mReducedSize, log1X, log1Y, 1)
            log1X += size * 5
            self.mLogs1.append(log)

        #turtles1
        self.mTurtle1_size = self.mReducedSize * 3
        turtle1X = size * 3
        turtle1Y = log1Y - size
        self.mTurtles1 = []
        for x in range(3):
            turtle = froggerlib.Turtle(turtle1X, turtle1Y, self.mTurtle1_size, self.mReducedSize, turtle1X, turtle1Y, 2)
            turtle1X += size * 4
            self.mTurtles1.append(turtle)

        #logs2
        self.mLog2_size = self.mReducedSize * 2
        log2X = size * 3
        log2Y = turtle1Y - size
        self.mLogs2 = []
        for x in range(3):
            log = froggerlib.Log(log2X, log2Y, self.mLog2_size, self.mReducedSize, log2X, log2Y, 4)
            log2X += size * 4
            self.mLogs2.append(log)
        #turtles
        self.mTurtle2_size = self.mReducedSize * 3
        turtle2X = size * 2
        turtle2Y = log2Y - size
        self.mTurtles2 = []
        for x in range(3):
            turtle = froggerlib.Turtle(turtle2X, turtle2Y, self.mTurtle2_size, self.mReducedSize, turtle2X, turtle2Y, 3)
            turtle2X += size * 4
            self.mTurtles2.append(turtle)

        #logs3
        self.mLog3_size = self.mReducedSize * 3
        log3X = size * 3
        log3Y = turtle2Y - size
        self.mLogs3 = []
        for x in range(3):
            log = froggerlib.Log(log3X, log3Y, self.mLog3_size, self.mReducedSize, log3X, log3Y, 4)
            log3X += size * 4
            self.mLogs3.append(log)
        
        self.mGameOver = True

    def update( self, dt, keys ):

        #frog moves
        if self.mGameOver == True:

            if self.mFrog.outOfBounds(self.mWidth, self.mHeight):
                self.mGameOver = False

            if pygame.K_w in keys:
                self.mFrog.up()
            if pygame.K_a in keys:
                self.mFrog.left()
            if pygame.K_d in keys:
                self.mFrog.right()
            if pygame.K_s in keys:
                self.mFrog.down()
            self.mFrog.move()

            #dozer
            for dozer in self.mDozers:
                dozer.setDesiredX(self.mWidth)
                if dozer.atDesiredLocation():
                    dozer.setX(0 - self.mSize)
                dozer.move()
                if dozer.hits(self.mFrog):
                    self.mGameOver = False
            #Cars


            for car in self.mCars:
                car.setDesiredX(0)
                if car.atDesiredLocation():
                    car.setX(self.mWidth)
                car.move()
                if car.hits(self.mFrog):
                    self.mGameOver = False

            # trucks


            for truck in self.mTrucks:
                truck.setDesiredX(self.mWidth)
                if truck.atDesiredLocation():
                    truck.setX(0 - self.mSize)
                truck.move()
                if truck.hits(self.mFrog):
                    self.mGameOver = False
            #racecars
            for raceCar in self.mRaceCars:
                raceCar.setDesiredX(0)
                if raceCar.atDesiredLocation():
                    raceCar.setX(self.mWidth)
                raceCar.move()
                if raceCar.hits(self.mFrog):
                    self.mGameOver = False
            #dozers1
            for dozer in self.mDozers1:
                dozer.setDesiredX(0 - self.mSize)
                if dozer.atDesiredLocation():
                    dozer.setX(self.mWidth)
                dozer.move()
                if dozer.hits(self.mFrog):
                    self.mGameOver = False

            #logs1

            for log in self.mLogs1:
                log.setDesiredX(0 - self.mLog1_size )
                if log.atDesiredLocation():
                    log.setX(self.mWidth)
                log.move()
                # if log.supports(self.mFrog):
                #     self.mFrog.setRide(True)
                # else:
                #     self.mFrog.setRide(False)
                log.supports(self.mFrog)
            #turtles1

            for turtles in self.mTurtles1:
                turtles.setDesiredX(self.mWidth)
                if turtles.atDesiredLocation():
                    turtles.setX(0 - self.mTurtle1_size)
                turtles.move()
                turtles.supports(self.mFrog)
            #logs2

            for log in self.mLogs2:
                log.setDesiredX(0 - self.mLog2_size)
                if log.atDesiredLocation():
                    log.setX(self.mWidth)
                log.move()
                log.supports(self.mFrog)
            #turtles2

            for turtles in self.mTurtles2:
                turtles.setDesiredX(self.mWidth)
                if turtles.atDesiredLocation():
                    turtles.setX(0 - self.mTurtle2_size)
                turtles.move()
                turtles.supports(self.mFrog)
            #logs3

            for log in self.mLogs3:
                log.setDesiredX(0 - self.mLog3_size)
                if log.atDesiredLocation():
                    log.setX(self.mWidth)
                log.move()
                log.supports(self.mFrog)
            if self.mHome.hits(self.mFrog):
                self.mGameOver = False
                print("You won the Game")
            if self.mWater.hits(self.mFrog):
                self.mGameOver = False
                print("You lost the game")
            for grass in self.mGrass:
                if grass.hits(self.mFrog):
                    self.mFrog.setRide(False)
                    self.mGameOver = False
                    print("you lost the game")
        
    def drawFrog(self,surface):
        green = (55, 207,50)
        rect = (self.mFrog.getX(),self.mFrog.getY(),self.mFrog.getWidth(),self.mFrog.getHeight())        
        pygame.draw.rect(surface, green, rect, 0)

    def drawRect(self, surface, object1, color):
        rect = (object1.getX(), object1.getY(), object1.getWidth(), object1.getHeight())
        pygame.draw.rect(surface, color, rect, 0)
    def drawRects(self, surface, objects, color):
        for object1 in objects:
            rect = (object1.getX(), object1.getY(), object1.getWidth(), object1.getHeight())
            pygame.draw.rect(surface, color, rect, 0)


    def draw(self,surface):
        surface.fill((0,0,0))

        #stage1

        gray = (31, 51 ,30)
        self.drawRect(surface, self.mStage1, gray)


        #road

        roadColor = (175, 178, 179)
        self.drawRect(surface, self.mRoad, roadColor)

        
        #water

        waterColor = (44, 60, 242)
        self.drawRect(surface, self.mWater, waterColor)

        #stage2

        self.drawRect(surface,self.mStage2,gray)

        #home

        homeColor = (242, 136, 44)
        self.drawRect(surface, self.mHome, homeColor)

        #grass

        grassColor = (176, 235, 176)
        self.drawRects(surface, self.mGrass, grassColor)

        

        #Dozers

        red = (242, 12, 12)
        self.drawRects(surface, self.mDozers, red)

        #Cars

        orange = (230, 131, 18)
        self.drawRects(surface, self.mCars, orange)

        #Trucks

        white = (152, 151 , 166)
        self.drawRects(surface,self.mTrucks,white)

        #RaceCars

        purple = (212, 144, 203)

        self.drawRects(surface, self.mRaceCars, purple)

        #dozers1

        self.drawRects(surface, self.mDozers1, red)

        #logs1
        brown = (163, 104, 52)
        self.drawRects(surface, self.mLogs1, brown)

        #turtles

        darkgreen = (95, 150, 6)
        self.drawRects(surface, self.mTurtles1, darkgreen)

        #logs2

        self.drawRects(surface, self.mLogs2, brown)

        #turtles

        self.drawRects(surface, self.mTurtles2, darkgreen)

        #logs3

        self.drawRects(surface, self.mLogs3, brown)







        # frog

        self.drawFrog(surface)