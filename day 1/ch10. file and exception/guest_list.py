# 编写一个 while 循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个
# 文件中的每条记录都独占一行。输入quit退出

file_name = "guest_book.txt"

# with open(file_name, 'w') as record:
#     record.write("Guest List:\n")

while True:
    name = input("请登记来宾姓名（输入quit以退出）")

    if (name.lower() == "quit") or (name.upper() == "QUIT"):
        break

    print('欢迎您的到来，{:s}\n'.format(name.title().strip()))
    with open(file_name, 'a') as record:
        record.write(name.title().strip() + '\n')

print("登记结束，感谢！")
