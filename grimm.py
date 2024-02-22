# Example file showing a circle moving on screen
import pygame
from physics_object import PhysicsObject

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# player movement vectors
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_vel = pygame.Vector2(0, 0)
player_dir = pygame.Vector2(0, 0)
player_accel = pygame.Vector2(0, 0)
player_force = pygame.Vector2(0, 0)

# player movement scalars
player_max_speed = 10
player_max_force = 1000
player_frict_coeff = 0.9
player_mass = 5
player_stopping_speed = 0.1
player_radius = 50

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cornflowerblue")

    # render the player
    pygame.draw.circle(screen, "red", player_pos, player_radius)

    # reset the FORCE for each run of the loop
    player_force = pygame.Vector2(0,0)

    # points the FORCE in a direction based on the buttons pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_force.y += -1
    if keys[pygame.K_s]:
        player_force.y += 1
    if keys[pygame.K_a]:
        player_force.x += -1
    if keys[pygame.K_d]:
        player_force.x += 1

    # normalize the FORCE if it is not zero and prepare it for computation
    if player_force.magnitude() != 0:
        player_force = player_force.normalize()
    
    # if the player is not pressing anything, then slow the player if they are moving
    #elif (player_force.magnitude() == 0) and (player_vel.magnitude() > player_stopping_speed):
    #    player_force += -player_force * (player_mass * -9.8) * player_frict_coeff
    
    # if the player is not pressing anything and is moving slower than the STOPPING SPEED then stop
    #elif (player_vel.magnitude() < 0):
    #    player_vel = pygame.Vector2(0, 0)
        
    # calculate the player ACCELERATION by dividing FORCE by MASS and multiplying by the DELTA TIME
    player_accel = ((player_force * player_max_force) / player_mass) * dt
    
    # add the ACCELERATION to the VELOCITY
    player_vel = player_vel + player_accel
    
    # clamp the magnitude of the velocity
    if player_vel.magnitude() >= player_max_speed:
        player_vel = player_vel.normalize() * player_max_speed
    
    # add the velocity to position
    player_pos = player_pos + player_vel
    
    # reverse direction if the player hits a wall
    if player_pos.x > screen.get_width() + player_radius:
        player_pos.x = -player_radius
    if player_pos.x < -player_radius:
        player_pos.x = screen.get_width() + player_radius
    if player_pos.y > screen.get_height() + player_radius:
        player_pos.y = -player_radius
    if player_pos.y < -player_radius:
        player_pos.y = screen.get_height() + player_radius
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()