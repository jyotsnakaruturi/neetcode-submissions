class Solution {
    public int trap(int[] height) {
        int leftmax = height[0];
        int n= height.length;
        int rightmax = height[n-1];
        int l=0;
        int r = n-1;
        int res =0;
        while (l<r){
            if (leftmax < rightmax){
                l++;
                leftmax = Math.max(leftmax,height[l]);
                res += leftmax - height[l];
            }
            else{
                r--;
                rightmax = Math.max(rightmax,height[r]);
                res += rightmax - height[r];
            }

        }
        return res;

        
    }
}
