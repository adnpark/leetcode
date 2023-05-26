"""
브루트 포스 풀이
1. nums[i] 값과 나머지 값을 더해서 target이 되는 이중 반복문을 작성한다.
2. 일치할 경우 해당 값의 인덱스 배열을 리턴한다.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                if n + m == target:
                    return [i, j]


"""
target - n 값이 존재하는지 확인
1. target - nums[i] 값을 구한다.
2. 해당 값이 nums[i+1:] 배열에 있는지 확인한다.
3. 만약 있다면 해당 값들의 인덱스 배열을 리턴한다.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]:
                print(i)
                return [i, nums[i + 1:].index(complement) + (i + 1)]


"""
딕셔너리로 변환하여 첫번째 수를 뺀 결과 조회
1. 리스트의 밸류를 키로, 인덱스를 밸류로 바꿔서 딕셔너리로 저장한다.
2. 해당 딕셔너리를 순회하며, 타겟 넘버에서 첫번째 수를 뺀 값이 딕셔너리에 존재하는지 확인한다.
3. 해당 인덱스 값의 배열을 리턴한다.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
