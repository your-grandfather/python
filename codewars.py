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
# def invert(lst):
#     new_lst = []
#     for a in lst:
#         a *= -1
#         new_lst.append(a)
#     return new_lst
#
#
# print(invert([5, -3, 1]))
#
# 6
#
# def lovefunk(flower1, flower2):
#     return not (flower1 + flower2) % 2 == 0
#
# 7
#
# def paperwork(n, m):
#     if n < 0 or m < 0:
#         return 0
#     return n * m
#
# 8
# def find_needle(haystack):
#     return f"found the needle at position {haystack.index('needle')}"
#
# 9
# def remove_char(s):
#     return s[1:-1]
#
# 10
#
# def calculate_time(battery, charger):
#     return round(((0.85 * battery / charger) + (0.1 * battery / (charger / 2)) + (0.05 * battery / (charger / 5))), 2)
#
# 12
# def descending_order(num):
#     print(int(''.join(sorted(str(num), reverse=True))))
#
# descending_order(15)
#
# 13
# def high_and_low(numbers):
#     a = [int(num) for num in numbers.split()]
#     return f"{max(a)} {min(a)}"
#
#
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
#
# 14
# def find_average(numbers):
#     if len(numbers) != 0:
#         return sum(numbers) / len(numbers)
#     else:
#         return 0
#
# 15
#
# def solution(text, ending):
#     if text.rfind(ending) == abs((len(text)) - (len(ending))):
#         return True
#     else:
#         return False
#
#
# print(solution('sensei', 'i'))
# print('sensei'.rfind('i'))
#
# 16
#
# def are_you_playing_banjo(name):
#     if (name.lower()[0]) == 'r':
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"
#
# 17
#
# def square_digits(num):
#     num_str = str(num)
#     result = ''.join(str(int(digit) ** 2) for digit in num_str)
#     return int(result)
#
#
# print(square_digits(9119))
#
# 18
# def is_square(n):
#     return isinstance(n ** 0.5, float) and (n ** 0.5).is_integer()
#
#
# print(is_square(-1))
#
# 19
# def catch_sign_change(lst):
#     res = 0
#     for i in range(1, len(lst)):
#         if (lst[i] < 0 <= lst[i - 1]) or (lst[i] >= 0 > lst[i - 1]):
#             res += 1
#     return res
#
#
# bbb = [1, -5, -4, 4, -5]
# print(catch_sign_change(bbb))
#
# 20
def series_sum(n):