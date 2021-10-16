class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        cmn = []
        total = set(nums1 + nums2 + nums3)

        for n in total:
            if (n in nums1 and n in nums2) or (n in nums1 and n in nums3) or (n in nums2 and n in nums3):
                cmn.append(n)
        return (cmn)


nums1 = [1, 1, 2, 3]
nums2 = [2, 3]
nums3 = [3]
obj = Solution()  # instantiate
flist = obj.twoOutOfThree(nums1, nums2, nums3)
print(flist)