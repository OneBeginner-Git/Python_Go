from typing import List

import matplotlib.pyplot as plt

input_values: list[int] = [1, 2, 3, 4, 5]
squares: list[int] = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=3)
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度样式，实参将影响x轴和y轴上的刻度（ axes='both'），并将刻度标记的字号
# 设置为14（labelsize=14）
plt.tick_params(axis='both', labelsize=14)
plt.show()
