import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(60000)
print("random point is {:d}".format(rw.numpoints))
rw.fill_walk()
point_numbers = list(range(rw.numpoints))
plt.figure(dpi=128, figsize=(20, 12))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=10)

# 突出起点和终点
plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
s=100)

# 隐藏坐标轴
plt.axis('off')

plt.show()
