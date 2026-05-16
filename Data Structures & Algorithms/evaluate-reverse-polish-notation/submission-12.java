class Solution {
    public int evalRPN(String[] tokens) {
        Stack <Integer>stack = new Stack<>();
        for(String i :tokens){
            if (i.equals("+")){
            int a = stack.pop();
            int b = stack.pop();
            stack.push(a+b);
            }
            else if(i.equals("*")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(a*b);
            }
            else if(i.equals("-")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(a-b);
            }
            else if (i.equals("/")){
                int a = stack.pop();
                int b = stack.pop(); 
                int c = (int)b/a;
                stack.push(c);
            }
            else{
                int c = Integer.parseInt(i);
                stack.push(c);
            }
        }
        int c =stack.pop();
        return c;
        
    }
}
