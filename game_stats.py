class GameStatus:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_status()
        # 游戏启动是处于活动状态
        self.game_active = True

    def reset_status(self):
        """初始化在游戏运行期间肯变化的统计信息"""
        self.ships_left = self.settings.ship_limit
