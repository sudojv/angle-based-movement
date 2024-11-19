import pygame

from math import pi as PI

from math import cos
from math import sin

class Hero:
    def __init__(self, game):
        self.screen:pygame.Surface = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.settings = game.settings

        self.rect = pygame.rect.Rect(
            0, 0, self.settings.hero_width, self.settings.hero_height
        )

        self.rect.center = self.screen_rect.center

        self.direction = 0
        self.angle = self.direction * PI

        self.speed = self.settings.hero_speed

        self.left_acceleration = 0.0
        self.right_acceleration = 0.0

        self.angle_acceleration = 0.0

        self.rotating_left = False
        self.rotating_right = False
        self.moving_front = False
        self.moving_back = False

    def update(self):
        self._update_movements()

    def _update_movements(self):
        self._update_direction_angle()

        self.rect.centerx += (
            self.speed * cos(self.angle) * self.angle_acceleration
        )
        self.rect.centery -= (
            self.speed * sin(self.angle) * self.angle_acceleration
        )

        self._update_movement_flags()
    
    def _update_direction_angle(self):
        self.direction += self.speed * self.left_acceleration
        self.direction -= self.speed * self.right_acceleration

        self.angle = (self.direction / 100) * PI
    
    def _update_movement_flags(self):
        self._update_left_acceleration()
        self._update_right_acceleration()
        self._update_angle_acceleration()
    
    def _update_left_acceleration(self):
        if self.rotating_left:
            if self.left_acceleration < self.settings.hero_max_acc:
                self.left_acceleration += self.settings.hero_acceleration
        
        if not self.rotating_left:
            if self.left_acceleration > 0.0:
                self.left_acceleration -= self.settings.hero_attrition
            else:
                self.left_acceleration += self.settings.hero_attrition

    def _update_right_acceleration(self):
        if self.rotating_right:
            if self.right_acceleration < self.settings.hero_max_acc:
                self.right_acceleration += self.settings.hero_acceleration
        
        if not self.rotating_right:
            if self.right_acceleration > 0.0:
                self.right_acceleration -= self.settings.hero_attrition
            else:
                self.right_acceleration += self.settings.hero_attrition

    def _update_angle_acceleration(self):
        if self.moving_front:
            if self.angle_acceleration < self.settings.hero_max_acc:
                self.angle_acceleration += self.settings.hero_acceleration
        elif self.moving_back:
            if self.angle_acceleration > self.settings.hero_min_acc:
                self.angle_acceleration -= self.settings.hero_acceleration
        
        if not self.moving_front and not self.moving_front:
            if self.angle_acceleration > 0.0:
                self.angle_acceleration -= self.settings.hero_attrition
            else:
                self.angle_acceleration += self.settings.hero_attrition

    def blit(self):
        self.rect = pygame.draw.circle(
            self.screen,
            self.settings.hero_color,
            self.rect.center,
            self.settings.hero_height,
            self.settings.hero_width
        )
        
        pygame.draw.rect(self.screen, 'white', self.rect, 1)

        pygame.draw.line(
            self.screen, 'white', self.rect.center,
            (
                self.rect.centerx + cos(self.angle) * 60,
                self.rect.centery - sin(self.angle) * 60
            )
        )