from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()  # 先将数组排序，方便后续操作
    closest_sum = float('inf')  # 初始化最接近目标值的和为正无穷大
    min_diff = float('inf')  # 初始化最小差值为正无穷大

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]  # 当前三数之和

            # 计算当前三数之和与目标值的差值
            diff = abs(current_sum - target)
            if diff < min_diff:
                min_diff = diff
                closest_sum = current_sum

            # 根据当前三数之和与目标值的大小关系调整左右指针
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum  # 如果找到和等于目标值，则直接返回

    return closest_sum  # 返回最接近目标值的和


class Solution:
    # 示例
    nums = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest(nums, target))
