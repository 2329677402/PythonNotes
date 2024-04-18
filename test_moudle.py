"""
没有__all__时,会导入所有功能.
使用了__all__,在其它文件使用 from test_moudle import * 的导入方式只能导入被允许的功能.
而import test_moudle的导入方式不会受__all__的限制.
"""
__all__ = ['hi', 'hello']


def hi():
    print("hi")


def hello():
    print("hello")
