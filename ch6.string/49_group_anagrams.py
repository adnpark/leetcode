"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

1. strs를 순회하며 각 string을 먼저 가져와서 dictionary에 각 char를 count를 해준다.
2. 그리고 나머지 string들을 가져와서 같은 char count를 가지고 있는지 확인한다.
3. 만약 같다면 해당 string들을 같은 list에 넣어준다.

"""


# Wrong Answer
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: List[List[str]] = []
        for str in range(len(strs)):
            str_char_count = {}
            anagrams: List[str] = []
            for char in str:
                if char in str_char_count:
                    str_char_count[char] += 1
                else:
                    str_char_count[char] = 1
            for i in range(str + 1, len(strs)):
                str_i_char_count = {}
                for char in strs[i]:
                    if char in str_i_char_count:
                        str_i_char_count[char] += 1
                    else:
                        str_i_char_count[char] = 1
                if str_char_count == str_i_char_count:
                    anagrams.append(strs[i])
            result.append(anagrams)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict를 이용하면 default value를 초기화해서 위 코드처럼 복잡하게 안해줘도 된다.
        anagram_dict = defaultdict(list)

        for s in strs:
            # Use tuple of character counts as the dictionary key
            # dict의 key로는 tuple을 사용할 수 있다. 이런 식으로 사용하면, string이 다르더라도 sorted를 했기 때문에 같은 key를 가지게 된다.
            key = tuple(sorted(s))
            anagram_dict[key].append(s)
            # print(anagram_dict)를 하면 아래와 같이 출력됨
            # defaultdict(<class 'list'>, {('a', 'e', 't'): ['eat', 'tea'], ('a', 'n', 't'): ['tan']})

        return anagram_dict.values()
