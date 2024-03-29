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

### Implementation

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

### Implementation

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

### Implementation

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
## Quick Sort 
Divide and conquer approach
select a pivot value fromthe array the array is then partitioned into two sub arrays one with values greater than the pivot and the other with values 
smaller than the pivot selected, this is repeated until we get  an empty array or a single element array. 
Unwinding at the recursive calls returns the sorted array

### Implementation

```javascript
function quickSort(array) {
  // Only change code below this line
  // edge case
  if(array.length  === 1){
    return array;
  }
  const pivot = array[array.length -1]
  const leftArr = []
  const rightArr = []
  for (let i = 0; i < array.length -1; i++){
    if(array[i] < pivot){
      leftArr.push(array[i])
    } else {
      rightArr.push(array[i])
    }
  }
  if (leftArr.length > 0 && rightArr.length > 0){
    return [...quickSort(leftArr), pivot, ...quickSort(rightArr)]
  } else if (leftArr.length > 0){
    return [...quickSort(leftArr), pivot]
  } else {
    return [pivot, ...quickSort(rightArr)]
  }
  return array;
  // Only change code above this line
}
quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92])
```
## Merge sort

Implements divide and conquer just like wuick sort, Recursively split the input array until we get a sub array with only one element 
Merge the split array to form a sorted array

```javascript
// leftArr and rightArr are sorted 
const merge = (leftArr, rightArr) => {
  const output = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while(leftIndex < leftArr.length && rightIndex < rightArr.length) {
    const leftEl = leftArr[leftIndex];
    const rightEl = rightArr[rightIndex];

    if(leftEl < rightEl){
      output.push(leftEl);
      leftIndex++;
    } else {
      output.push(rightEl);
      rightIndex++;
    }
    return [...output, ...leftArr.slice(leftIndex), rightArr.slice(rightIndex)];
  }
}

const  mergeSort = array=> {
  // Only change code below this line
  if(array.length <= 1){
    return array;
  }
  const middleIndex = Math.floor(array.length / 2);
  const leftArr = array.slice(0, middleIndex);
  const rightArr = array.slice(middleIndex)
  return merge(
    mergeSort(leftArr),
    mergeSort(rightArr)
  );
  // Only change code above this line
}
mergeSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92])
```
