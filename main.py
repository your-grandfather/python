# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy
#
#
# initial_post = {
#     'id': 243,
#     'author': 'Bogdan'
# }
#
# post_with_weekday = create_new_post(initial_post)
#
# print(post_with_weekday)
#
# def print_number_info(num):
#     if (num % 2) == 0:
#         print("Entered number is even")
#     else:
#         print("Entered number is odd")
#
#
# def print_square_num(num):
#     print("Square of the num is", num * num)
#
#
# def process_number(num, callback_fn):
#     callback_fn(num)
#
#
# entered_num = int(input('Enter any number: '))
#
# process_number(entered_num, print_number_info)
# process_number(entered_num, print_square_num)
#
# c = 5
#
#
# def my_fn(a, b):
#     d = 10
#     print(c)
#     print(a, b)
#     print(dir())
#
# 27
#
# my_car = {
#     'brand': 'Toyota',
#     'price': 10000
# }
#
# print('brand' in my_car)
#
# a = {3, True, 'cook'}
# b = {3, True, 'cook'}
#
# print(a == b)
#
# print(a is b)
#
# print(True in a)
#
# 28
#
# dict_a = {
#     'key1': 'value1',
#     'key2': 'value2',
# }
# dict_b = {
#     'key1': 'value1',
#     'key2': 'value2',
# }
#
# (dict_a == dict_b) and print("Dictionaries are equal")
#
# 29
#
# button = {
#     'width': 200,
#     'text': 'Buy',
# }
#
# red_button = {
#     'color': 'red',
# }
#
# button_new = {**button, **red_button, }
#
# print(button_new)
#
# 31
# my_name = 'Tim'
# my_hobby = 'running'
# time = 8
#
# info = f"{my_name} do not likes {my_hobby} at {time} o'clock"
# info = str.title(info)
# print(info)
#
# 32
# def greeting(greet):
#     return lambda name: f"{greet}, {name}!"
#
#
# morning_greeting = greeting("Good Morning")
#
# print(morning_greeting(input("What is your name? ")))
#
# 33
# try:
#     print(10 / 0)
# except Exception as e:
#     print(e)
# else:
#     print("There was no error")
# finally:
#     print('Continue...')
#
# def image_info(img):
#     if ('image_id' not in img) or ('image_title' not in img):
#         raise TypeError("Keys image_id and image_title must be present")
#
#     return f"Image {img['image_title']} has id {img['image_id']}"
#
#
# image5136 = {
#     'image_i': 5136,
#     'image_title': 'my cat',
# }
# try:
#     print(image_info(image5136))
# except TypeError as e:
#     print(e)
#
# 34
#
# user_data = ['Timur', 23]
#
#
# def user_info(name, comments_qty):
#     if not comments_qty:
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments"
#
#
# print(user_info(*user_data))
#
# dicts_list = [{'value1': 'value1-1', 'value2': 'value1-2', }, {'value1': 'value2-1', 'value2': 'value2-2', },
#               {'value1': 'value3-1', 'value2': 'value3-2', }]
# dict1, dict2, dict3 = dicts_list
#
#
# def fn(value1, value2):
#     return f"{value1} and {value2}"
#
#
# print(fn(**dict1))
# print(fn(**dict2))
# print(fn(**dict3))
#
# 35
#
# def route_info(dict1):
#     if dict1.get('distance') and dict1['distance'] is int:
#         return f"Distance to your destination is {dict1['distance']}"
#     if dict1.get('speed') and dict1.get('time'):
#         return f"Distance to your destination is {dict1['speed'] * dict1['time']}"
#     return f"No distance info is available"
#
#
# route = {
#     'speed': 20,
#     'distance': 40.3,
#     'time': 3,
# }
#
# print(route_info(route))
#
# 36
#
# my_img = ('1920', '1080', 4)
#
# if len(my_img) == 2:
#     print(f"{my_img[0]}x{my_img[1]}")
# else:
#     print("Incorrect image formatting")
#
# string1 = "kjsdjkhsdkjfsdjkhfsdjkhsdkhsdhkjfkjh"
# print("String is short") if len(string1) < 80 else print("String is long")
#
# 37
#
# my_dict = {'id': 124, 'title': 'test', }
# for k, v in my_dict.items():
#     print(k, v)
#
# for num in range(0, 10, 3):
#     print(num)
#
#
# def filter_list(list1, value_type):
#     new_list2 = []
#     for item in list1:
#         if type(item) is value_type:
#             new_list2.append(item)
#     print(new_list2)
#
#
# filter_list([1, 2, 'ddd', 3, 4, 5, 'abc'], int)
#
#
# def filter_list2(list2, value_type):
#     def check_element_type(elem):
#         return type(elem) is value_type
#
#     return list(filter(check_element_type, list2))
#
#
# res = filter_list2([1, 10, 'abc', 5.5], int)
# print(res)
#
# 38
#
# import random
#
# random_num = random.randint(1, 5)
# while True:
#     num = int(input("Guess the number fom 1 to 5: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congratulations!", random_num)
#     break
#
# while True:
#     num1 = float(input("Enter first number: "))
#     num2 = 0
#     while num2 == 0:
#         num2 = float(input("Enter second number (not 0!): "))
#     print(f"{num1}/{num2}={num1 / num2}")
#     cont = input("Do you want to continue?(y/n): ")
#     if cont == 'y':
#         continue
#     elif cont == 'n':
#         break
#
# 39
#
# my_scores = [10, 7, 14]
#
# scores = {k: v for k, v in enumerate(my_scores)}
#
# print(scores)
# print(my_scores)
#
# my_dict = {
#     'k1': 'value1',
#     'k2': 'value2',
#     'k3': 'value3',
# }
#
# upper_d = {k: str.upper(v) for k, v in my_dict.items()}
# print(upper_d)
#
# my_list = ['qwer', 'qwe', 'qwerty', 'qw', 'asdf']
# new_list = [v for v in my_list if len(v) > 3]
# print(new_list)
#
# from sys import getsizeof
#
# squares_gen = (num * num for num in range(100000))
#
# print(getsizeof(squares_gen))
#
# for elem in squares_gen:
#     print(elem)
#     if elem == 100:
#         break
#
# squares_list = [num * num for num in range(100000)]
#
# print(getsizeof(squares_list))
#
# 40
#
# class Car:
#     def move(self):
#         print("Car is moving")
#
#     def stop(self):
#         print("Car stopped")
#
#
# my_car = Car()
#
# my_car.move()
# my_car.stop()
#
# my_second_car = Car()
# class Comment:
#     def __init__(self, text):
#         self.text = text
#         self.votes_qty = 0
#
#     def upvote(self):
#         self.votes_qty += 1
#
#
# my_comment = Comment("My comment")
#
# print(my_comment.text)
# print(my_comment.votes_qty)
#
# my_comment.upvote()
#
# class Image:
#     def __init__(self, resolution, title, extension):
#         self.resolution = resolution
#         self.title = title
#         self.extension = extension
#
#     def resize(self, new_resolution):
#         self.resolution = new_resolution
#
#
# img1 = Image('640x480', 'grib', '.grb')
#
# print(img1.resolution)
#
# img1.resize('1280x960')
#
# print(img1.resolution)
#
# class Comment:
#     total_comments = 0
#
#     def __init__(self, text):
#         self.text = text
#         self.votes_qty = 0
#         Comment.total_comments += 1
#
#
# comment_1 = Comment("First comment")
#
# print(Comment.total_comments)
#
# comment_2 = Comment("Second comment")
#
# print(Comment.total_comments)
#
# 41
# class Comment:
#     def __init__(self, text):
#         self.text = text
#         self.votes_qty = 0
#
#     def upvote(self):
#         self.votes_qty += 1
#
#     def __add__(self, other):
#         return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)
#
#     def __eq__(self, other):
#         return self.text == other.text and self.votes_qty == other.votes_qty
#
#
# first_comment = Comment("123")
# first_comment.upvote()
# second_comment = Comment("123")
# second_comment.upvote()
# print(first_comment + second_comment)
# print(first_comment == second_comment)
#
# class ExtendedList(list):
#     def print_list_info(self):
#         print(f"List has {len(self)} element(s)")
#
#
# custom_list = ExtendedList([3, 5, 2])
#
# custom_list.print_list_info()
#
# custom_list.append(7)
#
# custom_list.print_list_info()
#
# 44
#
# import json
#
# my_dict = {
#     "key1": "value1",
#     "key2": 2,
#     "key3": True,
#     "key4": [4, 44, 4],
# }
# j_dict = json.dumps(my_dict)
# print(j_dict)
# print(type(j_dict))
#
# conv_json = json.loads(j_dict)
# print(conv_json)
#
# 45
# from pathlib import Path
#
# Path('.') / 'files'
#
# with open('./files/first.txt', 'w') as file1:
#     file1.write("First string\nSecond string\n")
#
# with open('./files/first.txt') as file1:
#     print(file1.read())
#
# with open('./files/second.txt', 'w') as file2:
#     file2.write("First string\nSecond string\n")
#
# with open('./files/second.txt') as file2:
#     print(file2.readlines())
#
# Path('./files/first.txt').unlink()
# Path('./files/second.txt').unlink()
# Path('./files').rmdir()
#
# 50
import re


def check_password(passw):
    pass_check_pattern1 = re.compile("........+")
    pass_check_pattern2 = re.compile(r"^.*[a-z]+.*$")
    pass_check_pattern3 = re.compile(r"^.*[A-Z]+.*$")
    pass_check_pattern4 = re.compile(r"^.*[0-9]+.*$")
    pass_check_pattern5 = re.compile(r"^.*[!@#$%^&*()]+.*$")

    if pass_check_pattern1.fullmatch(passw) and pass_check_pattern2.fullmatch(passw) and pass_check_pattern3.fullmatch(
            passw) and pass_check_pattern4.fullmatch(passw) and pass_check_pattern5.fullmatch(
        passw):
        return passw, "valid"
    else:
        return passw, "invalid"


print(check_password(input("enter password: ")))
