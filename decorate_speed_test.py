#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

# Тестируем скорость Итератора и Генератора с применением декоратора =)

@timeit
def iterate_speed_tests(n):
    # start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    # print(datetime.now() - start)
    return l


@timeit
def generate_speed_test(n):
    # start = datetime.now()
    l = [x for x in range(n) if x % 2 == 0]
    # print(datetime.now() - start)
    return l


l1 = iterate_speed_tests(10**4)
l2 = generate_speed_test(10**4)

# print(l1)
# print(l2)

# print(l)

# l1 = iterate_speed_tests
# a = l1(10)
# print(a)

# l1 = timeit(iterate_speed_tests)
# # print(type(l1), l1.__name__)
# a = l1(10)



# Декоратор, который принимает аргументы:

def timeit_a(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer



@timeit_a('name')
def iterate_speed_tests_a(n):
    # start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    # print(datetime.now() - start)
    return l


@timeit_a('name')
def generate_speed_test_a(n):
    # start = datetime.now()
    l = [x for x in range(n) if x % 2 == 0]
    # print(datetime.now() - start)
    return l

iterate_speed_tests_a(10**4)
generate_speed_test_a(10**4)
