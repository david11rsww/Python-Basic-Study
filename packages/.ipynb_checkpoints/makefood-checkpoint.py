# __all__ 仅对 from makefood import * 导入方式进行约束
# __all__ = ["make_icecream"]
__all__ = ["make_icecream", "make_drink"]

# 制作冰激凌的功能
def make_icecream(*toppings):
    # toppings 配料
    print('这个冰激凌的配料如下: ')
    for topping in toppings:
        print('\t', topping)


def make_drink(size, drink):
    print('您点的饮料如下: ')
    print('-----', size.title())
    print('-----', drink.title())



class Person(object):
    pass


# 如果此模块作为主程序运行, 则执行 main 函数代码, 否则不执行
if __name__ == '__main__':
    # 模块开发者可能会测试自己编写的功能
    make_icecream('草莓酱', '葡萄干', '巧克力碎片')
    make_drink('大杯', '卡布奇诺')
