以十进制的“19”转换为二进制数为例，用19除以模（在这里模就是2）然后取它的余数。

19除以2商9余1

9除以2商4余1

4除以2商2余0

2除以2商1余0

1除以2商0余1

当商为0时结束运算
从上到下依次是个位、十位
所以19的二进制为10011

'''

# 获取用户输入十进制数
while True:
    dec=int(input("输入数字："))

    print("十进制数为：", dec)
    print("转换为二进制为：", bin(dec))
    print("转换为八进制为：", oct(dec))
    print("转换为十六进制为：", hex(dec))
# 执行以上代码输出结果为：

# python3
# test.py
# 输入数字：5
# 十进制数为：5
# 转换为二进制为： 0b101
# 转换为八进制为： 0o5
# 转换为十六进制为： 0x5
# python3
# test.py
# 输入数字：12
# 十进制数为：12
# 转换为二进制为： 0b1100
# 转换为八进制为： 0o14
# 转换为十六进制为： 0xc

