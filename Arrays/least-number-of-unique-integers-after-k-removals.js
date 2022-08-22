/**
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
*/

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findLeastNumOfUniqueInts = function(arr, k) {
    counter = {}
    arrayun = []
    keep = 0
    for(let val of arr){
        if(counter[val] > 0){
            counter[val]++;
        } else {
            counter[val] =1
        }
    }
    console.log(counter);
    var count = Object.keys(counter).length
    console.log(count)
    for(const [key, value] in Object.entries(counter)){
        k -= value
        if(k<0){
            return count
        } else {
            count-=1  
        }
        return count
    }
};
