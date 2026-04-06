class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_map={}
        t_map={}
        for ch in s:
            if ch in s_map.keys():
                s_map[ch]+=1
            else:
                s_map[ch]=1
        for ch in t:
            if ch in t_map.keys():
                t_map[ch]+=1
            else:
                t_map[ch]=1
        for key,value in s_map.items():
            if key not in t_map.keys():
                return False
            if value!=t_map[key]:
                return False

        return True        