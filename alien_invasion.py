import sys
from random import randint

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        """注释部分为游戏全屏设置"""
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        """非全屏情况"""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 创建飞船实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_stars()
        self._create_fleet()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        # 将飞船绘制到屏幕上
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_up_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一个子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可以容纳多少个外星人
        # 外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少个外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 创建第一行外星人
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # 创建一个外星人并将其加入当行
                self._create_alien(alien_number, row_number)

    def _create_stars(self):
        """创建星星"""
        for row_number in range(self.settings.star_number):
            self._create_star()

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人,并将其放在当行"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_star(self,):
        star = Star(self)
        star.x = randint(0, self.settings.screen_width)
        star.rect.x = star.x
        star.rect.y = randint(0, self.settings.screen_height - 1.5 * self.ship.rect.height)
        self.aliens.add(star)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
