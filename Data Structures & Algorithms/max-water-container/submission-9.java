class Solution {
    public int maxArea(int[] heights) {
        int l=0;
        int r= heights.length -1;
        int maxe =0;
        
        while(l<r){
            int hei = Math.min( heights[l], heights[r]);
            int breath = r-l;
            maxe = Math.max(maxe,hei*breath);
            if( heights[l]< heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxe;
        
        
    }
}
