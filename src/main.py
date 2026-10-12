import pygame # drawing the game stuff 
import pymunk # phsyics engine for game 

pygame.init()

screen = pygame.display.set_mode((1344, 756)) # 1344x756 window
pygame.display.set_caption("Stickman") #the title thingy
clock = pygame.time.Clock()

space = pymunk.Space() # spaces holds physics objects and their interactions
space.gravity = (0, 900) # (x,y) , 0 horizontal pull from gravity, 900 vertical pull from gravity

player_x = screen.get_width() // 2 # places character in middle of window
player_y = screen.get_height() - 100 # places player on the ground
player_colour = (230, 230, 230) # greyish colour for player - contrasts with dark background

running = True
while running == True:
    for event in pygame.event.get(): # checks for actions like close button being clicked
        if event.type == pygame.QUIT:
            running = False

    space.step(1/60) # updates physics engine every second - matches fps of game
    
    screen.fill((30, 30, 40)) #makes window's background kinda dark
    pygame.draw.rect( # draws the ground at the bottom of window
        screen,
        (110, 75, 45),
        (0, screen.get_height() - 100, screen.get_width(), 100)
    ) 
    pygame.draw.circle( # draws the head of character
        screen, player_colour,
        (player_x, player_y - 110), 15, 4
    )
    pygame.draw.line( # draws the body of character
        screen, player_colour,
        (player_x, player_y - 95),
        (player_x, player_y - 45), 4
    )
    pygame.draw.line( # draws the left arm of character
        screen, player_colour,
        (player_x, player_y - 80),
        (player_x - 30, player_y - 55), 5
    )
    pygame.draw.line( # draws the right arm of character
        screen, player_colour,
        (player_x, player_y - 80),
        (player_x + 30, player_y - 55), 5
    )
    pygame.draw.line( # draws the left leg of character
        screen, player_colour,
        (player_x, player_y - 45),
        (player_x - 20, player_y), 5
    )
    pygame.draw.line( # draws the right leg of character
        screen, player_colour,
        (player_x, player_y - 45),
        (player_x + 20, player_y), 5
    )
    pygame.display.flip() # updates the window w everything thats been drawn until the next flip()
    clock.tick(60) # limits game to 60 fps

pygame.quit() #closes window and ends program
