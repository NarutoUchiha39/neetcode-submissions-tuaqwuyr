class Solution {
    public boolean search(int[] nums, int target) {

        int low = 0;
        int high = nums.length-1;

        while(low<=high){
            int mid_index = (low+high)/2;
            int mid = nums[mid_index];
            
            if(mid == target){
                return true;
            }

            while(nums[low] == mid && mid == nums[high]){
                if(mid_index!=low && mid_index!=high){
                    low+=1;
                    high-=1;
                }else{
                    break;
                }
                    
            }

            if(mid >= nums[low]){

                if(target>=nums[low] && target<mid){
                    high = mid_index-1;
                }else{
                    low = mid_index+1;
                }
            }else{
                if(target<=nums[high] && target>mid){
                    low = mid_index+1;
                }else{
                    high = mid_index-1;
                }
            }
        }

        return false;
        
    }
}