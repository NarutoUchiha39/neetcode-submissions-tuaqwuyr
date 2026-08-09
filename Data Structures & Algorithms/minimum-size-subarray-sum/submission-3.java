class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int curSum = 0;
        int sol = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            curSum += nums[right];

            while (curSum >= target) {
                sol = Math.min(sol, right - left + 1);
                curSum -= nums[left];
                left++;
            }
        }

        return sol == Integer.MAX_VALUE ? 0 : sol;
    }
}