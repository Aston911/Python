def fib(n):
    '''
    fib 是斐波那契数列自定义函数
    n 是大于1的自然数，f(1)=1 f(2)=1,f(3)=2,
    f(n)=f(n-1)+f(n-2)
    '''
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
for i in range(6):
    i += 1
    print(fib(i),end = ',')
print('\n' ,'~ '* 10)
def hano(n, a, b,c):
    '''
    汉诺塔的递归实现
    n：代表几个盘子
    a：代表第一个塔，开始的塔
    b：代表第二个塔，中间过渡的塔
    c：代表第三个塔, 目标塔
    '''
    if n == 1:
        print(a, "-->", c)
        return None

    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None

    # 把n-1个盘子，从a塔借助于c塔，挪到b塔上去
    hano(n - 1, a, c, b)
    print(a, "-->", c)
    # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上去
    hano(n - 1, b, a, c)


a = "A"
b = "B"
c = "C"

n = 3
hano(n,a,b,c)
