class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map ={}
        for i in range (len(numbers)):
            num = target - numbers[i]
            if num in map:
                return [map.get(num)+1,i+1]
            map[numbers[i]]=i
        