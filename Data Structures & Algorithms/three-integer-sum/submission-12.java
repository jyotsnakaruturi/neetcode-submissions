class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n= nums.length;
        for (int i=0;i<n;i++){
            if((i>0) && (nums[i] == nums[i-1])){
                continue;
            }
            int r= n-1;
            int l =i+1;
            while (l<r){
                int sum = nums[i]+nums[l]+nums[r];
                if (sum == 0){
                    ArrayList<Integer> list = new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[r]);
                    list.add(nums[l]);
                    res.add(list);
                    r--;
                    l++;
                    while (l<r && r<n-2 && nums[r]==nums[r+1]){
                        r--;
                    }
                    while (l<r && nums[l] == nums[l-1]){
                        l++;
                    }
                }
                else if(sum >0){
                    r--;
                }
                else{
                    l++;
                }
            }
        }
        return res;
         
    }
}
