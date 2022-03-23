import particle as p
import pyxel as px
import random

class RainParticle(p.Particle):
    def __init__(self):
        self.Reset(x=0,y=0,groundY=0,length=1,speed=1,color=0)

    def Reset(self,x,y,groundY,length,speed,color):
        self.length = length
        self.color = color
        self.speed = speed
        self.groundY= groundY
        super().Reset(x,y,-1)

    def Update(self):
        self.y += self.speed
        if (self.y +self.length) > self.groundY:
            self.active = False
        
    def Draw(self,screenX:int=0,screenY:int=0):
        px.line(self.x-screenX, self.y-screenY, self.x-screenX, self.y-screenY+self.length, self.color)


class Rain(p.ParticleGenerator):
    def __init__(self,
                left=0,
                right=127,
                y=0,
                groundY=120,
                color=10,
                speed=5,
                particle=RainParticle,
                newPerFrame:int=20,
                maxNum:int=1000,
                activate:bool=True,
                visible:bool=True,
                ):
        self.left = left
        self.right = right
        self.groundY = groundY
        self.color = color
        self.speed = speed
        super().__init__(left,y,particle,newPerFrame,maxNum,activate,visible)

    def InitNewParticle(self,p):
        
        #(x,y,groundY,length,speed,color
        p.Reset(random.randint(self.left,self.right),self.y,self.groundY,random.randint(1,5),self.speed,self.color)

