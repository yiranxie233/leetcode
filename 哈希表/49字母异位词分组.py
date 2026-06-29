"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。


示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
解释：
在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]

"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_map = {}
        # answer = []
        for s in strs:
            sort_s = ''.join(sorted(s)) 
            if sort_s in alpha_map:
                alpha_map[sort_s].append(s)
            else:
                alpha_map[sort_s] = [s]

        # for value in alpha_map.values():
        #     answer.append(value)
        # return answer
        return list(alpha_map.values())


# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d = defaultdict(list)
#         for s in strs:
#             sorted_s = ''.join(sorted(s))
#             d[sorted_s].append(s)


s = Solution()
strs = ['eat','tea','tan','ate','nat','bat']
print(s.groupAnagrams(strs))