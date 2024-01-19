# 1
#
# def square_sum(numbers):
#     result = 0
#     for a in numbers:
#         result += a * a
#     return result
#
#
# my_list = [-1, 0, 1]
#
# square_sum(my_list)
#
# print(square_sum(my_list))

# 2
# def find_smallest_int(arr):
#     return min(arr)
#
#
# my_list = [34, -345, -1, 100]
#
# print(find_smallest_int(my_list))
#
# 3
# def string_to_array(s):
#     if s == '':
#         return ''
#     else:
#         return s.split()
#
#
# aaa = ''
#
# print(string_to_array(aaa))
#
# 4
# def abbrev_name(name):
#     a = name.title().split()
#     return f"{a[0][0]}.{a[1][0]}"
#
#
# print(abbrev_name('tim malikov'))
#
# 5
def invert(lst):
    new_lst = []
    for a in lst:
        a *= -1
        new_lst.append(a)
    return new_lst


print(invert([5, -3, 1]))
