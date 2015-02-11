import pygame, sys
from pygame.locals import *
    
class paddle:
    def __init__(self, xPos, yPos):
        self.vx = 0.0
        self.vy = 0.0
        self.xPos = xPos
        self.yPos = yPos
        self.player = pygame.draw.rect(windowSurface, WHITE, (self.xPos, self.yPos, 10, 40))           
 
class ball:
    def __init__(self):
        self.vx = 2.5
        self.vy = 2.5
        self.ball = pygame.draw.rect(windowSurface, WHITE, (200, 200, 10, 10), 0)
   
    def respawnBall(self):
        pygame.time.wait(500)
        self.ball = pygame.draw.rect(windowSurface, WHITE, (195, 195, 10, 10), 0)
    
    def moveBall(self):
        if self.vx == 2.5:
            self.ball.right += self.vx
        if self.vx == -2.5:
            self.ball.left += self.vx
        if self.vy == 2.5:
            self.ball.bottom += self.vy
        if self.vy == -2.5:
            self.ball.top += self.vy
    
    def collideBall(self, paddle):
        if self.ball.right > WINDOWWIDTH - 10.0:
            s1.playerScore += 1
            print(s1.playerScore)
                    
            self.respawnBall()
        if self.ball.left < 0 + 10.0:
            s2.playerScore += 1
            print(s2.playerScore)
            self.respawnBall()
        if self.ball.top < WINDOWHEIGHT + 10.0:
            self.vy = 2.5
        if self.ball.bottom > WINDOWDEPTH - 10.0:
            self.vy = -2.5
   
        if self.ball.left < paddle.right and self.ball.left > paddle.right - 5.0: # COLLIDE FROM RIGHT
            if self.ball.bottom > paddle.top and self.ball.top < paddle.bottom:                
                if self.vy == 2.5:
                    self.vy = 2.5
                    self.vx = 2.5
                else:
                    self.vy = -2.5
                    self.vx = 2.5
                       
        if self.ball.right > paddle.left and self.ball.right < paddle.left + 5.0: # COLLIDE FROM LEFT
            if self.ball.bottom > paddle.top and self.ball.top < paddle.bottom:
                if self.vy == 2.5:
                    self.vy = 2.5
                    self.vx = -2.5
                else:
                    self.vy = -2.5
                    self.vx = -2.5
                       
        if self.ball.bottom > paddle.top and self.ball.bottom < paddle.top + 5.0: # COLLIDE FROM TOP
            if self.ball.right > paddle.left and self.ball.left < paddle.right:
                if self.vx == 2.5:
                    self.vx = 2.5
                    self.vy = -2.5
                else:
                    self.vx = -2.5
                    self.vy = -2.5
    
        if self.ball.top < paddle.bottom and self.ball.top > paddle.bottom - 5.0: # COLLIDE FROM BOTTOM           
            if self.ball.right > paddle.left and self.ball.left < paddle.right:
                if self.vx == 2.5:
                    self.vx = 2.5
                    self.vy = 2.5
                else:
                    self.vx = -2.5
                    self.vy = 2.5
   
