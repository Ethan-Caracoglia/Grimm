import pygame

class PhysicsObject:
    
    # A physics object class that contains all of the necessary data to simulate movement by forces
    def __init__(self, pos: pygame.Vector2 = pygame.Vector2(0, 0), mass: float = 10,
                 max_speed: float = 10, max_force: float = 10, frict_coeff: float = 0.5, 
                 is_frict: bool = True):
        self.pos = pygame.Vector2(pos.x, pos.y)
        self.vel = pygame.Vector2(0, 0)
        self.accel = pygame.Vector2(0, 0)
        self.dir = pygame.Vector2(0, 0)
        self.force = pygame.Vector2(0, 0)
        self.mass = mass
        self.max_speed = max_speed
        self.max_force = max_force
        self.frict_coeff = frict_coeff
        self.is_frict = is_frict
    
    # applies force in a certain direction
    def apply_force(self, force: pygame.Vector2):
        self.accel += force / self.mass
        
        
    # function to apply friction
    def apply_friction(self):
        self.frict_force = -self.dir * self.frict_coeff * # TODO Need to figure out how to implement friction in order to slowdown the player to a stop without reversing movement
        self.apply_force(self.frict_force)
        
   # update should be called once every frame in the game loop
    def update(self, dt: float):
        # gets the input from the user and applies it to a 2D vector
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_w]:
            self.force.y += -1
        if self.keys[pygame.K_s]:
            self.force.y += 1
        if self.keys[pygame.K_a]:
            self.force.x += -1
        if self.keys[pygame.K_d]:
            self.force.x += 1
            
        self.apply_force(self.force.normalize() * self.max_force)

        if self.is_frict:
            self.apply_friction()
        
        self.vel = self.accel * dt
        self.dir = self.vel.normalize()