def find_duplicate(nums):
    nums.sort()

    if len(nums) == 0:
        return False

    counter = 1
    number = False

    for i in range(1, len(nums)):
        curr_num = nums[i]

        if type(curr_num) != int or curr_num < 1:
            return False

        if curr_num == nums[i - 1]:
            number = curr_num
            counter += 1

    return number
