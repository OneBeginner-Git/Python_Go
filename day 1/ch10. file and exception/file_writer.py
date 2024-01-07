filename = "programming.txt"

# 打开文件时，可指定读取模
# 式（ 'r'）、 写入模式（ 'w'）、 附加模式（ 'a'）或让你能够读取和写入文件的模式（ 'r+'）。如果
# 你省略了模式实参， Python将以默认的只读模式打开文件
with open(filename, 'w') as file_object:
    file_object.write('I love programming.')

# 如果你要写入的文件不存在，函数open()将自动创建它。
with open("programming_noe.txt", 'w') as file_object:
    file_object.write('I love programming.')

with open(filename, 'r') as file_object:
    print(file_object.read())

with open(filename, 'a') as file_object:
    file_object.write('\nI love programming.')
    file_object.write('\nI also love creating apps.')
