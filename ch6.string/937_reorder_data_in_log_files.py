"""
1. 먼저 letter string과 digit string list로 구분한다.
2. letter string list를 lexicographically 하게 정렬한다.
3. digit string list는 기존 순서를 그대로 유지한다.
4. 두개의 string list를 join 한다.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) == 1:
            return logs

        letterStr: List[str] = []
        digitStr: List[str] = []

        for log in logs:
            if log.split()[1].isalpha():
                letterStr.append(log)
            else:
                digitStr.append(log)

        # 근데 이렇게 그냥 sort 함수 써버리면 연습의 의미가 있나? sorting 알고리즘을 구현해야 하는거 아닌가? 흠...
        letterStr.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letterStr + digitStr


class SolutionOptimized:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                digits.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
