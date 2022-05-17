import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """表示单个星星的类"""

    def __init__(self, ai_game):
        """初始化星星并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # 每个星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星的精确水平位置
        self.x = float(self.rect.x)