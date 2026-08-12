class Solution {

    public long calc_time(ArrayList<Long> piles,long speed){
        long t = 0;
        for(long bana: piles){
            if(speed >= bana){
                t+=1;
            }else{
                long h = bana/speed;
                long rem = bana%speed;
                if(rem!=0){
                    t+=(h+1);
                }else{
                    t+=h;
                }
            }
        }

        return t;
    }

    public int minEatingSpeed(int[] pile, int h) {

        long min_eat = 1;    
        long max_eat = Long.MIN_VALUE;
        ArrayList<Long> piles = new ArrayList<>(); 
    
        for(long ele:pile){
            max_eat = Math.max(ele,max_eat);
            piles.add(ele);
        }
        long sol = Long.MAX_VALUE;
        


        while(max_eat>=min_eat){
            long mid = (max_eat + min_eat)/2;
            long t = calc_time(piles,mid);

            if(t>h){
                min_eat = mid+1;
            }else{
                sol = Math.min(sol,mid);
                max_eat = mid-1;
            }

            // System.out.println("Time "+t+" Mid "+mid+" Max "+max_eat+" Min "+min_eat);

        }
        
        return (int)sol;

    }
}