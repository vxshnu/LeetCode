class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i=0
        l = min(len(first),len(last))
        print(l)
        if len(strs) == 1:
            return first
        if not first:
            return ""
        while i < l and first[i] == last[i]:
            i = i+1
        return first[:i]