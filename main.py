#-------------------------------------------------------------------------------------
import pygame as py
import sys
import random as rnd
import NolanGuzman as nolan
import JoseGarcia as jose
import ArthurDiaz as aj
import AndyKor as ak
import lightbulbs as lb
import textform as tf
from dhb import Particle
import pygame.gfxdraw as pgf

py.init()
py.mixer.pre_init(22050, -16, 16, 4096)
py.mixer.init()

#-------------------------------------------------------------------------------------
dimensions = py.display.Info()
screen = py.display.set_mode((dimensions.current_w, dimensions.current_h), py.FULLSCREEN)
py.display.set_caption("Hackathon Study Buddy")
py.key.set_repeat(500, 25)
textFont = py.font.SysFont("Monospace", 50)
fpscounter = py.time.Clock()

# Game State Vars:
running = True
answer_correct = 0
section = 0
text_sfx = py.mixer.Sound("textsnd.wav")
lit = py.image.load("l.png")
unlit = py.image.load("ul.png")
question_dict = {}
question_dict.update(nolan.NolanQs)
question_dict.update(jose.myQs)
question_dict.update(aj.myQs)
question_dict.update(ak.myQs)

#-------------------------------------------------------------------------------------
class StartScreen:
    centerX = 0
    centerY = 0
    nameX = 0
    nameY = 0
    color = (0, 0, 0)
    titlefont = py.font.SysFont("Monospace", 75)
    namefont = py.font.SysFont("Monospace", 27)
    
    def __init__(self, centerX, centerY, nameX, nameY, (r,g,b)):
        self.centerX = centerX
        self.centerY = centerY
        self.nameX = nameX
        self.nameY = nameY
        self.color = (r,g,b)

    def title(self):
        screen.blit(self.titlefont.render("Code Escape", 1, self.color), (self.centerX, self.centerY))

    def names(self):
        screen.blit(self.namefont.render("Created by: Andy Kor, Arthur Diaz, Jose Garcia, Kirk Worley, Nolan Guzman"
                                         , 1, self.color), (self.nameX, self.nameY))

#-------------------------------------------------------------------------------
class Button:
   def __init__(self, position, color, size, font, text, textcolor, textpos, chroma=None, rwid=0):
       self.x = position[0]
       self.y = position[1]
       self.rgb = color
       self.width = size[0]
       self.height= size[1]
       self.message = text
       self.messagex = textpos[0]
       self.messagey = textpos[1]
       self.rwidth = rwid
       self.sur = py.Surface((self.width+2, self.height+2))
       self.hitbox = py.Rect((self.x, self.y), (self.width, self.height))
       self.sur.set_colorkey((chroma))
       self.draw(font, textcolor)

   def draw(self, fnt, txtcolor):
       self.sur.fill((0, 0, 0))
       self.sur.lock()
       py.draw.rect(self.sur, self.rgb, ((0, 0), (self.width, self.height)), self.rwidth)
       self.sur.unlock()
       self.sur.blit(fnt.render(self.message, 1, txtcolor), (self.messagex, self.messagey))

   def blit(self, surface):
       surface.blit(self.sur, (self.x, self.y))
       
#-------------------------------------------------------------------------------------        
def Duplicates(dictionary_numbers):
    non_duplicates = []
    for i in dictionary_numbers:
        if i not in non_duplicates:
            non_duplicates.append(i)
    return non_duplicates

#-------------------------------------------------------------------------------
def RestartRandom():
    new_dictionary_numbers = [rnd.randint(1, 48) for i in range(100)]
    new_non_duplicates = []
    
    for i in new_dictionary_numbers:
        if i not in new_non_duplicates:
            new_non_duplicates.append(i)
            
    return new_non_duplicates

#-------------------------------------------------------------------------------
def GetRandomDictionary(dict_numbers, questions):
    x = dict_numbers[0]
    dict_numbers.pop(0)
    return questions[x]

#-------------------------------------------------------------------------------------
def QuestionPage(current_problem):
    global answer_correct
    posX = dimensions.current_w/4.5
    posY = 30
    questionfont = py.font.SysFont("Monospace", 50)
    answerfont = py.font.SysFont("Monospace", 50)

    py.display.update()

    lb.draw_litlight(screen, answer_correct, lit, unlit, dimensions.current_w/4, dimensions.current_h/1.35)
    tf.printText(screen, current_problem, (255, 255, 255), questionfont, posX, posY, text_sfx)
        
#-------------------------------------------------------------------------------------
# Title Screen Vars
start = StartScreen((dimensions.current_w)/2.75, (dimensions.current_h)/25, (dimensions.current_w)/5.25,
                    (dimensions.current_h)/1.15, (255, 255, 255))
                 
