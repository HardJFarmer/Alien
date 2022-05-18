class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 68, 153)
        # 飞船设置
        self.ship_limit = 2
        self.ship_speed = 2.5
        # 子弹设置
        self.bullet_speed = 2.5
        self.bullet_width = 800
        self.bullet_height = 15
        self.bullet_color = (255, 0, 17)
        self.bullets_allowed = 10
        # 星星设置
        self.star_number = 150
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1
        # 加快游戏节奏速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction 为1 表示向右， -1 向左
        self.fleet_direction = 1

        # 记分
        self.alien_point = 50

    def increase_speed(self):
        """提高速度设置和外星人的分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)
        print(self.alien_point)
