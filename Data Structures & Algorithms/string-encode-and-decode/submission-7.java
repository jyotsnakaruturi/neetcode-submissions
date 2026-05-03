class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String i : strs){
            sb.append(i.length());
            sb.append("#");
            sb.append(i);
             
        }
        String str = sb.toString();
        return str;

    }

    public List<String> decode(String str) {
        ArrayList<String> res = new ArrayList<>();
        
        int i=0;
        while (i < str.length()){
            int j=i;
            while(j < str.length() && str.charAt(j)!='#'){
                j++;
            }
            int length = Integer.parseInt(str.substring(i,j));
            String word = str.substring(j+1,j+1+length);
            res.add(word);
            i=j+1+length;
        }
        return res;

    }
}
