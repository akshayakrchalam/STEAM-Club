class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for n in range(0, len(nums)):
            for m in range(n+1, len(nums)):
                if nums[n] + nums[m] == target:
                    result.append(n)
                    result.append(m)
                    return result


nums = [2, 7, 11, 15]
target = 9
obj = Solution()
p_lst = obj.twoSum(nums, target)
print(p_lst)