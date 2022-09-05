# Sorting
| Problem | My Solution | Review status |
| :-- | :-- | :-- |
| **Majority Element** | [Accepted](Sorting/majority-element) | Reviewed |
| **Majority Element ii** | [Accepted](Sorting/majority-element) | Reviewed |

# Bubble Sort Algorithm

Involves swapping of adjascent elements if the left element is greater than the one to its right 

e.g
nums = [4,3,5,6,8,7]

at the first step 4 - 3 would be swapped 
until the whole array is sorted 

```javascript
  function bubbleSort(array) {
  // Only change code below this line
  for (let i = 0; i < array.length - 1; i++){
    for(let j = 0; j < array.length - 1- i; j++){
      if(array[j] > array[j+1]){
        const temp = array[j];
        array[j] = array[j+1];
        array[j+1] = temp;
      }
    }
  }
  return array;
  // Only change code above this line
}
console.log(bubbleSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))

```
