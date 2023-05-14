"""
Two Pointers
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptrStart: str = ''
        ptrEnd: str = ''

        for i in range(0, len(s) // 2, 1):
            ptrStart = s[i]
            ptrEnd = s[len(s) - 1 - i]
            s[i] = ptrEnd
            s[len(s) - 1 - i] = ptrStart


"""
Two Pointers - Neat Ver.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1  # 이런식으로 변수를 여러개 동시에 선언 및 할당 가능
        while left < right:  # left == right 인 순간이 교차점일 것이므로(length가 홀수인 경우)
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


"""
Pythonic Way
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
