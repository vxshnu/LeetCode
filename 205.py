class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for i in range(0,len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = i
            if t[i] not in mapping_t:
                mapping_t[t[i]] = i
        if len(mapping_t) == len(mapping_s):
            for v1,v2 in zip(mapping_s.values(),mapping_t.values()):
                if v1==v2:
                    continue
                else:
                    return False
            return True
        else:
            return False
