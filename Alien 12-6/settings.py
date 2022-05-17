class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (174, 0, 255)
        self.bullets_allowed = 3
