class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map = new HashMap<>();
        for(String i : strs){
            char[] S=i.toCharArray();
            Arrays.sort(S);
            String s = new String(S);
            if(map.containsKey(s)){
                map.get(s).add(i);
            }
            else{
                List<String> list = new ArrayList<>();
                list.add(i);
                map.put(s,list);
            }
        }
        List<List<String>> l = new ArrayList<>();
        for (String key : map.keySet()){
            l.add(map.get(key));
        }
        return l;
        
    }
}
