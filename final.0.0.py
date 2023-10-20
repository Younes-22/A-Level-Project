import pygame,sys,time, random, os
from pygame.locals import *
os.environ['SDL_VIDEO_CENTERED'] = '1'# centre 
pygame.init()#initialize game
pygame.mixer.init()

#creating the screen
SCREENWIDTH = 800
SCREENHEIGHT = 800
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)
mid_x = SCREENWIDTH/2
mid_y = SCREENHEIGHT/2

#music
pygame.mixer.music.load('Background.wav')# loads music
pygame.mixer.music.play(-1)# plays music
#colours
BLUE = (0, 65, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LBLUE = (173,216,230)
DBLUE = (0,0,139)
GREEN = (0, 180, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
BROWN = (92, 64, 51)
#caption for the game
pygame.display.set_caption("Flood Escape")
#fonts
font = pygame.font.Font("Fresh_Lychee.ttf", 100)
nfont = pygame.font.SysFont(None, 50)
fps = pygame.time.Clock()
#sprite starting coordinates
sprite_x = 0
sprite_y = 750


class Menu():
    def __init__(self):

        self.SCREEN = pygame.display.set_mode((800, 800))
        self.font_name = "Fresh_Lychee.ttf"
        self.start_box = pygame.draw.rect(SCREEN, WHITE,(290, 320, 190, 85))#start box
        self.help_box = pygame.draw.rect(SCREEN, WHITE,(290, 420, 190, 90))#help box
        self.quit_box = pygame.draw.rect(SCREEN, WHITE,(290, 520, 190, 80))#quit box
        self.backImg = pygame.image.load("floodbackground.jpg")#background image
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.level1 = False
        self.level2 = False


    
    def mouse(self):
        self.start_box = pygame.draw.rect(SCREEN, WHITE,(290, 320, 190, 85))#start box
        self.help_box = pygame.draw.rect(SCREEN, WHITE,(290, 420, 190, 90))#help box
        self.quit_box = pygame.draw.rect(SCREEN, WHITE,(290, 520, 190, 80))#quit box
        while True:
            M1.draw_text()
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                    print(self.mouse_x, self.mouse_y)#prints the coodinates of the mouse
                    if self.start_box.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box  
                        M1.start_screen()# call this function
                        print('start')
                    if self.help_box.collidepoint((self.mouse_x, self.mouse_y)):
                        M1.help_screen()
                        print('help')
                    if self.quit_box.collidepoint((self.mouse_x, self.mouse_y)) :
                            pygame.quit()


    def menu_background(self):
        self.backImg = pygame.transform.scale(self.backImg,(SCREENWIDTH, SCREENHEIGHT))#adjust size of the image
        SCREEN.blit(self.backImg, (0,0))

    def draw_text(self):
        M1.menu_background()
        self.start_box = pygame.draw.rect(SCREEN, WHITE,(290, 320, 190, 85))#start box
        self.help_box = pygame.draw.rect(SCREEN, WHITE,(290, 420, 190, 90))#help box
        self.quit_box = pygame.draw.rect(SCREEN, WHITE,(290, 530, 190, 80))#quit box
        self.start_button = font.render("Start", True, DBLUE)#Start
        SCREEN.blit(self.start_button, (290, 310))
        self.quit_text = font.render("Quit", True, DBLUE)#Quit
        SCREEN.blit(self.quit_text, (290, 515))
        self.help_text = font.render("Help", True, DBLUE)#Help
        SCREEN.blit(self.help_text, (SCREENWIDTH/2.7, SCREENHEIGHT/1.95))
        self.screen_title = font.render("Flood Escape", True, BLACK)
        SCREEN.blit(self.screen_title, (SCREENWIDTH/4, SCREENHEIGHT/8))    
        pygame.display.update()
       

    def start_screen(self):
        M1.menu_background()
        self.L1 = nfont.render("Level 1", True, BLACK)
        self.L1_box = pygame.draw.rect(SCREEN, WHITE,(50, 200, 120, 40))
        SCREEN.blit(self.L1, (50, 200))
        self.L2 = nfont.render("Level 2", True, BLACK)
        self.L2_box = pygame.draw.rect(SCREEN, WHITE,(50, 300, 120, 40))
        SCREEN.blit(self.L2, (50, 300))
        running = True
        while running:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.L1_box.collidepoint((self.mouse_x, self.mouse_y)):
                        main_game()
                        self.level1 = True
                    if self.L2_box.collidepoint((self.mouse_x, self.mouse_y)):#
                        main_game2()
                        self.level2 = True
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
     

    def help_screen(self):
        running = True
        while running:
            M1.menu_background()
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            self.con_info = pygame.image.load("controls info.png")#controls image
            self.con_info = pygame.transform.scale(self.con_info,(500, 500))#adjust size of the image
            SCREEN.blit(self.con_info, (SCREENWIDTH/4.5, SCREENHEIGHT/8.5))
            self.on_box = pygame.draw.rect(SCREEN, GREY,(SCREENWIDTH/4.5, SCREENHEIGHT/8.5, 50, 50))
            self.off_box = pygame.draw.rect(SCREEN, GREY,(SCREENWIDTH/3.5, SCREENHEIGHT/8.5, 50, 50))
            self.music_on = pygame.image.load('musicOn.png')
            self.music_on = pygame.transform.scale(self.music_on,(50, 50))
            SCREEN.blit(self.music_on, (SCREENWIDTH/4.5, SCREENHEIGHT/8.5))
            self.music_off = pygame.image.load('musicOff.png')
            self.music_off = pygame.transform.scale(self.music_off,(50, 50))
            SCREEN.blit(self.music_off, (SCREENWIDTH/3.5, SCREENHEIGHT/8.5))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.off_box.collidepoint((self.mouse_x, self.mouse_y)):
                        pygame.mixer.music.pause()# pause music
                    if self.on_box.collidepoint((self.mouse_x, self.mouse_y)):
                        pygame.mixer.music.unpause()# unpause music
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()

level1 = False
level2 = False
class Player(pygame.sprite.Sprite):
    def __init__(self,sprite_x, sprite_y):
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.stepIndex = 0
        self.vel = 0
        self.jump = False
        self.fall = True
        self.timeMS = 0#time in milliseconds
        self.timeS = 0#time in seconds
        self.timeM = 0#time in minutes
        self.B_colour = RED
        self.door = pygame.image.load('door.png')
        self.idleSprite = pygame.image.load('Idle_00.png')
        self.Rsprite = [pygame.image.load('RRun_00.png'),
        pygame.image.load('RRun_01.png'), pygame.image.load('RRun_02.png'),
        pygame.image.load('RRun_03.png'), pygame.image.load('RRun_04.png'),
        pygame.image.load('RRun_05.png'), pygame.image.load('RRun_06.png'),
        pygame.image.load('RRun_07.png'), pygame.image.load('RRun_08.png'),
        pygame.image.load('RRun_09.png'),]# right running sprites
        self.Lsprite = [pygame.image.load('LRun_00.png'),
        pygame.image.load('LRun_01.png'), pygame.image.load('LRun_02.png'),
        pygame.image.load('LRun_03.png'), pygame.image.load('LRun_04.png'),
        pygame.image.load('LRun_05.png'), pygame.image.load('LRun_06.png'),
        pygame.image.load('LRun_07.png'), pygame.image.load('LRun_08.png'),
        pygame.image.load('LRun_09.png'),]# left running sprites
        self.current_sprite = 0 # switching between images
        self.flood_y = 800 #flood y axis starting point
        self.bar = 100 # healthbar
        self.health = 100# health
        
        
    def timer(self):
        timer_top = nfont.render('Time:'+ str(self.timeM) + ':' + str(self.timeS), True, WHITE)#Start timer
        if self.sprite_x < 690 and self.sprite_y > 120 and self.health > 0:
            self.timeMS = self.timeMS + 2.4
            if self.timeMS >=100:
                self.timeS = self.timeS + 1# seconds
                self.timeMS = 0
            if self.timeS >= 60:
                self.timeM = self.timeM + 1
                self.timeS = 0
            SCREEN.blit(timer_top, (290, 10))#show timer
        else:
            SCREEN.blit(timer_top, (290, 10))
            
    

    def draw(self,keys):
        self.Rimage = self.Rsprite[self.current_sprite]
        self.Rimage = pygame.transform.scale(self.Rimage,(50, 50))#adjust size of the image
        self.idleSprite = pygame.transform.scale(self.idleSprite,(50, 50))
        self.Limage = self.Lsprite[self.current_sprite]
        self.Limage = pygame.transform.scale(self.Limage,(50, 50))
        if keys[pygame.K_RIGHT]:
            SCREEN.blit(self.Rimage, (self.sprite_x,self.sprite_y))
            self.current_sprite = self.current_sprite + 1 #constantly switch image to create animation
            if self.current_sprite >= 10:
                self.current_sprite = 0 #to make sure it loops
        if keys[pygame.K_LEFT]:
            SCREEN.blit(self.Limage, (self.sprite_x,self.sprite_y))
            self.current_sprite = self.current_sprite + 1
            if self.current_sprite >= 10:
                self.current_sprite = 0
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            SCREEN.blit(self.idleSprite, (self.sprite_x,self.sprite_y))#sprite stands still if user isn't controling it
        SCREEN.blit(self.door, (700, 85))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        

        
    def move(self, keys):
        if self.sprite_x < 700 or self.sprite_y > 150:
            if keys[pygame.K_RIGHT]:
                self.sprite_x = self.sprite_x + 8
            elif keys[pygame.K_LEFT]:
                self.sprite_x = self.sprite_x - 8
            if self.sprite_x <= 0:
                self.sprite_x = 0#stops the player from leaving the map from the west
            if self.sprite_x >= 750:
                self.sprite_x = 750 #stops the player from leaving the map from the east
            elif self.sprite_y <= 0:
                self.sprite_y = 0#stops the player from leaving the map from the north
            elif self.sprite_y >= 750:
                self.sprite_y = 750
                #self.fall = False
                self.vel = 1#stops the player from leaving the map from the south
                self.jump = False
        

    def gravity(self):
        if self.fall:
            self.sprite_y += 6.5 # how fast the player falls
           
    def jumps(self):
        if self.jump == False:
            self.jump = True# if player presses the up arrow key then jump is true
            self.vel = 15

    def update(self):
        if self.jump == True:
            self.sprite_y = self.sprite_y - self.vel # how high to jump
            self.vel -=1# player accelerates upwards until it reaches a stationary point where the sprite then deaccellerates 
            if self.vel == 0 and self.jump == True:
                self.fall = True # stops sprite from falling through surfaces
        
    def key(self):
        self.button = pygame.draw.rect(SCREEN, self.B_colour,(770, 730, 20, 20))#draw button
        if self.button.collidepoint((self.sprite_x + 20, self.sprite_y + 32)):
            self.B_colour = GREEN
        if self.B_colour == RED:# change the buttons colour if its pressed
            self.wall = pygame.draw.rect(SCREEN, GREY,(150, 0, 20, 200))#draw shut passage
            if self.wall.collidepoint((self.sprite_x + 50, self.sprite_y)):
                self.sprite_x = 100# stop the sprite from moving through the wall creating a barrier
            
    def key2(self):
        self.button = pygame.draw.rect(SCREEN, self.B_colour,(250, 780, 20, 20))#draw button
        if self.button.collidepoint((self.sprite_x + 20, self.sprite_y + 32)):
            self.B_colour = GREEN
        if self.B_colour == RED:# change the buttons colour if its pressed
            self.wall = pygame.draw.rect(SCREEN, GREY,(250, 0, 20, 200))#draw shut passage
            if self.wall.collidepoint((self.sprite_x + 50, self.sprite_y)):
                self.sprite_x = 200# stop the sprite from moving through the wall creating a barrier

        
    def plat(self):
        self.box = pygame.draw.rect(SCREEN, GREY,(750, 750, 50, 50))# bottom floor box
        if self.box.collidepoint((self.sprite_x + 50, self.sprite_y)):#if player touches the box horizontally
            self.sprite_x = 700
        if self.box.collidepoint((self.sprite_x + 10, self.sprite_y + 50)):#if player touches the box vertically
            self.jump = False
            self.sprite_y = 700
        self.box2 = pygame.draw.rect(SCREEN, GREY,(0, 650, 50, 50))#second floor box
        if self.box2.collidepoint((self.sprite_x, self.sprite_y)):#if player touches the box horizontally
            self.sprite_x = 50
        if self.box2.collidepoint((self.sprite_x + 10, self.sprite_y + 50)):#if player touches the box vertically
            self.jump = False
            self.sprite_y = 600
        self.p1 = pygame.draw.rect(SCREEN, GREY, (0, 700, 200, 50))#floor 1
        if self.p1.collidepoint((self.sprite_x + 10, self.sprite_y + 20)):
            self.sprite_x = 200
        if self.p1.collidepoint((self.sprite_x, self.sprite_y + 50)):# y = 650
            self.jump = False
            self.sprite_y = 650
        if self.p1.collidepoint((self.sprite_x, self.sprite_y)):
            self.sprite_y = 760
        self.p2 = pygame.draw.rect(SCREEN, GREY, (275, 700, 400, 50))#floor 2
        if self.p2.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 650
        if self.p2.collidepoint((self.sprite_x + 20, self.sprite_y)):
            self.sprite_y = 760
        self.p3 = pygame.draw.rect(SCREEN, GREY, (100, 575, 380, 50))#floor 2
        if self.p3.collidepoint((self.sprite_x + 20, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 525
        if self.p3.collidepoint((self.sprite_x + 20, self.sprite_y)):
            self.sprite_y = 650
        self.box3 = pygame.draw.rect(SCREEN, GREY, (430, 525, 50, 50))#third floor box
        if self.box3.collidepoint((self.sprite_x + 25, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 475
        if self.box3.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 380
        self.p6 = pygame.draw.rect(SCREEN, GREY, (480, 475, 200, 50))# third floor
        if self.p6.collidepoint((self.sprite_x, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 425
        if self.p6.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 430
        self.box4 = pygame.draw.rect(SCREEN, GREY, (680, 425, 120, 100))
        if self.box4.collidepoint((self.sprite_x, self.sprite_y + 50)):# third flood stair
            self.jump = False
            self.sprite_y = 375
        if self.box4.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 625
        self.p7 = pygame.draw.rect(SCREEN, GREY, (500, 375, 120, 50))# floating block 1
        if self.p7.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 325
        if self.p7.collidepoint((self.sprite_x + 30, self.sprite_y)):
            self.sprite_y = 420
        self.p8 = pygame.draw.rect(SCREEN, GREY, (300, 325, 120, 50))# floating block 2
        if self.p8.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 275
        self.p9 = pygame.draw.rect(SCREEN, GREY, (70, 275, 150, 50))# floating block 3
        if self.p9.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 225
        self.box5 = pygame.draw.rect(SCREEN, GREY, (0, 225, 50, 50))# floating block 4
        if self.box5.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 175
        self.p10 = pygame.draw.rect(SCREEN, GREY, (100, 175, 700, 50))
        if self.p10.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 125
        if self.p10.collidepoint((self.sprite_x + 30, self.sprite_y)):
            self.sprite_y = 220

    def plat2(self):
        self.p1 = pygame.draw.rect(SCREEN, GREY,(170, 750, 50, 50))# bottom floor box
        if self.p1.collidepoint((self.sprite_x + 50, self.sprite_y)):#if player touches the box horizontally:
            self.sprite_x = 120
        if self.p1.collidepoint((self.sprite_x, self.sprite_y)):#if player touches the box horizontally
            self.sprite_x = 220
        if self.p1.collidepoint((self.sprite_x + 10, self.sprite_y + 50)):#if player touches the box horizontally
            self.jump = False
            self.sprite_y = 700
        self.p2 = pygame.draw.rect(SCREEN, GREY,(220, 700, 200, 50))# bottom floor box
        if self.p2.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 170
        if self.p2.collidepoint((self.sprite_x , self.sprite_y)):
            self.sprite_x = 400
        if self.p2.collidepoint((self.sprite_x, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 650
        if self.p2.collidepoint((self.sprite_x, self.sprite_y - 48)):
            self.sprite_y = 760
        self.p3 = pygame.draw.rect(SCREEN, GREY,(500, 750, 50, 50))
        if self.p3.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 450
        if self.p3.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 700
        self.p4 = pygame.draw.rect(SCREEN, GREY,(550, 700, 50, 50))
        if self.p4.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 500
        if self.p4.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 650
        self.p5 = pygame.draw.rect(SCREEN, GREY,(600, 650, 50, 50))
        if self.p5.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 550
        if self.p5.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 600
        self.p6 = pygame.draw.rect(SCREEN, GREY,(650, 600, 50, 50))
        if self.p6.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 600
        if self.p6.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 550
        self.p7 = pygame.draw.rect(SCREEN, GREY,(700, 550, 50, 50))
        if self.p7.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 650
        if self.p7.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 500
        self.p8 = pygame.draw.rect(SCREEN, GREY,(750, 500, 50, 50))
        if self.p8.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 700
        if self.p8.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 450
        self.p9 = pygame.draw.rect(SCREEN, GREY,(400, 450, 300, 50))
        if self.p9.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 400
        if self.p9.collidepoint((self.sprite_x, self.sprite_y)):
            self.sprite_y = 480
            self.sprite_x = 700 
        self.p10 = pygame.draw.rect(SCREEN, GREY,(0, 450, 300, 50))
        if self.p10.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 400
        if self.p10.collidepoint((self.sprite_x, self.sprite_y)):
            self.sprite_y = 480
            self.sprite_x = 300
        self.p11 = pygame.draw.rect(SCREEN, GREY,(0, 400, 25, 50))
        if self.p11.collidepoint((self.sprite_x , self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 350
        if self.p11.collidepoint((self.sprite_x, self.sprite_y)):
            self.sprite_x = 25
        self.p12 = pygame.draw.rect(SCREEN, GREY,(75, 325, 50, 50))
        if self.p12.collidepoint((self.sprite_x + 30, self.sprite_y)):
            self.sprite_x = 75
        if self.p12.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 275
        if self.p12.collidepoint((self.sprite_x + 10, self.sprite_y)):
            self.sprite_y = 380
        self.p13 = pygame.draw.rect(SCREEN, GREY,(125, 275, 50, 50))
        if self.p13.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 75
        if self.p13.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 225
        self.p14 = pygame.draw.rect(SCREEN, GREY,(175, 225, 50, 50))
        if self.p14.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 125
        if self.p14.collidepoint((self.sprite_x + 30, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 175
        self.p15 = pygame.draw.rect(SCREEN, GREY,(225, 175, 575, 50))
        if self.p15.collidepoint((self.sprite_x + 50, self.sprite_y)):
            self.sprite_x = 175
        if self.p15.collidepoint((self.sprite_x + 50, self.sprite_y + 50)):
            self.jump = False
            self.sprite_y = 125
        print(self.sprite_x, self.sprite_y)


    def mob(self):
        self.flood = pygame.draw.rect(SCREEN, DBLUE, (0, self.flood_y, 800, 750))
        if not self.health <= 0:
            self.flood_y = self.flood_y - 0.5 # causes the flood to gradually move up
        if self.flood_y <= 200:
            self.flood_y = 200# stops the flood from reaching a certain point
        if self.flood.collidepoint(self.sprite_x, self.sprite_y + 45):
            self.health = self.health - 1
            if self.bar > 0:
                self.bar = self.bar - 1
        if self.health <= 0:
            player.endScreen()
        if self.sprite_x >= 690 and self.sprite_y <= 125:
            player.winScreen()

    def mob2(self):
        self.flood = pygame.draw.rect(SCREEN, DBLUE, (0, self.flood_y, 800, 750))
        if not self.health <= 0:
            self.flood_y = self.flood_y - 0.7 # causes the flood to gradually move up
        if self.flood_y <= 200:
            self.flood_y = 200# stops the flood from reaching a certain point
        if self.flood.collidepoint(self.sprite_x, self.sprite_y + 25):
            self.health = self.health - 1
            if self.bar > 0:
                self.bar = self.bar - 1
        if self.health <= 0:
            player.endScreen2()
        if self.sprite_x >= 690 and self.sprite_y <= 125:
            player.winScreen2()

            
    def healthbar(self):
        self.outline = pygame.draw.rect(SCREEN, WHITE, (680, 10, 100, 30))
        self.healthbar1 = pygame.draw.rect(SCREEN, GREEN, (680, 10, self.bar, 30))


    def reset_game(self): #resets all game variables
        self.health = 100
        self.timeMS = 0
        self.timeS = 0
        self.timeM = 0
        self.vel = 0
        self.jump = False
        self.fall = True
        self.sprite_x = 0
        self.sprite_y = 800
        self.flood_y = 800
        self.bar = 100
        self.B_colour = RED
        
    def level_back(self):
        self.LbackImg = pygame.image.load("warehouse.png")#background image
        self.LbackImg = pygame.transform.scale(self.LbackImg,(SCREENWIDTH, SCREENHEIGHT))#adjust size of the image
        SCREEN.blit(self.LbackImg, (0,0))

    def level_back2(self):
        self.LbackImg2 = pygame.image.load("back2.png")#background image
        self.LbackImg2 = pygame.transform.scale(self.LbackImg2,(SCREENWIDTH, SCREENHEIGHT))#adjust size of the image
        SCREEN.blit(self.LbackImg2, (0,0))

    def winScreen(self):
        self.end_screen = pygame.draw.rect(SCREEN, BROWN, (100, 100, 600, 600))
        self.end_mes = font.render('Level 1 Complete', True, WHITE)#write game over
        SCREEN.blit(self.end_mes, (120, 150))
        self.retry_button = pygame.draw.rect(SCREEN, WHITE, (200, 350, 80, 80))
        self.retry = pygame.image.load('retry.png')# retry icon
        self.retry = pygame.transform.scale(self.retry,(80, 80))#reshape icon
        SCREEN.blit(self.retry, (200, 350))
        self.previous_button = pygame.draw.rect(SCREEN, WHITE, (500, 350, 80, 80))
        self.previous = pygame.image.load('previous.png')# retry icon
        self.previous = pygame.transform.scale(self.previous,(80, 80))#reshape icon
        SCREEN.blit(self.previous, (500, 350))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                if self.retry_button.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box
                    count = 0
                    player.reset_game()# reset scores
                    main_game()# run game again
                    print('retry')
                if self.previous_button.collidepoint((self.mouse_x, self.mouse_y)):# go back to menu
                    player.reset_game()
                    M1.mouse()

    def winScreen2(self):
        self.end_screen = pygame.draw.rect(SCREEN, BROWN, (100, 100, 600, 600))
        self.end_mes = font.render('Level 2 Complete', True, WHITE)#write game over
        SCREEN.blit(self.end_mes, (120, 150))
        self.retry_button = pygame.draw.rect(SCREEN, WHITE, (200, 350, 80, 80))
        self.retry = pygame.image.load('retry.png')# retry icon
        self.retry = pygame.transform.scale(self.retry,(80, 80))#reshape icon
        SCREEN.blit(self.retry, (200, 350))
        self.previous_button = pygame.draw.rect(SCREEN, WHITE, (500, 350, 80, 80))
        self.previous = pygame.image.load('previous.png')# retry icon
        self.previous = pygame.transform.scale(self.previous,(80, 80))#reshape icon
        SCREEN.blit(self.previous, (500, 350))
        self.retry_mes = nfont.render('Retry', True, GREY)#write Retrt
        SCREEN.blit(self.retry_mes, (200, 450))
        self.exit_mes = nfont.render('Exit', True, GREY)#write Exit
        SCREEN.blit(self.exit_mes, (500, 450))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                if self.retry_button.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box
                    count = 0
                    player.reset_game()# reset scores
                    main_game2()# run game again
                    print('retry')
                if self.previous_button.collidepoint((self.mouse_x, self.mouse_y)):# go back to menu
                    player.reset_game()
                    M1.mouse()


    def endScreen(self):
        self.end_screen = pygame.draw.rect(SCREEN, BROWN, (100, 100, 600, 600))
        self.end_mes = font.render('Game Over', True, WHITE)#write game over
        SCREEN.blit(self.end_mes, (200, 100))
        self.retry_button = pygame.draw.rect(SCREEN, WHITE, (200, 350, 80, 80))
        self.retry = pygame.image.load('retry.png')# retry icon
        self.retry = pygame.transform.scale(self.retry,(80, 80))#reshape icon
        SCREEN.blit(self.retry, (200, 350))
        self.previous_button = pygame.draw.rect(SCREEN, WHITE, (500, 350, 80, 80))
        self.previous = pygame.image.load('previous.png')# retry icon
        self.previous = pygame.transform.scale(self.previous,(80, 80))#reshape icon
        SCREEN.blit(self.previous, (500, 350))
        self.retry_mes = nfont.render('Retry', True, GREY)#write Retrt
        SCREEN.blit(self.retry_mes, (200, 450))
        self.exit_mes = nfont.render('Exit', True, GREY)#write Exit
        SCREEN.blit(self.exit_mes, (500, 450))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                if self.retry_button.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box
                    count = 0
                    player.reset_game()# reset scores
                    main_game()# run game again
                    print('retry')
                if self.previous_button.collidepoint((self.mouse_x, self.mouse_y)):# go back to menu
                    player.reset_game()
                    M1.mouse()

    def endScreen2(self):
        self.end_screen = pygame.draw.rect(SCREEN, BROWN, (100, 100, 600, 600))
        self.end_mes = font.render('Game Over', True, WHITE)#write game over
        SCREEN.blit(self.end_mes, (200, 100))
        self.retry_button = pygame.draw.rect(SCREEN, WHITE, (200, 350, 80, 80))
        self.retry = pygame.image.load('retry.png')# retry icon
        self.retry = pygame.transform.scale(self.retry,(80, 80))#reshape icon
        SCREEN.blit(self.retry, (200, 350))
        self.previous_button = pygame.draw.rect(SCREEN, WHITE, (500, 350, 80, 80))
        self.previous = pygame.image.load('previous.png')# retry icon
        self.previous = pygame.transform.scale(self.previous,(80, 80))#reshape icon
        SCREEN.blit(self.previous, (500, 350))
        self.retry_mes = nfont.render('Retry', True, GREY)#write Retrt
        SCREEN.blit(self.retry_mes, (200, 450))
        self.exit_mes = nfont.render('Exit', True, GREY)#write Exit
        SCREEN.blit(self.exit_mes, (500, 450))
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                if self.retry_button.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box
                    count = 0
                    player.reset_game()# reset scores
                    main_game2()# run game again
                    print('retry')
                if self.previous_button.collidepoint((self.mouse_x, self.mouse_y)):# go back to menu
                    player.reset_game()
                    M1.mouse()

    #def update2()
     #   if self.level1

    def pause(self):
        pausing = True
        while pausing:
            self.end_screen = pygame.draw.rect(SCREEN, BROWN, (100, 90, 600, 600))
            self.con_info = pygame.image.load("controls info.png")#controls image
            self.con_info = pygame.transform.scale(self.con_info,(300, 200))
            SCREEN.blit(self.con_info, (100, 490))
            self.pause_mes = font.render('Pause', True, WHITE)#write Pause
            SCREEN.blit(self.pause_mes, (300, 100))
            self.retry_mes = nfont.render('Retry', True, GREY)#write Retrt
            SCREEN.blit(self.retry_mes, (200, 450))
            self.exit_mes = nfont.render('Exit', True, GREY)#write Exit
            SCREEN.blit(self.exit_mes, (500, 450))
            self.on_box = pygame.draw.rect(SCREEN, GREY,(SCREENWIDTH/4.5, SCREENHEIGHT/8.5, 50, 50))
            self.off_box = pygame.draw.rect(SCREEN, GREY,(SCREENWIDTH/3.5, SCREENHEIGHT/8.5, 50, 50))
            self.retry_button = pygame.draw.rect(SCREEN, WHITE, (200, 350, 80, 80))
            self.retry = pygame.image.load('retry.png')# retry icon
            self.retry = pygame.transform.scale(self.retry,(80, 80))#reshape icon
            SCREEN.blit(self.retry, (200, 350))
            self.previous_button = pygame.draw.rect(SCREEN, WHITE, (500, 350, 80, 80))
            self.previous = pygame.image.load('previous.png')# retry icon
            self.previous = pygame.transform.scale(self.previous,(80, 80))#reshape icon
            self.music_on = pygame.image.load('musicOn.png')
            self.music_on = pygame.transform.scale(self.music_on,(50, 50))
            SCREEN.blit(self.music_on, (SCREENWIDTH/4.5, SCREENHEIGHT/8.5))
            self.music_off = pygame.image.load('musicOff.png')
            self.music_off = pygame.transform.scale(self.music_off,(50, 50))
            SCREEN.blit(self.music_off, (SCREENWIDTH/3.5, SCREENHEIGHT/8.5))
            SCREEN.blit(self.previous, (500, 350))
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                    if self.retry_button.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box
                        count = 0
                        player.reset_game()# reset scores
                        main_game()# run game again
                        print('retry')
                    if self.previous_button.collidepoint((self.mouse_x, self.mouse_y)):# go back to menu
                        player.reset_game()
                        M1.mouse()
                    if self.off_box.collidepoint((self.mouse_x, self.mouse_y)):
                        pygame.mixer.music.pause()# pause music
                    if self.on_box.collidepoint((self.mouse_x, self.mouse_y)):
                        pygame.mixer.music.unpause()# unpause music
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pausing = False
                    pygame.display.update() #update
            
    def pause2(self):
        pausing = True
        while pausing:
            self.end_screen = pygame.draw.rect(SCREEN, BROWN, (100, 90, 600, 600))
            self.con_info = pygame.image.load("controls info.png")#controls image
            self.con_info = pygame.transform.scale(self.con_info,(300, 200))
            SCREEN.blit(self.con_info, (100, 490))
            self.pause_mes = font.render('Pause', True, WHITE)#write Pause
            SCREEN.blit(self.pause_mes, (300, 100))
            self.retry_mes = nfont.render('Retry', True, GREY)#write Retrt
            SCREEN.blit(self.retry_mes, (200, 450))
            self.exit_mes = nfont.render('Exit', True, GREY)#write Exit
            SCREEN.blit(self.exit_mes, (500, 450))
            self.on_box = pygame.draw.rect(SCREEN, GREY,(SCREENWIDTH/4.5, SCREENHEIGHT/8.5, 50, 50))
            self.off_box = pygame.draw.rect(SCREEN, GREY,(SCREENWIDTH/3.5, SCREENHEIGHT/8.5, 50, 50))
            self.retry_button = pygame.draw.rect(SCREEN, WHITE, (200, 350, 80, 80))
            self.retry = pygame.image.load('retry.png')# retry icon
            self.retry = pygame.transform.scale(self.retry,(80, 80))#reshape icon
            SCREEN.blit(self.retry, (200, 350))
            self.previous_button = pygame.draw.rect(SCREEN, WHITE, (500, 350, 80, 80))
            self.previous = pygame.image.load('previous.png')# retry icon
            self.previous = pygame.transform.scale(self.previous,(80, 80))#reshape icon
            self.music_on = pygame.image.load('musicOn.png')
            self.music_on = pygame.transform.scale(self.music_on,(50, 50))
            SCREEN.blit(self.music_on, (SCREENWIDTH/4.5, SCREENHEIGHT/8.5))
            self.music_off = pygame.image.load('musicOff.png')
            self.music_off = pygame.transform.scale(self.music_off,(50, 50))
            SCREEN.blit(self.music_off, (SCREENWIDTH/3.5, SCREENHEIGHT/8.5))
            SCREEN.blit(self.previous, (500, 350))
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #gets the positions of the mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:# if the mouse is clicked
                    if self.retry_button.collidepoint((self.mouse_x, self.mouse_y)):# if mouse is clicked in the start box
                        count = 0
                        player.reset_game()# reset scores
                        main_game2()# run game again
                        print('retry')
                    if self.previous_button.collidepoint((self.mouse_x, self.mouse_y)):# go back to menu
                        player.reset_game()
                        M1.mouse()
                    if self.off_box.collidepoint((self.mouse_x, self.mouse_y)):
                        pygame.mixer.music.pause()# pause music
                    if self.on_box.collidepoint((self.mouse_x, self.mouse_y)):
                        pygame.mixer.music.unpause()# unpause music
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pausing = False
                    pygame.display.update() #update

def main_game():# calls all the gameplay functions once the user presses level 1
    count = 0
    level1 = True
    while True:
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        count = count + 1
        player.level_back()
        player.update()
        player.timer()
        player.gravity()
        player.move(keys)
        player.draw(keys)
        player.plat()
        player.key()
        player.healthbar()
        player.update() #all the main game functions are called
        if count >= 150: # countdown for flood to start moving
            player.mob()
        pygame.display.update()
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:#if a key is pressed
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:# if up arrow key or space bar is pressed
                    player.jumps()
                if event.key == pygame.K_p:# if p key is pressed
                    player.pause()

def main_game2():# calls all the gameplay functions once the user presses level 2
    count = 0
    level2 = True
    while True:
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        count = count + 1
        player.level_back2()
        player.update()
        player.timer()
        player.gravity()
        player.move(keys)
        player.draw(keys)
        player.plat2()
        player.key2()
        player.healthbar()
        player.update() #all the main game functions are called
        if count >= 150: # countdown for flood to start moving
            player.mob2()
        pygame.display.update()
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:#if a key is pressed
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:# if up arrow key or space bar is pressed
                    player.jumps()
                if event.key == pygame.K_p:# if p key is pressed
                    player.pause2()

player = Player(0,750)
M1 = Menu()
M1.mouse()# contains all the menu functions and dosen't need to be in a loop
pygame.display.update()
fps.tick(120)


