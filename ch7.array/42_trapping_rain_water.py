"""
1. 가장 큰 높이를 기준으로 왼쪽, 오른쪽을 나눈다.
2. 왼쪽에서 다음으로 가장 큰 높이의 인덱스를 찾는다.
3. 그 사이의 넓이를 구하고, 높이만큼을 빼준다.
3. 오른쪽도 동일하게 반복한다.

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]

        while left < right:
            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]

        return water
