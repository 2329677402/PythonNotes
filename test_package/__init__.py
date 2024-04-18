"""
# __init__.py

1、在__init__.py中增加__all__ = [允许导入的模块列表].
2、仅针对 from 包 import * 方式生效，对import xx 方式不生效.
3、对 from test_package import moudle01, moudle02 的导入方式也不生效.
"""
#  控制包允许导入的模块为moudle02
__all__ = ['moudle02']
