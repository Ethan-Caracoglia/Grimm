# Example file showing a basic pygame "game loop"
import pygame

# Constant values for trackin the screen dimensions.
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
clock = pygame.time.Clock()
running = True

# Variable for detla-time.
dt = 1
player_pos = 0
player_size = 0
    
def game_setup():
    player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    player_size = 10
        

    # Function to run inside of the game loop
def game_loop(Number: dt):
    # Print the framerate
    if dt != 0:
        print(1 / dt)

    if player_pos.y < (SCREEN_HEIGHT - player_size / 2):
        player_pos = -player_size 

    # Drawing
    pygame.draw.circle(screen, "green", player_size)
    
# set up the game
game_setup()

while running:
    dt = clock.get_time() / 1000 # Gets the time since the last frame in seconds.
   
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cornflowerblue")

    # RENDER YOUR GAME HERE
    game_loop(dt)
    
    pygame.draw.circle(screen, "green", player_pos, 5)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()