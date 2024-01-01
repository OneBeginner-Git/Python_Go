class TestObject(object):
    strClassName = 'alias'
    intClassId = 0

    def show_name(self):
        print(self.strClassName)


# 创建类的实例
a = TestObject()

# 调用实例方法
a.show_name()
