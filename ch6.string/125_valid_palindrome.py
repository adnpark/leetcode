
# Two Pointers: O(n)
# 1. 주어진 string을 포매팅한다. (uppercase to lowercase, remove non-alphanumerics)
# 2. 포매팅한 string의 맨 앞과 맨 뒤를 가리키는 포인터를 둔다.
# 3. 해당 포인터들이 가리키는 문자를 서로 비교해서 palindrome인지 판별한다.
class SolutionTwoPtrs:
    def isPalindrome(self, s: str) -> bool:
        formattedStr = self.formatString(s)
        startPtr: int = 0
        endPtr: int = len(formattedStr) - 1
        maxCount: int = len(formattedStr) // 2
        for i in range(0, maxCount, 1):
            if formattedStr[startPtr] != formattedStr[endPtr]:
                return False
            startPtr += 1
            endPtr -= 1
        return True

    def formatString(self, string: str) -> str:
        # remove non-alphanumeric characters
        alphanumerics = ''.join(filter(str.isalnum, string))
        # convert all chars to lowercase
        return alphanumerics.lower()


# Convert to List: O(n)
class SolutionList:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
