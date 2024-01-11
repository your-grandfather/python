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

def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id and image_title must be present")

    return f"Image {img['image_title']} has id {img['image_id']}"


image5136 = {
    'image_i': 5136,
    'image_title': 'my cat',
}
try:
    print(image_info(image5136))
except TypeError as e:
    print(e)
