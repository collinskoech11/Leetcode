# Inserton Sort
## Quadratic Runtime -> O(n^2)
[2,6,5,1,3,4] -> asssuming we are to sort this array using insertion sort 
## we frst split the array into two parts i.e sorted and unsorted 
   [2, | 6.5.1.3.4] 
sorted | unsorted 
## First iteration is to shift 6 to the sorted side and compare it to the elements that are in the sorted side 
[2,6, | 5,1,3,4] -> since they are in the correct order we move to the next iteration
## Second Iteration shifts 5 to sorted side 
[2,6,5, | 1,3,4] -> we then check if 5 has been placed correctly
[2,5,6, | 1,3,4] -> since it isnt we swap it with 6
## Third iteration shifts 1 
[2,5,6,1, | 3,4] -> we then check if 1 has been placed correctly
[2,5,1,6, | 3,4] -> since 1 is smaller than 6 we swap the two(1,6)
[2,1,5,6, | 3,4] -> since 1 is smaller than 5 we swap the two(1,5)
[1,2,5,6, | 3,4] -> since 1 is smaller than 2 we swap the two(1,2)
## Fourth Iteration shifts 3 to the sorted side 
[1,2,5,6,3, | 4]
