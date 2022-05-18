class GameStatus:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        #
        self.reset_stats()
        # 游戏启动处于非活动状态
        self.game_active = False
        # 任何情况下都不应重置最高得分
        self.ships_left = 0
        # 任何情况下都不应该重置最高得分
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间肯变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """读取文件中得最高分"""
        try:
            with open("file/highScore.txt", 'r') as file_object:
                high_score = file_object.read()
            return int(high_score)
        except Exception:
            # 如果读文件发生错误直接返回0分
            return 0

    def write_high_score(self, score):
        with open("file/highScore.txt", 'w') as file_object:
            file_object.write(str(score))