class score:
    def __init__(self):
        self.playerScore = 0
           
    def drawNum(self, x):
        if self.playerScore == 0:
            # DRAW ZERO
            self.ZERO = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (115 + x, 10), (115 + x, 40), (85 + x, 40)))
            self.ZERO2 = pygame.draw.polygon(windowSurface, BLACK, ((95 + x, 20), (105 + x, 20), (105 + x, 30), (95 + x, 30)))
 
        if self.playerScore == 1:
            # DRAW ONE
            self.ONE = pygame.draw.polygon(windowSurface, WHITE, ((95 + x, 10), (105 + x, 10), (105 + x, 40), (95 + x, 40)))
 
        if self.playerScore == 2:
            # DRAW TWO
            self.TWO = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (115 + x, 10), (115 + x, 28), (95 + x, 28), (95 + x, 34), (115 + x, 34), (115 + x, 40), (85 + x, 40), (85 + x, 22), (105 + x, 22), (105 + x, 16), (85 + x, 16)))
  
        if self.playerScore == 3:
            # DRAW THREE
            self.THREE = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (115 + x, 10), (115 + x, 40), (85 + x, 40), (85 + x, 34), (109 + x, 34), (109 + x, 28), (91 + x, 28), (91 + x, 22), (109 + x, 22), (109 + x, 16), (85 + x, 16)))
  
        if self.playerScore == 4:
            # DRAW FOUR
            self.FOUR = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (91 + x, 10), (91 + x, 28), (109 + x, 28), (109 + x, 10), (115 + x, 10), (115 + x, 40), (109 + x, 40), (109 + x, 34), (85 + x, 34)))
 
        if self.playerScore == 5:
            # DRAW FIVE
            self.FIVE = pygame.draw.polygon(windowSurface, WHITE, ((91 + x, 16), (91 + x, 22), (115 + x, 22), (115 + x, 40), (85 + x, 40), (85 + x, 34), (109 + x, 34), (109 + x, 28), (85 + x, 28), (85 + x, 10), (115 + x, 10), (115 + x, 16)))
 
        if self.playerScore == 6:        
            # DRAW SIX
            self.SIX = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (85 + x, 40), (115 + x, 40), (115 + x, 22), (91 + x, 22), (91 + x, 10)))
            self.SIX2 = pygame.draw.polygon(windowSurface, BLACK, ((91 + x, 28), (91 + x, 34), (109 + x, 34), (109 + x, 28)))
 
        if self.playerScore == 7:
            # DRAW SEVEN
            self.SEVEN = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (115 + x, 10), (115 + x, 40), (109 + x, 40), (109 + x, 16), (85 + x, 16)))
 
        if self.playerScore == 8:
            # DRAW EIGHT
            self.EIGHT = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (115 + x, 10), (115 + x, 40), (85 + x, 40)))
            self.EIGHT2 = pygame.draw.polygon(windowSurface, BLACK, ((91 + x, 16), (91 + x, 22), (109 + x, 22), (109 + x, 16)))
            self.EIGHT3 = pygame.draw.polygon(windowSurface, BLACK, ((91 + x, 28), (91 + x, 34), (109 + x, 34), (109 + x, 28)))
 
        if self.playerScore == 9:
            # DRAW NINE
            self.NINE = pygame.draw.polygon(windowSurface, WHITE, ((85 + x, 10), (85 + x, 28), (109 + x, 28), (109 + x, 40), (115 + x, 40), (115 + x, 10)))
            self.NINE2 = pygame.draw.polygon(windowSurface, BLACK, ((91 + x, 16), (91 + x, 22), (109 + x, 22), (109 + x, 16)))        

        if self.playerScore == 10:
            # DRAW TEN
            self.TEN1 = pygame.draw.polygon(windowSurface, WHITE, ((75 + x, 10), (81 + x, 10), (81 + x, 40), (75 + x, 40)))
            self.TEN2 = pygame.draw.polygon(windowSurface, WHITE, ((87 + x, 10), (111 + x, 10), (111 + x, 40), (87 + x, 40)))
            self.TEN3 = pygame.draw.polygon(windowSurface, BLACK, ((93 + x, 16), (105 + x, 16), (105 + x, 34), (93 + x, 34)))
            
    def winner(self):
        if self.playerScore > 9:
            # STOP BALL AND PLAYER MOVEMENT
            b1.vx = 0.0
            b1.vy = 0.0
            p1.vx = 0.0
            p2.vx = 0.0

            # DRAW WINNING MESSAGE            
            pygame.draw.polygon(windowSurface, WHITE, ((25, 360), (43, 360), (43, 378), (31, 378), (31, 390), (25, 390)))
            pygame.draw.polygon(windowSurface, BLACK, ((31, 366), (37, 366), (37, 372), (31, 372)))

            pygame.draw.polygon(windowSurface, WHITE, ((49, 360), (55, 360), (55, 390), (49, 390)))

            pygame.draw.polygon(windowSurface, WHITE, ((67, 360), (73, 360), (73, 384), (76, 384), (76, 372), (82, 372), (82, 384), (85, 384), (85, 360), (91, 360), (91, 390), (67, 390)))

            pygame.draw.polygon(windowSurface, WHITE, ((97, 360), (103, 360), (103, 390), (97, 390)))

            pygame.draw.polygon(windowSurface, WHITE, ((109, 360), (127, 360), (127, 390), (121, 390), (121, 360), (121, 366), (115, 366), (115, 390), (109, 390)))

            pygame.draw.polygon(windowSurface, WHITE, ((133, 360), (151, 360), (151, 366), (139, 366), (139, 372), (151, 372), (151, 390), (133, 390), (133, 384), (145, 384), (145, 378), (133, 378))) 
            
            
           
           
   
