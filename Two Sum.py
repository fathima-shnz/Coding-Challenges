class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
