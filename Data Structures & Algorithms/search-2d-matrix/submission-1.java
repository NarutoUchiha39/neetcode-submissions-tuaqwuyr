class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int lo = 0;
        int rows = matrix.length;
        int cols = matrix[0].length;
        int hi = (rows*cols)-1;

        while(lo <= hi){
            int mid = (int)Math.floor((lo+hi)/2);
            int mid_row = (int)Math.floor(mid/cols);
            int mid_col = (int)Math.floor(mid%cols);
            
            int mid_element = matrix[mid_row][mid_col];
            // System.out.println("Mid element "+mid_element+" Mid Row "+mid_row+" Mid Col "+mid_col+" Mid "+mid+" Low "+lo+" hi "+hi);


            if(mid_element == target){
                return true;
            }else if(mid_element < target){
                lo = mid+1;
            }else if(mid_element > target){
                hi = mid -1;
            }
        }

        return false;
        
    }
}