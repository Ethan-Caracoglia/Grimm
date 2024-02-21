import pygame

class PhysicsObject:
    
    #p_pos, p_vel, p_accel, p_dir, p_force, p_mass, p_max_speed, p_max_force, p_frict_coeff, p_is_grav, p_is_frict
    
    def __init__(self, pos: pygame.Vector2 = pygame.Vector2(0, 0), mass: float = 10, max_speed: float = 10, max_force: float = 10, frict_coeff: float = 0.5, is_grav: bool = True, is_frict: bool = True):
        self.p_pos = pygame.Vector2(pos.x, pos.y)
        self.p_vel = pygame.Vector2(0, 0)
        self.p_accel = pygame.Vector2(0, 0)
        self.p_dir = pygame.Vector2(0, 0)
        self.p_force = pygame.Vector2(0, 0)
        self.p_mass = mass
        self.p_max_speed = max_speed
        self.p_max_force = max_force
        self.p_frict_coeff = frict_coeff
        self.p_is_grav = is_grav
        self.p_is_frict = is_frict
    
    def apply_force(self, force: pygame.Vector2):
        self.p_accel += self.p_accel + force / self.p_mass