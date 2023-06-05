def moveZeroes(nums):
    zero_count = 0
    i = 0

    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            zero_count += 1
        else:
            i += 1

    nums.extend([0] * zero_count)
    return nums

#1
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))

#2
nums = [0]
print(moveZeroes(nums))