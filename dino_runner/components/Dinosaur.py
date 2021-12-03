import pygame
from pygame.sprite import Sprite
from utils.constants import RUNNING, DUCKING, JUMPING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, RUNNING_SHIELD, JUMPING_SHIELD

class Dinosaur(Sprite):
    x_POS = 80
    y_POS = 310
    y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.type = DEFAULT_TYPE

        self.Image = self.run_img[self.type][0]
        self.dino_rect = self.Image.get_rect()
        self.dino_rect.x = self.x_POS
        self.dino_rect.y = self.y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.setup_state_boolans()

    def setup_state_boolans(self):
        self.has_powerup = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0


    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.Image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.Image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.Image.get_rect()
        self.dino_rect.x = self.x_POS
        self.dino_rect.y = self.y_POS
        self.step_index += 1

    def duck(self):
        self.Image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.Image.get_rect()
        self.dino_rect.x = self.x_POS
        self.dino_rect.y = self.y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.Image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def check_invicibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 100, 2)
            if time_to_show >=0:
                if self.show_text:
                    fond = pygame.font.Font('freesansbold.ttf',18)
                    text = fond.render(f'shield enable for {time_to_show}', True, (0, 0, 0))
                    text_rect = text.get_rect()
                    text_rect.center = (500, 40)
                    screen.blit(text, text_rect)
            else:
                self.shield = False
                self.update_to_default(SHIELD_TYPE)


    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE
