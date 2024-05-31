def removeDuplicates(nums):
    if not nums:  # 处理空数组的情况
        return 0

    k = 1  # 唯一元素的数量，初始值为 1，因为第一个元素肯定是唯一的
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # 如果当前元素不等于前一个元素，说明找到了一个新的唯一元素
            nums[k] = nums[i]  # 将当前唯一元素放入索引为 k 的位置
            k += 1  # 更新唯一元素数量
    print(nums[:k])
    return k  # 返回唯一元素的数量


# 示例用法
nums = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5]
unique_count = removeDuplicates(nums)
print("唯一元素的数量:", unique_count)
print("去重后的数组:", nums[:unique_count])  # 输出去重后的数组，包含前 unique_count 个元素
print("原始数组:", nums)  # 输出原始数组，可以看到多余的重复元素被覆盖掉了
