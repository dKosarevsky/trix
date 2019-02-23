# Способы проверки, если все элементы в списке равны:

lst = ['a', 'a', 'a']

test_one = len(set(lst)) == 1
print(test_one) # True

test_two = all(x == lst[0] for x in lst)
print(test_two) # True

test_thre = lst.count(lst[0]) == len(lst)
print(test_thre) # True

# Решение len (set ()) идиоматично, но построение set менее эффективно с точки зрения памяти и скорости.
