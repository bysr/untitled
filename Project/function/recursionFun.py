# 递归函数，比如阶乘算法
import sys
sys.setrecursionlimit(1500)  # set the maximum depth as 1500


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


print(fact(1000))


def fact(n):
    return fact_item(n, 1)


def fact_item(num, produce):
    if num == 1:
        return produce
    return fact_item(num-1, num*produce)


print(fact(500))


def fact(n):
    return fact_iter(1, 1, n)


def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)


print(fact(1000))
