'''
1. 먼저 인풋으로 주어진 nums를 오름차순으로 정렬한다.
2. min([0],[1]) + ... + min([len() - 2], [len() - 1])의 값을 리턴한다.
'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        length = len(nums)
        if (length == 2):
            return min(nums[0], nums[1])

        nums.sort()  # 먼저 정렬
        result = 0
        for i in range(0, length, 2):
            result += nums[i]  # 여기서 min을 쓸 필요는 없다.
        return result
