import pygame

def draw_litlight(surface, numlit, Lit, Unlit, posX, posY):
   flag = True
   
   for x in range(0,10):
       if(x < numlit):
           flag = True
           
       elif(x >= numlit):
           flag = False
           
       if(flag == True):
           surface.blit(Lit, (posX,posY))
           
       if(flag == False):
           surface.blit(Unlit, (posX,posY))

       posX = posX + 40
