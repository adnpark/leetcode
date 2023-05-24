

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                # skip if element is same as prior one
                # (ex. [1, 1, ...]) we don't need to check nums[1], because it's same as nums[0]
            left, right = i + 1, len(nums) - 1
            while left < right:  # keep narrowing two pointers
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right += 1
                else:
                    result.append(nums[i], nums[left], nums[right])
