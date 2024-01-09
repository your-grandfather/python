# def merge_lists_to_dict(list1, list2):
#     return dict(zip(list1, list2))
#
#
# letters = ['a', 'b', 'c', 'd']
# is_glas = [True, False, False, False]
#
# print(merge_lists_to_dict(list1=letters, list2=is_glas))
#
# print(merge_lists_to_dict(letters, list2=is_glas))

def update_car_info(**car):
    car['is_available'] = True
    return car


print(update_car_info(brand='audi', price=100_000))
