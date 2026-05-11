class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character,Integer> s1_map = new HashMap<>();
        for(char i : s1.toCharArray()){
            s1_map.put(i,s1_map.getOrDefault(i,0)+1);
        }
        HashMap<Character,Integer> s2_map = new HashMap<>();
        int l=0;
        for (int r=0;r<s2.length();r++){
            s2_map.put(s2.charAt(r),s2_map.getOrDefault(s2.charAt(r),0)+1);
            if (r-l == s1.length()-1){
                if( s2_map.equals(s1_map)){
                    return true; 
                } 
                s2_map.put(s2.charAt(l),s2_map.get(s2.charAt(l))-1 );
                if (s2_map.get(s2.charAt(l)) == 0){
                    s2_map.remove(s2.charAt(l));
                }
                l++;
            }

        }
        return false;
        
    }
}
