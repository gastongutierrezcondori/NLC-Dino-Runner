import pygame.font
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
black_color = (0, 0, 0)


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render('Point: {}'.format(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (100, 40)
    return text, text_rect

def get_centered_message(message, width=SCREEN_WIDTH //2, height=SCREEN_HEIGHT //3):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect


