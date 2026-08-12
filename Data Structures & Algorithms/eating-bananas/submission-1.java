class Solution {

    public int calc_time(int[] piles,int speed){
        int t = 0;
        for(int bana: piles){
            if(speed >= bana){
                t+=1;
            }else{
                int h = bana/speed;
                int rem = bana%speed;
                if(rem!=0){
                    t+=(h+1);
                }else{
                    t+=h;
                }
            }
        }

        System.out.println("Time "+t+" speed "+speed);
        return t;
    }

    public int minEatingSpeed(int[] piles, int h) {

        int min_eat = 1;
        OptionalInt max_eat_opt = Arrays.stream(piles).max();
        int max_eat = 0;
        int sol = Integer.MAX_VALUE;

        if (max_eat_opt.isPresent()) {
            max_eat = max_eat_opt.getAsInt();
        } else {
            System.out.println("Array is empty. No maximum value.");
            return -1;
        }

        while(max_eat>=min_eat){
            int mid = (max_eat + min_eat)/2;
            int t = calc_time(piles,mid);
            System.out.println(t);
            if(t>h){
                min_eat = mid+1;
            }else{
                sol = Math.min(sol,mid);
                max_eat = mid-1;
            }
        }
        
        return sol;

    }
}
