nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

def choose_func(nums, square_nums, remove_negatives):
    for num in nums:
        if num > 0: 
            return square_nums
        else:
            return remove_negatives
    
    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

if __name__ == '__main__':
    print(choose_func(nums1, square_nums, remove_negatives))