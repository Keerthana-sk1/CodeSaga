#RANSOM_NOTE
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h_map_rstr={}
        h_map_mstr={}
        flag=True
        for ch in ransomNote:
            h_map_rstr[ch]=h_map_rstr.get(ch,0)+1
        for ch in magazine:
            h_map_mstr[ch]=h_map_mstr.get(ch,0)+1
        for ch in h_map_rstr:
            if ch not in h_map_mstr:
                flag=False
                return flag
            elif ch in h_map_mstr and h_map_rstr[ch]<=h_map_mstr[ch]:
                continue
            else:
                flag=False
                return flag
        return flag

#M2

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
