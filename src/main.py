import pygame

pygame.init()

screen = pygame.display.set_mode((1344, 756)) # 1920x1080 window
pygame.display.set_caption("Stickman") #the title thingy
clock = pygame.time.Clock()

running = True
while running == True:
    for event in pygame.event.get(): # checks for actions like close button being clicked
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 40)) #makes window's background kinda dark
    pygame.draw.rect(
        screen,
        (110,75,45),
        (0, screen.get_height() - 100, screen.get_width(), 100)
    ) # draws the ground at the bottom of window
    pygame.display.flip() # updates the window w everything thats been drawn until the next flip()
    clock.tick(60) # limits game to 60 fps

pygame.quit() #closes window and ends program