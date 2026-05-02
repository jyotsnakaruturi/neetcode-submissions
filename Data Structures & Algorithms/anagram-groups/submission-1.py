class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        S=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            S[key].append(i)
        result=[]
        for key,value in S.items():
            result.append(value)
        return result