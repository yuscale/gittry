# -*- coding: utf-8 -*-
# filename foo.py

from sys import argv


def foo(x):
    sum = 0
    for i in range(x):
        sum += i
    return sum

'''
#  单参数 ok
if __name__ == "__main__":
    t = int(argv[1])
    with open('out.txt', 'a') as out:
        out.write(str(foo(t)))
'''


# 双参数 ok
def foo2(x, y):
    sum = 0
    for i in range(x + y):
        sum += i
    return sum



if __name__ == "__main__":
    t1 = int(argv[1])
    t2 = int(argv[2])
    with open('out.txt', 'a') as out:
        out.write(str(foo2(t1, t2)))
        out.write('\n')

'''
使用方法        ## 注意必须要带上 .py 后缀名
在 才cmd 环境中使用

# 单参数
python foo.py 100

#双参数
python foo.py 10 10


'''