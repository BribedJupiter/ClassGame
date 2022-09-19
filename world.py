import pygame
#Let's import the Car Class
from bird import Bird

def start_world_gen():
    pygame.init()

    CameraX = 0
    CameraY = 0
    #KU RGB Colors..
    TICK_RATE = 60 # this is what gives us 60 frames per second when we use this variable later..
    KU_BLUE = (0, 81, 186)
    KU_CRIMSON = (255, 200, 45)
    KU_YELLOW = (133, 137, 138)
    KU_GREY = (133, 137, 138)

    LIGHT_BLUE = (0, 180, 255)
    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
            
    SCREENWIDTH=400
    SCREENHEIGHT=500
    
    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("FlapPY Bird")
    
    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    playerBird = Bird(RED, 20, 30)
    playerBird.rect.x = 200
    playerBird.rect.y = 300
    
    # Add the bird to the list of objects
    all_sprites_list.add(playerBird)
    
    #Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()
    
    while carryOn:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        carryOn=False
    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                playerBird.moveLeft(5)
            if keys[pygame.K_RIGHT]:
                playerBird.moveRight(5)
            if keys[pygame.K_UP]:
                playerBird.moveUp(5)
            if keys[pygame.K_DOWN]:
                playerBird.moveDown(5)
            if keys[pygame.K_SPACE]:
                playerBird.bigJump(50)
            #Game Logic
            all_sprites_list.update()
            #Drawing on Screen
            screen.fill(LIGHT_BLUE)
            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            CameraX += 2
            CameraY += 2

            #screen.blit(playerBird,(x -CameraX,y -CameraY))
            #Refresh Screen
            pygame.display.flip()
    
            #Number of frames per secong e.g. 60
            clock.tick(TICK_RATE)
            playerBird.gravity(TICK_RATE / 9.81)
    pygame.quit() 