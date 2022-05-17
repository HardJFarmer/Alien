class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 68, 153)
        self.ship_speed = 2.5
        # 子弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 17)
        self.bullets_allowed = 10
        # 星星设置
        self.star_number = 150
