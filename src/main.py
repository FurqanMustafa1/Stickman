import pygame # drawing the game stuff 
import pymunk # phsyics engine for game 

pygame.init() # initialises pygame

screen = pygame.display.set_mode((1344, 756)) # 1344x756 window
pygame.display.set_caption("Stickman") #the title thingy
clock = pygame.time.Clock()

space = pymunk.Space() # spaces holds physics objects and their interactions
space.gravity = (0, 900) # (x,y) , 0 horizontal pull from gravity, 900 vertical pull from gravity

ground_y = screen.get_height() - 100 # y coordinate of ground

floor = pymunk.Segment( # adds a floor in the physics engine
    space.static_body,
    (0, ground_y),
    (screen.get_width(), ground_y),
    0
)
floor.friction = 0.7 # adds friction to the floor so no sliding around
space.add(floor) # adds floor to physics engine

player_width = 60 # players width and height and colour for drawing the player
player_height = 125
player_colour = (230, 230, 230)

player_body = pymunk.Body(1, float("inf")) # creates body for player with mass of 1 and infinite moment so the player stays upright and doesnt rotate
player_body.position = (screen.get_width() // 2, 200) # gets the bodies position and places it 200 pixels from top and in the centre of window

player_shape = pymunk.Poly.create_box( # creates a box shape to detect collisions, invisible
    player_body,
    (player_width, player_height)
)
player_shape.friction = 0.7 # adds friction to player so it doesnt slide around on the ground

space.add(player_body, player_shape) # adds players body and shape to physics engine

move_speed = 300 # movement speed in pixels per sec

running = True
while running == True:
    for event in pygame.event.get(): # checks for actions like close button being clicked
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # checks to see if any keys get pressed

    movement_x = 0 # each frame starts with 0 movement in the x direction

    if keys[pygame.K_a] or keys[pygame.K_LEFT]: # if either a or the left arrow is clicked, the player moves left.
        movement_x -= move_speed # moves player left by taking away movespeed from movement_x

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # if either d or the right arrow is clicked, the player moves right.
        movement_x += move_speed # moves player right by adding movespeed to movement_x

    player_body.velocity = (
        movement_x,
        player_body.velocity.y
    )

    space.step(1/60) # updates physics engine every 1/60 of a second - matches fps of game

    player_x = round(player_body.position.x) # players x position from centre of player
    player_y = round( # players y position from centre of player
        player_body.position.y + player_height / 2
        )
    
    screen.fill((30, 30, 40)) #makes window's background kinda dark
    pygame.draw.rect( # draws the ground at the bottom of window
        screen,
        (110, 75, 45),
        (0, screen.get_height() - 100, screen.get_width(), 100)
    ) 
    pygame.draw.circle( # draws the head of character
        screen, player_colour,
        (player_x, player_y - 110), 15, 0
    )
    pygame.draw.line( # draws the body of character
        screen, player_colour,
        (player_x, player_y - 95),
        (player_x, player_y - 45), 6
    )
    pygame.draw.line( # draws the left arm of character
        screen, player_colour,
        (player_x, player_y - 80),
        (player_x - 30, player_y - 55), 8
    )
    pygame.draw.line( # draws the right arm of character
        screen, player_colour,
        (player_x, player_y - 80),
        (player_x + 30, player_y - 55), 8
    )
    pygame.draw.line( # draws the left leg of character
        screen, player_colour,
        (player_x, player_y - 45),
        (player_x - 20, player_y), 8
    )
    pygame.draw.line( # draws the right leg of character
        screen, player_colour,
        (player_x, player_y - 45),
        (player_x + 20, player_y), 8
    )
    pygame.display.flip() # updates the window w everything thats been drawn until the next flip()
    clock.tick(60) # limits game to 60 fps

pygame.quit() #closes window and ends program
