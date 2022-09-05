# Sorting
| Problem | My Solution | Review status |
| :-- | :-- | :-- |
| **Majority Element** | [Accepted](Sorting/majority-element) | Reviewed |
| **Majority Element ii** | [Accepted](Sorting/majority-element) | Reviewed |

## Bubble Sort Algorithm

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
        // const temp = array[j];
        // array[j] = array[j+1];
        // array[j+1] = temp;
        [array[j], array[j+1]] = [array[j+1], array[j]]
      }
    }
  }
  return array;
  // Only change code above this line
}
console.log(bubbleSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))

//returns [ 1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643 ]

```
Time Complexity => O(n^2)
Space complecity => O(1)

## Selection Sort

Involves selecting the minimum value in a list and swapping it with the first value in the list Then repeats the same process but starting at the second value in the list

e.g
nums = [4,3,5,1,8,7]

at the first step 4 - 1 would be swapped 
until the whole array is sorted 

```javascript
function selectionSort(array) {
  // Only change code below this line
  for (let i= 0; i < array.length -1; i++){
    let minIndex = i;
    for(let j = i+1; j < array.length; j++){
      minIndex = j;
    }
    const temp = array[i];
    array[i] = array[minIndex]; 
    array[minIndex] = temp
  }
  return array;
  // Only change code above this line
}
console.log(selectionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))
// returns => [ 92, 1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234 ]
```

## Insertion Sort

Works by building up a sorted array at the beginning of the list , begins the sorted array woth the first element in the list , then it inspects the next element and swaps it backwards into the sorted array  until it is in its sorted position

```javascript
function insertionSort(array) {
  // Only change code below this line
  for (let i = 1; i < array.length; i++){
    for(let j = i; j > 0; j--){
      if(array[j] < array[j-1]){
        [array[j], array[j-1]] = [array[j-1], array[j]]
      } else {
        break;
      }
    }
  }
  return array;
  // Only change code above this line
}
insertionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92])
```
