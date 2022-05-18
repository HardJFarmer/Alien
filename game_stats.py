class GameStatus:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏启动处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间肯变化的统计信息"""
        self.ships_left = self.settings.ship_limit
