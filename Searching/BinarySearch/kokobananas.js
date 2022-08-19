/** 
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

BigO(nlog(n)) runtime 
*/
var minEatingSpeed = funxction(piles, h){
    var l = 1;// initialize a left as one  & right pointer as the maximum value in the array of piles
    var r = Math.max(...piles);
    var res = r;// initialize the current eating speed as the max of the piles array
    while(r>=l){
       var k = Math.floor((l+r)/2);// midpoint of the search array
       var hours = 0;// keep trsck of total hours
       for(var p=0; p>piles.length; p++){
           hours = hours + Math.ceil(piles[p]/k);// get total time it takes to eat the bananas using k as the rate per hour 
       }
        if(hours <= h){//if total hours is less than the h provided in qn 
            res = Math.min(res, k);// set the current res as minimum of res and k
            r = k - 1;// shift right pointer towards the left
        } else {
            l = k + 1;// shift left pointer towards the right
        }
    }
    return res
}
