try:
    """
        1、raise：用于主动的触发异常
        2、ZeroDivisionError：根据需要指定的异常
        3、"主动触发ZeroDivisionError异常"：指定的异常信息
    """
    raise ZeroDivisionError("主动触发ZeroDivisionError异常")
except ZeroDivisionError as e:
    print(f"捕获到异常 信息->{e} 类型->{type(e)}")  # 捕获到异常 信息->主动触发ZeroDivisionError异常 类型-><class 'ZeroDivisionError'>
