import pyxel as px
from math import *
def Tline( x0, y0, x1, y1, mx, my,mdx=0.125,mdy=0.125,tiltMap=0):
    '''
    x0,y0 The x,y coordinate of the start of the line
    x1,y1 The x,y coordinate of the end of the line
    mx,my The x,y coordinate to begin sampling the map, expressed in (fractional) map tiles
    mdx,mdy The amount to add to mx,my after each pixel is drawn, expressed in (fractional) map tiles. Default is 1/8 (move right one map pixel)
    '''
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


    '''
    while(x0<x1):
        if steep:
            px.pset(y0,x0,3)
        else:
            px.pset(x0,y0,3)
        err -= dy
        if err <0:
            y0 += ystep
            err += dx
        x0 +=1
    '''
    if steep:
        for i in range(dx+1):
            #get the color from map
            
            px.pset(y0,x0+1,3)
            err -= dy
            if err <0:
                y0+=ystep
                err += dx
    else:
        for i in range(dx+1):
            #get the color from map
            px.pset(x0+i,y0,3)
            err -= dy
            if err <0:
                y0+=ystep
                err += dx
    
    
    
            
    
