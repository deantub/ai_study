import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen

        # Завантажити зображення прибульця і обрати rect атрибут.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Зобразити кожного нового прибульця зверху зліва екрану.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.heigth

        # Розмістити прибульців в горизонтальному положенні.
        self.x = float(self.rect.x)