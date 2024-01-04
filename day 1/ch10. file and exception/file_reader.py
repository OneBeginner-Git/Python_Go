# 关键字with在不再需要访问文件后将其关闭，避免使用open()后，忘记调用close()
with open('pi_digits.txt') as file_object:
    text = file_object

