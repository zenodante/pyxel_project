import pyxel as px
from math import *
import random

colorTable = [2,4,9,10,7]

class Particle:
    def __init__(self):
        self.Reset(x=0,y=0,lifeTime=1)  

    
    def Reset(self,x,y,lifeTime):
        self.x=x
        self.y=y
        self.color=colorTable[-1]
        self.lifeTime = lifeTime
        self.active = True
        self.visiable = True

    def Update(self):
        self.x += random.randint(-2,2)
        self.y += random.randint(-2,2)
        self.color = colorTable[floor(self.lifeTime/10)]

    def Draw(self,screenX:int=0,screenY:int=0):
        if self.visiable == True:
            px.pset(self.x - screenX,self.y - screenY,self.color)

    
class ParticleGenerator:
    def __init__(self,x:int,
                y:int,
                particle=Particle,
                particleResetParam=None,
                newPerFrame:int=20,
                maxNum:int=1000,
                activate:bool=True,
                visible:bool=True):
        self.particlePool=list()
        self.activePool=list()
        self.x = x
        self.y = y
        self.maxNum = maxNum
        self.newPerFrame = newPerFrame
        for i in range(maxNum):
            p = particle()
            self.particlePool.append(p)
        self.activate = activate
        self.visible = visible

    def InitNewParticle(self,p):
        p.Reset(self.x,self.y,lifeTime=50)


    def Update(self):
        if self.activate == False:
            return

        # pop all the activate == False particle back to pool
        for idx in range(len(self.activePool) - 1, -1, -1):
            #if the particle active is not depends on the life time, here remove the inactive particle
            if self.activePool[idx].active == False:
                self.particlePool.append(self.activePool.pop(idx)) 
                continue
            #check the life time, if it is >0, means it would be count down by 1 each update
            if self.activePool[idx].lifeTime >0:
                self.activePool[idx].lifeTime -=1
            #check the life time for particle
            if (self.activePool[idx].lifeTime == 0):
                self.activePool[idx].active = False 
            #update the particle state, even if is already active, it would still be draw for current frame
            self.activePool[idx].Update()

                
        #generate new particles
        if len(self.particlePool)>self.newPerFrame:
            updateCount = self.newPerFrame
        else:
            updateCount = len(self.particlePool)
        for i in range(updateCount):
            p=self.particlePool.pop()
            self.InitNewParticle(p)
            self.activePool.append(p)
            
            


        #
    def Draw(self,screenX:int=0,screenY:int=0):
        if self.visible == False:
            return
        for p in self.activePool:
            p.Draw(screenX,screenY)

    
