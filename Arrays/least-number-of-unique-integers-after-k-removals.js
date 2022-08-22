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
