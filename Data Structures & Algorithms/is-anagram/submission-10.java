class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
       HashMap <Character,Integer>maps= new HashMap<>();
       HashMap <Character,Integer>mapt= new HashMap<>();
        for(Character i : s.toCharArray()){
            maps.put(i,maps.getOrDefault(i,0)+1);
        }
        for(Character i : t.toCharArray()){
            mapt.put(i,mapt.getOrDefault(i,0)+1);
        }
        return maps.equals(mapt);

    }
}
