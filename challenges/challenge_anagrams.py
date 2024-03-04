def merge_sort(string):
    if len(string) > 1:
        mid = len(string) // 2
        left = string[:mid]
        right = string[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(string, left, right)


def merge(string, left, right):
    left_index = right_index = general_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            string[general_index] = left[left_index]
            left_index += 1
        else:
            string[general_index] = right[right_index]
            right_index += 1
        general_index += 1

    while left_index < len(left):
        string[general_index] = left[left_index]
        left_index += 1
        general_index += 1

    while right_index < len(right):
        string[general_index] = right[right_index]
        right_index += 1
        general_index += 1


def is_anagram(first_string, second_string):
    sorted_first = list(first_string.lower())
    sorted_second = list(second_string.lower())

    merge_sort(sorted_first)
    merge_sort(sorted_second)

    fixed_first = "".join(sorted_first)
    fixed_second = "".join(sorted_second)

    return (
        fixed_first,
        fixed_second,
        fixed_first == fixed_second and fixed_first != "",
    )
