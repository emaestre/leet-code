import collections

class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        
        for s in strs:
            sorted_word = "".join(sorted(s))
            
            if sorted_word not in dic:
                dic[sorted_word] = [s]
            else:
                dic[sorted_word].append(s)
                       
        return dic.values()