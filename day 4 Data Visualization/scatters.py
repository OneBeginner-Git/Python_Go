import matplotlib.pyplot as plt
x_limit = 1000
x_values = list(range(1,x_limit))
y_values = [x**2 for x in x_values]
# 要修改数据点的颜色，可向scatter()传递参数c, 一个元组，其中包含三个0~1之间的小数值，
# 它们分别表示红色、绿色和蓝色分量
#plt.scatter(x_values, y_values, c='orange', s=10)
# plt.scatter(x_values, y_values, c=(0.2, 0, 0.8), edgecolors='none', s=10)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
edgecolor='none', s=10)
plt.title("Square Numbers in Points", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.axis((0, x_limit, 0, x_limit**2+x_limit))
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
