# Inserton Sort
## Quadratic Runtime -> O(n^2)
[2,6,5,1,3,4] -> asssuming we are to sort this array using insertion sort 
## we frst split the array into two parts i.e sorted and unsorted 
   [2, | 6.5.1.3.4] 
sorted | unsorted 
## First iteration is to shift 6 to the sorted side and compare it to the elements that are in the sorted side 
[2,6, | 5,1,3,4] -> since they are in the correct order we move to the next iteration
## Second Iteration shifts 5 to sorted side 
[2,6,5, | 1,3,4] -> we then check if 5 has been placed correctly <br/>
[2,5,6, | 1,3,4] -> since it isnt we swap it with 6 <br/>
## Third iteration shifts 1 
[2,5,6,1, | 3,4] -> we then check if 1 has been placed correctly
[2,5,1,6, | 3,4] -> since 1 is smaller than 6 we swap the two(1,6)<br/>
[2,1,5,6, | 3,4] -> since 1 is smaller than 5 we swap the two(1,5)<br/>
[1,2,5,6, | 3,4] -> since 1 is smaller than 2 we swap the two(1,2)<br/>
## Fourth Iteration shifts 3 to the sorted side 
[1,2,5,6,3, | 4] -> we then check if 3 has been placed correctly<br/>
[1,2,5,3,6, | 4] -> since 3 is smaller than 6 we swap the two(3,6)<br/>
[1,2,3,5,6, | 4] -> since 3 is smaller than 5 we swap the two(3,5)<br/>
-> at this poit all elements in the sorted side are correctly sorted <br/>
## Fifth Iteration shifts 4 to the sorted side (last element)
[1,2,3,5,6,4 | ] -> we then check if 4 has been placed correctly<br/>
[1,2,3,5,4,6 | ] -> since 4 is smaller than 6 we swap the two(4,6)<br/>
[1,2,3,4,5,6 | ] -> since 4 is smaller than 5 we swap the two(4,5)<br/>

## Our array is now fully sorted since the unsorted part is empty
