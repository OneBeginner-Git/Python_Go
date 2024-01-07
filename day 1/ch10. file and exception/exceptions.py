# 提示用户提供数值输入时，常出现的一个问题是，用户提供的是
# 文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异
# 常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
# 任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。对你编写
# 的程序进行测试：先输入两个数字，再输入一些文本而不是数字。

total_sum: int = 0

while True:
    num: str = input("请输入加数(q退出)")

    if (num.lower() == 'q') or (num.upper() == 'Q'):
        break

    try:
        add_num = int(num)
    except ValueError as ve:
        print("{} 不是数字，重试\n".format(num))
    else:
        total_sum += add_num
        print("新加数是{:d}, 新的和是{:d}\n".format(add_num, total_sum))

print("End！")
