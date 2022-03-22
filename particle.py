import pyxel as px
from math import *
import random

colorTable = [2,4,9,10,7]

class Particle:
    def __init__(self,x=0,y=0,lifeTime=50):
        self.Reset(x,y,lifeTime)  

    
    def Reset(self,x,y,lifeTime):
        self.x=x
        self.y=y
        self.color=colorTable[-1]
        self.lifeTime = lifeTime
        self.active = True
        self.visiable = True

    def Update(self):
        if self.active == True:
            self.lifeTime -=1
            if self.lifeTime<0:
                self.active = False
                self.lifeTime = 0
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
        self.particleResetParam = particleResetParam
        self.maxNum = maxNum
        self.newPerFrame = newPerFrame
        for i in range(maxNum):
            p = particle(self.x,self.y,lifeTime=0)
            self.particlePool.append(p)
        self.activate = activate
        self.visible = visible



    def Update(self):
        if self.activate == False:
            return
        #update all active particles
        for p in self.activePool:
            p.Update()
        # pop all the activate == False particle back to pool
        for idx in range(len(self.activePool) - 1, -1, -1):
            if self.activePool[idx].active == False:
                self.particlePool.append(self.activePool.pop(idx))
        #generate new particles
        if len(self.particlePool)>self.newPerFrame:
            updateCount = self.newPerFrame
        else:
            updateCount = len(self.particlePool)
        for i in range(updateCount):
            p=self.particlePool.pop()
            if self.particleResetParam is not None:
                p.Reset(*self.particleResetParam)
            else:
                p.Reset(self.x,self.y,lifeTime=50)

            self.activePool.append(p)


        #
    def Draw(self,screenX:int=0,screenY:int=0):
        if self.visible == False:
            return
        for p in self.activePool:
            p.Draw(screenX,screenY)

    
