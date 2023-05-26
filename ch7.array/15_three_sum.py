

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

                    # 정답과 동일한 숫자일 경우 스킵 처리
                    # (ex. [2, -1, -1, ... -1])일 때, [2, -1, -1]은 result 배열에 포함됨. 이 때, nums[2]는 동일하게 -1 이므로 스킵처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
