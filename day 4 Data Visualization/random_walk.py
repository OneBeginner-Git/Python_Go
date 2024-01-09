from random import choice

class RandomWalk():

    # 初始化属性num_points随机点数，默认5000个点
    def __init__(self, num_points=5000):
        self.numpoints = num_points
        # 随机漫步起始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 获得随机漫步所有的点

        while len(self.x_values) < self.numpoints:
            x_dir = choice([1, -1])
            x_dstnc = choice([0, 1, 2, 3, 4, 5])
            x_step = x_dir * x_dstnc

            y_dir = choice([1, -1])
            y_dstnc = choice([1, 2, 3, 4, 5])
            y_step = y_dir * y_dstnc

            # x,y都不移动，就重新循环一次。不能原地踏步
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
