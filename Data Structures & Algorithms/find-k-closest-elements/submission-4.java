class Solution {

    public int BinarySearch(int[]arr,int element){
        int left = 0;
        int right = arr.length-1;
        int mid = 0;
        while(left<=right){
            mid = (int)Math.floor((left + right)/2);
            if(element > arr[mid]){
                left = mid+1;
            }

            else if(element < arr[mid]){
                right = mid - 1;
            }

            else{
                return mid;
            }
        }

        return mid;
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {


        int index = BinarySearch(arr,x);
        ArrayList<Integer> result = new ArrayList(k);
        if (arr[index]<x){
            index+=1;
        }
        System.out.println(index);


        if(x < arr[0]){
            int index1 = 0;
            for(int a:arr){
                if(index1==k){
                    break;
                }
                result.add(a);
                index1+=1;
            }
        }

        else if(x > arr[arr.length-1]){
            for(int a = arr.length-k;a<=arr.length -1;a++){
                result.add(arr[a]);
            }
        }

        else{
            int num = 0;
            int left = index -1;
            int right = index;

            while(num < k){    
                
                int diff_l = Integer.MAX_VALUE;
                int diff_r = Integer.MAX_VALUE;

                if(left >= 0){
                    diff_l = Math.abs(arr[left]-x);
                }

                if(right <= arr.length-1){
                    diff_r = Math.abs(arr[right]-x);
                }

                if(diff_l > diff_r){
                    result.add(arr[right]);
                    right++;
                    num+=1;
                }else if(diff_r >= diff_l){
                    result.add(0,arr[left]);
                    left --;
                    num+=1;
                }

            }
        }
        return result;        
    }
}