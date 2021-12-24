def max_sum(nums) :
    m = nums[0]
    n = nums[0]
    list_num = []
    for i in range(1, len(nums)):
        if n > 0:
            n += nums[i]
        else:
            n = nums[i]

        if m < n:
            list_num.append(m)
            m = n
    return list_num,m
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1,-1,3,5]
nums3 = [-3,-2,-4,5,-2,3,1,-6,5]
print(max_sum(nums1))
print(max_sum(nums2))
print(max_sum(nums3))