startButton = Button((dimensions.current_w/3, dimensions.current_h/2), (255, 255, 255),
                     (dimensions.current_w/3.3, dimensions.current_h/14), textFont,
                     "Code your way out!", (255, 255, 255), (dimensions.current_w/80, dimensions.current_h/80),
                     (0, 0, 0), 2)

particles = [Particle((255, 255, 255)) for i in range(28)]
particles2 = [Particle((0, 255, 255)) for i in range(18)]
particles.extend(particles2)
#-------------------------------------------------------------------------------------
while running:

    #---------------------------------------------------------------------------------
    # Title Screen Section
    while section == 0:
        fpscounter.tick(60)
        screen.fill((0, 0, 0))
        for particle in particles:
            particle.update(screen)
        
        start.title()
        start.names()
        mpos = py.mouse.get_pos()
        keys = py.key.get_pressed()

        startButton.blit(screen)
        
        if (keys[py.K_2] and keys[py.K_ESCAPE]and keys[py.K_SPACE] and keys[py.K_COMMA]):
            screen = py.display.set_mode((dimensions.current_w, dimensions.current_h))
            
        if (keys[py.K_1] and keys[py.K_ESCAPE] and keys[py.K_SPACE] and keys[py.K_COMMA]):
            screen = py.display.set_mode((dimensions.current_w, dimensions.current_h), py.FULLSCREEN)

        if startButton.hitbox.collidepoint(mpos):
            py.draw.rect(screen, (255, 255, 255), (((dimensions.current_w/3)-2, (dimensions.current_h/2)-2),
                                                   ((dimensions.current_w/3.3)+4, (dimensions.current_h/14)+4)), 2)

        py.display.update()
        for e in py.event.get():
            
            if e.type == py.QUIT:
                py.quit(); sys.exit()

            if startButton.hitbox.collidepoint(mpos) and e.type == py.MOUSEBUTTONUP:
                section = 1
                
    #---------------------------------------------------------------------------------
    # Transition Data
    dictionary_numbers = [rnd.randint(1, 48) for i in range(100)]
    dictionary_numbers = Duplicates(dictionary_numbers)
    currentQuestion = GetRandomDictionary(dictionary_numbers, question_dict)
    questionWritten = False
    submit = False
    currAnswer = ""
    questionX = dimensions.current_w/4.5
    questionY = 30
    
    #---------------------------------------------------------------------------------
    # CS Question Section
    while section == 1:
        screen.fill((0, 0, 0))
        keys = py.key.get_pressed()
        py.draw.rect(screen, (128, 128, 128), ((dimensions.current_w/4, dimensions.current_h/1.25), (dimensions.current_w/2, dimensions.current_h/9.2)), 2)
        
        if not questionWritten:
            currAnswer = ""
            QuestionPage(currentQuestion["problem"])
            questionWritten = True
        else:
            questionX = dimensions.current_w/4.5
            questionY = 30
            for line in currentQuestion["problem"]: 
                screen.blit(textFont.render(line, 0, (255, 255, 255)), (questionX, questionY))
                questionY += 51

        lb.draw_litlight(screen, answer_correct, lit, unlit, dimensions.current_w/4, dimensions.current_h/1.35)
        screen.blit(textFont.render(currAnswer, 1, (0, 255, 255)), (dimensions.current_w/3.8, dimensions.current_h/1.2))
        py.display.update()

        if submit:
            submit = False
            if currAnswer == currentQuestion["answer"]:
                answer_correct += 1
                if(answer_correct == 10):
                    py.quit(); sys.exit()
                
                questionWritten = False
                currentQuestion = GetRandomDictionary(dictionary_numbers, question_dict)
            else:
                questionWritten = False
                currentQuestion = GetRandomDictionary(dictionary_numbers, question_dict)
                answer_correct = 0
                
            currentAnswer = ""

        if len(dictionary_numbers) == 0:
            RestartRandom()
        
        if (keys[py.K_RALT] or keys[py.K_LALT]):
            section = 0
            break
            
        if (keys[py.K_1] and keys[py.K_ESCAPE] and keys[py.K_SPACE] and keys[py.K_COMMA]):
            screen = py.display.set_mode((dimensions.current_w, dimensions.current_h), py.FULLSCREEN)
            
        if (keys[py.K_2] and keys[py.K_ESCAPE]and keys[py.K_SPACE] and keys[py.K_COMMA]):
            screen = py.display.set_mode((dimensions.current_w, dimensions.current_h))
            
        if (keys[py.K_TAB] and keys[py.K_0]):
            py.quit() ; sys.exit()

        for event in py.event.get():
            
            if event.type == py.QUIT:
                py.quit() ; sys.exit()
                
            elif event.type == py.KEYDOWN:
                try:
                    if event.key == 13:
                        submit = True
                    elif event.key == 8:
                        currAnswer = currAnswer[:-1]
                    elif len(currAnswer) < 30:
                        currAnswer += chr(event.key)
                except Exception:
                    pass
                
#-------------------------------------------------------------------------------------
