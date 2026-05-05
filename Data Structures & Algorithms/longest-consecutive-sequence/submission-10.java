class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int i :nums){
            set.add(i);
        }
        int count =0 ;
        int length =0;
        for (int i : set){
            if (!set.contains(i-1)){
                length=1;
                while (set.contains(i+length)){
                    length+=1;
                }
            }
            count=Math.max(length,count);
        }
        return count;
    }
}
