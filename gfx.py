import pyxel as px
from math import *
def Tline( x0:int, y0:int, x1:int, y1:int, mx:float, my:float,mdx:float=0.125,mdy:float=0.125,imgMap:int=0,tiltMap:int=0):
    '''
    x0,y0 The x,y coordinate of the start of the line
    x1,y1 The x,y coordinate of the end of the line
    mx,my The x,y coordinate to begin sampling the map, expressed in (fractional) map tiles
    mdx,mdy The amount to add to mx,my after each pixel is drawn, expressed in (fractional) map tiles. Default is 1/8 (move right one map pixel)
    '''
    tmap = px.tilemap(tiltMap)
    imap = px.image(imgMap)
    if abs( y1-y0)>abs(x1-x0):
        steep = True
        x0,y0 = y0,x0
        x1,y1 = y1,x1
    else:
        steep = False
           
    if (x0>x1):
        x0,x1 = x1,x0
        y0,y1 = y1,y0

    dx = x1-x0
    dy= abs(y1 - y0)

    err = dx//2
    if y0<y1:
        ystep = 1
    else:
        ystep = -1

    if steep:
        for i in range(dx+1):
            #get the color from map
            tileX,tileY=tmap.pget(floor(mx),floor(my)) 
            color=imap.pget(tileX*8+(mx*8)%8,tileY*8+(my*8)%8)
            mx +=mdx
            my +=mdy
            px.pset(y0,x0+i,color)
            err -= dy
            if err <0:
                y0+=ystep
                err += dx
    else:
        for i in range(dx+1):
            #get the color from map
            tileX,tileY=tmap.pget(floor(mx),floor(my)) 
            color=imap.pget(tileX*8+(mx*8)%8,tileY*8+(my*8)%8)
            mx +=mdx
            my +=mdy
            px.pset(x0+i,y0,color)
            err -= dy
            if err <0:
                y0+=ystep
                err += dx
    
    
def Tvline( x0:int, y0:int, y1:int, mx:float, my:float,mdx:float=0.125,mdy:float=0.125,imgMap:int=0,tiltMap:int=0):   
    tmap = px.tilemap(tiltMap)
    imap = px.image(imgMap)
    for i in range(y0,y1+1):
        tileX,tileY=tmap.pget(floor(mx),floor(my)) 
        color=imap.pget(tileX*8+(mx*8)%8,tileY*8+(my*8)%8)
        mx +=mdx
        my +=mdy
        px.pset(x0,i,color)
    
def Thline( x0:int, y0:int, x1:int, mx:float, my:float,mdx:float=0.125,mdy:float=0.125,imgMap:int=0,tiltMap:int=0):   
    tmap = px.tilemap(tiltMap)
    imap = px.image(imgMap)
    for i in range(x0,x1+1):
        tileX,tileY=tmap.pget(floor(mx),floor(my)) 
        color=imap.pget(tileX*8+(mx*8)%8,tileY*8+(my*8)%8)
        mx +=mdx
        my +=mdy
        px.pset(i,y0,color)