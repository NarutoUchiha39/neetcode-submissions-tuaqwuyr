class Solution {

    public int requiredDays(int[]weights,int weight){

        int d = 0;
        int curSum = 0;
        // System.out.println(weight+"==============>");
        for(int w: weights){
            curSum+=w;
            if(curSum > weight){
                curSum = w;
                d+=1;
            }
            // System.out.println(curSum+" "+d+" "+w);

        }
        // System.out.println(weight+"==============>");

        return d+1;
    }

    public int shipWithinDays(int[] weights, int days) {
        OptionalInt min_weight_opt = Arrays.stream(weights).max();
        if(!min_weight_opt.isPresent()){
            return -1;
        }

        int min_weight = min_weight_opt.getAsInt();
        int max_weight = Arrays.stream(weights).sum();
        int sol = Integer.MAX_VALUE;

        while(min_weight <= max_weight){
            int mid = (min_weight+max_weight)/2;
            int d = requiredDays(weights,mid);
            if(d<=days){
                sol = Math.min(sol,mid);
                max_weight = mid-1;
            }else{
                min_weight = mid+1;
            }
        }

        return sol;

    }
}