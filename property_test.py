class Screen(object):
    @property  ##设置property后可以通过设置self.setter来检查参数
    def width(self):
        return self._width

    @width.setter ##相当于装饰器
    def width(self, value):
        self._width=value

    @property ##@property方法相当于把方法当做属性调用
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height=value

    @property
    def resolution(self):
        return self._height * self._width


# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution