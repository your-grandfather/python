def merge_lists_to_dict(l1, l2):
    return dict(zip(l1, l2))


list_1 = ['a', 'b', 'c', 'd']
list_2 = [True, False, False, False]

print(merge_lists_to_dict(list_1, list_2))
