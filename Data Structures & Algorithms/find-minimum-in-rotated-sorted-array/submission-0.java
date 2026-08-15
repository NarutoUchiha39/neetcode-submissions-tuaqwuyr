class Solution {
    public int findMin(int[] nums) {

        int low = 0;
        int high = nums.length-1;
        int sol = Integer.MAX_VALUE;

        while(low <=high){
            int mid_index = (low+high)/2;
            int mid = nums[mid_index];
            // System.out.println("Mid "+mid+" sol "+sol+" low "+low+" high "+high);
            if(mid>nums[high]){
                low = mid_index+1;
            }else{
                sol = Integer.min(sol,mid);
                high = mid_index-1;
            }
        }

        return sol;
        
    }
}