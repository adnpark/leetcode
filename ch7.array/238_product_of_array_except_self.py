class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        # 왼쪽 곱셈 결과
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 오른쪽 곱셉 결과
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
