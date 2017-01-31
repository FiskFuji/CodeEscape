"""This module contains a function that draws text onto a Pygame surface."""
import pygame
import sys

pygame.init()
pygame.mixer.pre_init(22050, -16, 16, 4096)
pygame.mixer.init()

def printText(surface, text, color, fnt, x, y, sfx, mute=False):
    """
    Function draws text onto a surface one character at a time.
    --Arguments--
        surface:    ARG TYPE: pygame.Surface() object.
            A pygame.Surface() object such as a display or other surfaces.
            
        text:       ARG TYPE: sequence
            Sequence of strings that will be iterated over. Each string will
            be drawn one character at a time onto the surface passed.

        fnt:        ARG TYPE: pygame.font.Font() object.
            A pygame.font.Font() object passed that will determine the font
            drawn onto the surface. Has only been tested with monospace fonts
            like Monospace, Courrier New, etc. Currently also only works with
            14pt font.

        x:          ARG TYPE: int, float
            The x-coordinate to begin drawing the text on the screen. Will be
            automatically updated with each word.

        y:          ARG TYPE: int, float
            The y-coordinate to begin drawing the text on the screen. Will be
            automatically updated after each subsequent string. I.E: Multiple
            strings in the sequence; a 'block' of text.

        sfx:        ARG TYPE: pygame.Sound() object.
            A sound effect to be played as every couple of characters are drawn.
            Sound effect has a max play time of 270 ms.

        mute:       ARG TYPE: bool
            Boolean to determine whether or not the sound is muted instead.
            Since a sound effect must be provided, this is the option to make
            it silent.
    """
    # Text initially is not under any formatting.
    # Initialize a PyGame Clock object locally for limiting purposes.
    localClock = pygame.time.Clock()
    currString = ""
    for string in text:
        
        for single in string:
            # Limit the speed of the loop iteration.
            localClock.tick(25)
            currString += single
            
            if not mute and single != " ":
                sfx.play(maxtime=200)
                
            surface.blit(fnt.render(currString, 1, color), (x, y))
            pygame.display.update()
            
        currString = ""
        y += 51
        
    sfx.stop()

"""
screen = pygame.display.set_mode((600, 500))
sf = pygame.mixer.Sound("textsnd.wav")
prob = ["What is the capital of Uzbekistan?",
        "   Who knows?"]
myf = pygame.font.SysFont("Monospace", 50)

printText(screen, prob, (255, 255, 255), myf, 10, 10, sf)
"""
