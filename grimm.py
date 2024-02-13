# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# player movement vectors
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_vel = pygame.Vector2(0, 0)
player_accel = pygame.Vector2(0, 0)

# player movement scalars
player_max_speed = 100
player_max_accel = 50
player_frict_coeff = 0.3
player_mass = 10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # render the player
    pygame.draw.circle(screen, "red", player_pos, 40)

    # reset the acceleration for each run of the loop
    player_accel = pygame.Vector2(0,0)

    # accelerates the player in a direction based on what keys are preses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_accel.y -= 1
    if keys[pygame.K_s]:
        player_accel.y += 1
    if keys[pygame.K_a]:
        player_accel.x -= 1
    if keys[pygame.K_d]:
        player_accel.x += 1

    # normalize the acceleration if it is not zero
    if (player_accel.magnitude() != 0):
        player_accel.normalize()
        
    # if the player acceleration is zero and the player is moving then slow down
    elif (player_vel.magnitude() != 0):
        # makes the player's acceleration equal to the direction multiplied by the max acceleration
        # multiplied by the friction coefficient
        player_accel = -player_vel.normalize() * player_max_accel * player_frict_coeff
        
    # reverse direction if the player hits a wall
    # if (player_pos.x > screen.get_width() - 50):
    #    player_accel.x = -player_max_accel
    # if (player_pos.x < 50):
    #    player_accel.x = player_max_accel
    # if (player_pos.y > screen.get_height() - 50):
    #     player_accel.y = -player_max_accel
    # if (player_pos.y < 50):
    #     player_accel.y = player_max_accel
    
    # if the player is adding acceleration then the velocity will increase and if they are not then
    # it will decrease
    player_vel += player_accel * player_max_accel / player_mass
        # when the player has slowed down enough, stop them
    
    # Lock player at or below max speed
    if (player_vel.magnitude() > player_max_speed):
        player_vel = player_vel.normalize() * player_max_speed
    
    # move the player by the velocity
    player_pos += player_vel * dt
    
    if (dt * 1000 % 10 > 0):
        print("player_pos:", player_pos)
        print("player_vel:", player_vel)
        print("player_vel.magnitude():", player_vel.magnitude())
        print("player_accel:", player_accel)
        print("player_accel.magnitude():", player_accel.magnitude())

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()