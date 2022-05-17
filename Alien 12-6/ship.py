import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship_left.png")
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midleft = self.screen_rect.midleft

        # 在飞船的属性y中存储小数值
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.ship_speed

        # 根据self.x更新rect对象
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
