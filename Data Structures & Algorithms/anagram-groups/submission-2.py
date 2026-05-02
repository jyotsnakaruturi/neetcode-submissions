class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=defaultdict(list)
        for i in strs:
            I="".join(sorted(i))
            l[I].append(i)
         
        return list(l.values())