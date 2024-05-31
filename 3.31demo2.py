# 三数之和
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  # 数组长度
        res = []  # 存放结果的列表
        nums.sort()  # 将数组排序，方便后续操作
        for i in range(n):  # 遍历数组元素
            if nums[i] > 0:  # 如果当前元素大于 0，由于数组已排序，后面的元素肯定也大于 0，不可能存在三数之和等于 0
                return res
            if i > 0 and nums[i] == nums[i - 1]:  # 如果当前元素和上一个元素相同，跳过，避免重复解
                continue
            L = i + 1  # 左指针，指向当前元素的下一个位置
            R = n - 1  # 右指针，指向数组末尾
            while L < R:  # 当左指针小于右指针时，进行循环
                if nums[i] + nums[L] + nums[R] == 0:  # 找到满足条件的三元组
                    res.append([nums[i], nums[L], nums[R]])  # 将找到的三元组添加到结果列表中
                    # 跳过重复解
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1  # 左指针右移
                    R -= 1  # 右指针左移
                elif nums[i] + nums[L] + nums[R] > 0:  # 如果三数之和大于 0，将右指针左移
                    R -= 1
                else:  # 如果三数之和小于 0，将左指针右移
                    L += 1
        return res  # 返回结果列表
