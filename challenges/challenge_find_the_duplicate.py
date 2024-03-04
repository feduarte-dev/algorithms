def find_duplicate(nums):
    sorted_nums = sorted(nums)
    for index, number in enumerate(sorted_nums):
        if type(number) is not int or number < 0:
            return False
        elif index < len(sorted_nums) - 1 and number == sorted_nums[index + 1]:
            return number
    return False
