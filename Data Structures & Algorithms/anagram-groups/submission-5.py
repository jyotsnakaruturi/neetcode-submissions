class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for i in strs:
            k="".join(sorted(i))
            map[k].append(i)
        return list(map.values())