def background(x, y):
    BLOCK = pygame.draw.rect(windowSurface, WHITE, (x, y, 10, 10))        
    pygame.draw.rect(windowSurface, WHITE, BLOCK)
            
def main():       
    gameIsPlaying = True
    
    while gameIsPlaying:
  
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == ord('q'): # CLOSE PROGRAM
                    pygame.quit()
                    sys.exit()
                if event.key == ord('z'): # MOVE DOWN
                    p1.vy = 5.0                   
                if event.key == ord('a'): # MOVE UP
                   #easter egg
                    p1.vy = -5.0                   
                if event.key == ord('m'):
                    p2.vy = 5.0                   
                if event.key == ord('j'):
                    p2.vy = -5.0                   
  
            if event.type == KEYUP:
                if event.key == ord('z'):
                    p1.vy = 0.0
                if event.key == ord('a'):
                    p1.vy = 0.0
                if event.key == ord('m'):
                    p2.vy = 0.0
                if event.key == ord('j'):
                    p2.vy = 0.0
 
        if p1.vy == 5.0 and p1.player.bottom < WINDOWDEPTH:
            p1.player.bottom += p1.vy # MOVE DOWN               
    
        if p1.vy == -5.0 and p1.player.top > WINDOWHEIGHT:
            p1.player.top += p1.vy # MOVE UP
 
        if p2.vy == 5.0 and p2.player.bottom < WINDOWDEPTH:
            p2.player.bottom += p2.vy # MOVE DOWN               
    
        if p2.vy == -5.0 and p2.player.top > WINDOWHEIGHT:
            p2.player.top += p2.vy # MOVE UP           
                     
  
        windowSurface.fill(BLACK)  
          
        b1.moveBall()
        b1.collideBall(p1.player)
        b1.collideBall(p2.player)
 
        s1.drawNum(0)
        s2.drawNum(200)

        s1.winner()
        s2.winner()     
   
        pygame.draw.line(windowSurface, WHITE, (0, WINDOWHEIGHT), (WINDOWWIDTH, WINDOWHEIGHT), 2)
        pygame.draw.line(windowSurface, WHITE, (0, WINDOWHEIGHT), (0, WINDOWDEPTH), 2)
        pygame.draw.line(windowSurface, WHITE, (WINDOWWIDTH - 2.0, WINDOWHEIGHT), (WINDOWWIDTH - 2.0, WINDOWDEPTH), 2)
        pygame.draw.line(windowSurface, WHITE, (0, WINDOWDEPTH), (WINDOWWIDTH, WINDOWDEPTH), 2)
    
        pygame.draw.rect(windowSurface, WHITE, p1.player)
        pygame.draw.rect(windowSurface, WHITE, p2.player)
        pygame.draw.rect(windowSurface, WHITE, b1.ball)
           
        background(195, 55)
        background(195, 75)
        background(195, 95)
        background(195, 115)
        background(195, 135)
        background(195, 155)
        background(195, 175)
        background(195, 195)
        background(195, 215)
        background(195, 235)
        background(195, 255)
        background(195, 275)
        background(195, 295)
        background(195, 315)
        background(195, 335)       
    
        pygame.display.update()
        mainClock.tick(60)
   
pygame.init()
mainClock = pygame.time.Clock()
    
WINDOWHEIGHT = 50
WINDOWWIDTH = 400
WINDOWDEPTH = 350
    
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
    
windowSurface = pygame.display.set_mode((WINDOWWIDTH, 400))
pygame.display.set_caption("Pong")
   
blockXPos = 190
blockYPos = 20
    
p1 = paddle(50, 180)
p2 = paddle(350, 180)
    
b1 = ball()
   
s1 = score()
s2 = score()
    
main()
