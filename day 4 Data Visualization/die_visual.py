from die import Die
import pygal

die = Die(6)

results = []
for i in range(0, 100):
    result = die.roll()
    results.append(result)

print(results)
print(str(len(results)) + ' results')
frequencies = []
for value in range(1, die.sides_num + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')