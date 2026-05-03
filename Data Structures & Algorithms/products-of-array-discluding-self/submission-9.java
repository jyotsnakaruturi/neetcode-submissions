class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arr = new int[nums.length];
        int prefix =1;
        int n= nums.length;
        for(int i=0;i<n;i++){
            arr[i] = prefix;
            prefix *= nums[i];
            
        }
        int postfix=1;
        for(int i=n-1;i>=0;i--){
            arr[i] *= postfix;
            postfix *= nums[i];
        }
        return arr;

        
    }
}  
