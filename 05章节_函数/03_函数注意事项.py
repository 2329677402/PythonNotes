"""
- 函数注意事项和使用细节
① 函数的参数列表可以是多个,也可以没有
② 函数的命名遵循标识符命名规则和规范
③ 函数中的变量是局部的,函数外不生效
"""

# ④ 如果同一个文件,出现两个函数名相同的函数,则以就近原则进行调用
#   注意：此用法仅在Python语言中允许,在其它开发语言中并不支持重复的函数名
print("-----demo4-----")


def cry():
    print("hi")


def cry():
    print("hello")


cry()  # hello

# ⑤ 调用函数时，根据函数定义的参数位置来传递参数，这种传参方式就是位置参数，传递的实参和定义的的形参顺序和个数必须一致，同时定义的形参，不用指定数据类型，会根据传入的实参决定
print("-----demo5-----")


def car_info(name, price, color):
    print(f"name->{name} price->{price} color->{color}")


car_info("宝马", 5000000, "red")  # name->宝马 price->5000000 color->red
# 传递的实参和定义的的形参顺序和个数必须一致，否则报TypeError错误
# car_info("宝马", 5000000, "red", 11)  # TypeError


# ⑥ 函数可以有多个返回值，返回数据类型不受限制
print("-----demo6-----")


def f1(n1, n2):
    return n1 + n2, n1 - n2


r1, r2 = f1(10, 20)
print(f"r1->{r1},r2->{r2}")  # r1->30,r2->-10

# ⑦ 函数支持关键字参数
# - 函数调用时，可以通过"形参名 = 实参值"形式传递参数
# - 可以不受参数限制传递顺序的限制
print("-----demo7-----")


def book_info(name, price, author, amount):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 传统调用方式,一一对应,顺序不能打乱
book_info("红楼梦", 60, "曹雪芹", 30000)  # name->红楼梦 price->60 author->曹雪芹 amount->30000
# 关键字传参,顺序可以打乱
book_info(name="红楼梦", amount=30000, price=40, author="曹雪芹")  # name->红楼梦 price->60 author->曹雪芹 amount->30000

# ⑧ 函数支持默认参数/缺省参数
# - 定义函数时，可以给参数提供默认值，调用函数时，指定了实参，则以指定为准，没有指定，则以默认值为准
print("-----demo8-----")


def book_info2(name='<<Python>>', price=99.80, author='Simon', amount=1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


book_info2()  # name-><<Python>> price->99.8 author->Simon amount->1000
book_info2("红楼梦", 60, "曹雪芹", 30000)  # name->红楼梦 price->60 author->曹雪芹 amount->30000


# - 默认参数，需要放在参数列表后
def book_info2(name, price, author='Simon', amount=1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


book_info2("python", 99.8)  # name->python price->99.8 author->Simon amount->1000

# ⑨ 函数支持可变参数/不定长参数
# - 应用场景：当调用函数时，不确定传入多少个实参的情况
# - 传入的多个实参，会被组成一个元组(tuple)
# - 比如需要计算多个数的和,但是不确定有几个数
print("-----demo9-----")


def sum(*args):
    print(f"args->{args} 类型->{type(args)}")
    sum = 0
    for i in args:
        sum += i
    return sum


result = sum(1, 2, 3, 5, 10, 99)
print("result =", result)
# args->(1, 2, 3, 5, 10, 99) 类型-><class 'tuple'>
# result = 120

# ⑩ 函数的可变参数/不定长参数还支持多个关键字参数，也就是多个“形参名 = 实参值”
# - 应用场景：当调用函数时，不确定传入多少个关键字参数的情况
# - 传入的多个关键字参数，会被组成一个字典(dict)
# - 比如需要接收一个人的信息，但是有哪些信息是不确定的，就可以使用关键字可变参数
print("-----demo10-----")


def person(**args):
    print(f"args->{args} 类型->{type(args)}")
    for arg_name in args:
        print(f"参数名->{arg_name} 参数值->{args[arg_name]}")


person(name="Simon", age=18, email="3157043973@qq.com")

# ⑪ Python调用另一个.py文件中的函数
print("-----demo11-----")
import Test

Test.add(10, 20)
