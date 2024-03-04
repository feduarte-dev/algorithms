def bubble_sort(string):
    n = len(string)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if string[j].lower() > string[j + 1].lower():
                string[j], string[j + 1] = string[j + 1], string[j]


def is_anagram(first_string, second_string):
    first_sorted = list(first_string)
    second_sorted = list(second_string)

    bubble_sort(first_sorted)
    bubble_sort(second_sorted)

    fixed_first = "".join(first_sorted).lower()
    fixed_second = "".join(second_sorted).lower()

    if fixed_first != fixed_second or first_string == "":
        return (
            fixed_first,
            fixed_second,
            False,
        )
    return (
        fixed_first,
        fixed_second,
        True,
    )
