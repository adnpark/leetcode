"""
1. 우선 주어진 paragraph를 lowercase로 변환한다.
2. space, punctuation(!?',;.)을 기준으로 split해서 list로 만든다.
3. banned에 포함되지 않은 단어들을 dictionary에 저장한다. key = word, value = count
4. dictionary에서 가장 많이 등장한 단어를 리턴한다.

"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'[ \n\r\t.,;!?\']+', paragraph.lower())
        words = [word for word in words if word not in banned and word != '']
        wordDict = {}
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        return max(wordDict, key=wordDict.get)


# Optimized Ver. with list comprehension and counter object
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
        # [['ball', 2], ...]
