import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600)) # 800x600 window
pygame.display.set_caption("Stickman") #the title thingy
clock = pygame.time.Clock()

running = True
while running == True:
    for event in pygame.event.get(): # checks for actions like close button being clicked
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) #makes window's background white
    pygame.display.flip() # updates the window w everything thats been drawn until the next flip()
    clock.tick(60) # limits game to 60 fps

pygame.quit() #closes window and ends program