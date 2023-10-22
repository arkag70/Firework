import pygame
import threading
from random import random, randint, choice
from playsound import playsound

sound_file = 'firework.mp3'
width, height = 800, 600
g = 0.05
BLASTFORCE = -0.25
FRAGMENTS = 50
MARGIN = 50
colors = [(255,0,0,255), (0,0,255,255), (0,255,0,255), (255,255,0,255), (255,192,203,255), (148,0,211,255), (255,255,255,255), (0,255,255,255)]

def burstSound():
    playsound(sound_file)

class Circle:

    def __init__(self, screen, center, radius, color) -> None:
        self.screen = screen
        self.color = color
        self.x, self.y = center
        self.radius = radius
        self.xvel = 0
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0

class Cracker:

    def __init__(self, screen, color) -> None:
        self.x = randint(MARGIN, width-MARGIN)
        self.y = height - MARGIN
        self.color = color
        self.screen = screen
        self.circle = Circle(screen, (self.x, self.y), 6, color)
        self.fragments = []
        self.peaked = False
        self.lifespan = 150

    def applyForce(self, force, circle = None):
        if circle == None:
            self.circle.xacc , self.circle.yacc = force
        else:
            circle.xacc , circle.yacc = force

    def blast(self):
        self.peaked = True
        for fragment in self.fragments:
            xforce = random() * 0.06 - 0.03
            yforce = random() * -0.06
            self.applyForce((xforce, yforce), fragment)

    def stopFireWork(self):
        self.circle = None

    def updateFirework(self):

        if not self.peaked:
            self.circle.x += self.circle.xvel
            self.circle.y += self.circle.yvel

            self.circle.xvel += self.circle.xacc
            self.circle.yvel += self.circle.yacc

            self.circle.yacc += g

        else:
            self.lifespan -= 1
            if self.lifespan > 0:
                for fragment in self.fragments:

                        fragment.x += fragment.xvel
                        fragment.y += fragment.yvel

                        fragment.xvel += fragment.xacc
                        fragment.yvel += fragment.yacc

                        fragment.yacc += g / 30
            else:
                self.fragments = []

    def burstSoundThread(self):

        thread = threading.Thread(target=burstSound)
        thread.daemon = True
        thread.start()

    def constructFragments(self):

        self.burstSoundThread()

        for _ in range(FRAGMENTS):
            color = self.color if not self.color == "blue" else choice(colors)
            self.fragments.append(Circle(self.screen, (self.circle.x, self.circle.y), 2, color))

    def update(self):

        self.updateFirework()

        if self.circle != None:
            if self.circle.yvel > 0 and self.circle.yvel < 0.00001:
                
                self.constructFragments()
                self.stopFireWork()
                self.blast()

    def show(self):
        
        if self.circle != None:
            pygame.draw.circle(self.screen, self.circle.color, (self.circle.x, self.circle.y), self.circle.radius)
        for fragment in self.fragments:
            surface = pygame.Surface((fragment.radius * 2 - 1, fragment.radius * 2 -1), pygame.SRCALPHA)   # per-pixel alpha
            r,g,b,a = fragment.color
            a /= 1.7
            a = int(a)
            surface.fill((r,g,b,a))                         # notice the alpha value in the color
            pygame.draw.circle(surface, fragment.color, (fragment.x, fragment.y), fragment.radius)
            self.screen.blit(surface, (fragment.x,fragment.y))
