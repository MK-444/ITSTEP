def merge_two_list(list_a, list_b):
    list_c = []
    pointer_i = pointer_j = 0
    while pointer_i < len(list_a) and pointer_j < len(list_b):
        if list_a[pointer_i] < list_b[pointer_j]:
            list_c.append(list_a[pointer_i])
            pointer_i += 1
        else:
            list_c.append(list_b[pointer_j])
            pointer_j += 1
    if pointer_i < len(list_a):
        list_c += list_a[pointer_i:]
    if pointer_j < len(list_b):
        list_c += list_b[pointer_j:]
    return list_c


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    middle = len(input_list)// 2
    left = merge_sort(input_list[:middle])
    right = merge_sort(input_list[middle:])
    return merge_two_list(left, right)


print(*merge_sort([6,2,19,5,10,7,11]))