# %%

# 关键字with在不再需要访问文件后将其关闭，避免使用open()后，忘记调用close()
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents[-1])
    print(contents.rstrip())  # 使用rstrip方法剥除字符串末尾的空白

# %%

with open('D:\\Code\\Github\\Python_Go\\day 1\\ch10. file and exception\\pi_digits.txt') as file_object:
    for line in file_object:
        print(line, end='')

    for line in file_object:
        print(line.rstrip())  # 使用rstrip方法剥除字符串末尾的空白

# %%

# 使用关键字with时， open()返回的文件对象只在with代码块内可用
# 可以使用一个列表把文件先存储起来，然后在with代码块外使用
# 读取文本文件时， Python将其中的所有文本都解读为字符串。如果你读取的是数字，并
# 要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转
# 换为浮点数。
file_path = 'D:\\Code\\Github\\Python_Go\\day 1\\ch10. file and exception\\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()  # 去掉开头结尾的空格

print(pi_string)
print(len(pi_string))
# %%
