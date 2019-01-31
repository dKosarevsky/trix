from datetime import datetime


# Тестируем скорость Итератора и декоратора

def iterate_speed_tests():
    start = datetime.now()
    l = []
    for i in range(10**4):
        if i % 2 == 0:
            l.append(i)
    print(datetime.now() - start)
    return l


def generate_speed_test():
    start = datetime.now()
    l = [x for x in range(10**4) if x % 2 == 0]
    print(datetime.now() - start)
    return l


l1 = iterate_speed_tests()
l2 = generate_speed_test()

# print(l1)
# print(l2)
