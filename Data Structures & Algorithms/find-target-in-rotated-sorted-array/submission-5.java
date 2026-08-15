class Solution {
    public int search(int[] nums, int target) {
        
        int low = 0;
        int high = nums.length-1;
        int sol = -1;

        while(low <=high){
            int mid_index = (low+high)/2;
            int mid = nums[mid_index];
            // System.out.println("Mid "+mid+" sol "+sol+" low "+low+" high "+high);
            if(target == mid){
                return mid_index;
            }
            if(nums[low]>=nums[high]){
                if(target>=nums[low]){
                    if(mid > target && mid >= nums[low]){
                        high = mid_index-1;
                    }else if(mid < target && mid >= nums[low]){
                        low = mid_index+1;
                    }else{
                        high = mid_index-1;
                    }
                }else if(target<nums[low]){
                    low = low+1;
                }
            }else if(nums[low]<nums[high]){
                if(target<=nums[high]){
                    if(mid > target && mid >= nums[low]){
                        high = mid_index-1;
                    }else if(mid < target && mid >= nums[low]){
                        low = mid_index+1;
                    }else{
                        high = mid_index+1;
                    }
                }else if(target>nums[high]){
                    high = high-1;
                }
            }
        }

        return -1;
    }
}
