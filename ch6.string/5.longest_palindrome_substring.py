"""
1. 각 char를 dictionary에 count한다.
2. dict를 순회한다.
3. count가 2 이상인 경우, 2로 나눈 몫의 수만큼 char들을 result string에 앞뒤로 붙여준다.
4. 마지막으로 string의 length가 홀수인 경우, result string의 가운데에 count가 홀수인 char를 하나 삽입한다.
=> 이 알고리즘은 잘못됐음 
문제 이해를 잘못했다! substring은 string의 순서를 바꾸면 안됐음!
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        if len(s) == 2 and s[0] == s[1]:
            return s

        if len(s) == 2 and s[0] != s[1]:
            return s[0]

        result = ""
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
            if char_dict[char] == len(s):
                return s
        for key in char_dict:
            if len(result) + 3 >= len(s):
                break
            if char_dict[key] >= 2:
                result = key * (char_dict[key] // 2) + \
                    result + key * (char_dict[key] // 2)
                char_dict[key] = 0
        if len(s) % 2 != 0 and len(result) + 1 < len(s):
            for key in char_dict:
                if char_dict[key] != 0:
                    result = result[:len(result) // 2] + \
                        key + result[len(result) // 2:]
                    break
        return result


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]

        result = ""
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
