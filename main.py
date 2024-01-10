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

def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def print_square_num(num):
    print("Square of the num is", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Enter any number: '))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)
