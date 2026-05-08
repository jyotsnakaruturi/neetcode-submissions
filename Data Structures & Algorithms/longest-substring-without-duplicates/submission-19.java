class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> seen = new HashSet<>();
        int max =0;
        int j=0;
        for(int i=0;i<s.length();i++){
            while(seen.contains(s.charAt(i))){
                seen.remove(s.charAt(j));
                j++;
            }
            seen.add(s.charAt(i));
            max = Math.max(max,i-j+1);
        }
        return max;
    }
}
