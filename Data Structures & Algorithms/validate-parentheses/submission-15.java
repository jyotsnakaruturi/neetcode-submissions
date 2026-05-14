class Solution {
    public boolean isValid(String s) {
        if (s.length()<2){
            return false;
        }
        Stack<Character> stack = new Stack <>();
        Map<Character,Character> map = new HashMap<>();
        map.put('}','{');
        map.put(')','(');
        map.put(']','[');
        for(char i :s.toCharArray()){
            if (i == '{' || i=='(' || i == '['){
                stack.push(i);
            }
            else{
                if (stack.isEmpty() || map.get(i)!=stack.pop()){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
