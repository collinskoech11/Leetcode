# Arrays
### 1D array example nums = [1,2,3,4,5] (also nums: list[int])
## indexing 
nums[0] = 1
nums[-1] = 5



## Container with the most water
given an integer array of length n, there are n vertical ines drawn such that the two endponts of the ith line are (i, 0) and (i, height[i]). 
find two lines that together with the x axis form a container , such that the container contains the most water. 
return the maximum amount of water the container can store.
Note that you may not  slant the container.

### Naive approach 
Steps 
    - initialize the max_volume as 0
    - run two nested loops on with i and the other with j (let j start as i+1) => to reduce the number of times we go through the loop
    - calculate the current volume as (Math.min(height[i], height[j]) * (j -i)
    - get the max volume by comparing the current_volume and the maximum_volume  => Math.max(volume,  current_volume)
    - outside the nested loops return the volume
    
##### Implementation 
```javascript
var maxArea = function(height) {
    var volume = 0;
    for(let i = 0; i<height.length;  i++){
        for(let j = i; j<height.length; j++){
            let x = Math.min(height[i], height[j])
            var current_volume = x * (j-i);     
            volume = Math.max(volume, current_volume)
        }
    }
    return volume;
}
```

### Binary Search solution
```javascript
var maxArea = function(height) {
    let r = height.length-1;
    let l = 0;
    let max_area=0;
    let current_area;
    while( r > l){
        current_area = (r-l) * Math.min(height[r],height[l])
        if(current_area > max_area){
            max_area = current_area;
        }
        if(height[l] < height[r]){
            l++;
        }
        else {
            r --;
        }
    }
    return max_area;
```
