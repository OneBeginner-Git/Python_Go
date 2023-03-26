# %%
a = 10
b = 3
print(a / b)
# %%
# 格式化输出
LocalTime = 1230
count = 1
template = "Time: {}, count: {}"
result = template.format(LocalTime, count)
print(result)
# 指定使用第几个元素
template = "Time: {1}, count: {0}"
result = template.format(LocalTime, count)
print(result)
# %%
L = ['Alice', 66, 'Bob', True, 'False', 100]
n = 0
for n in range(0, len(L), 2):
    print(L[n])

# %%
import re

s = "Gain: 1dB \n \ Input Power:       23 dBm"
pattern = r"Input Power:       (\d+\.\d+) dBm"
match = re.search(pattern, s)
if match:
    value = float(match.group(1))
    print("找到了数字：", value)
    if value > 20:
        print("数字大于20")
    else:
        print("数字小于等于20")
else:
    print("未找到目标字符串")

# %%
import telnetlib

'''可以使用Python内置的telnetlib模块实现telnet连接。
下面是一个简单的示例代码，连接到IP地址为192.168.1.100，
端口号为23的设备：
'''

# IP地址和端口号
host = "192.168.1.100"
port = 23

# 创建telnet对象并连接到设备
tn = telnetlib.Telnet(host, port)

# 进行登录或者其他操作，这里以登录为例
tn.read_until(b"login: ")
tn.write(b"admin\n")
tn.read_until(b"Password: ")
tn.write(b"password\n")

# 执行其他命令
tn.write(b"show version\n")
output = tn.read_until(b"exit")
print(output.decode("utf-8"))

# 关闭连接
tn.close()