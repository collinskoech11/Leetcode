# Binary Search
### Efficient algorithm for finding an item in a sorted list of items . it works by repeatedly dividing in half the partitionof the list that could contain the item , until you,ve narrowed down the possible locations to just one
### we basically ignore half of the elements afer just one iteration
### i) Compare x with the middle element 
### ii) if x matches the middle element, we retuen the mid index.
### iii) If  x is greater than the middle element, then can only lie in the right half subaray after the middle element. so we only recurr in the right half 
### iv) if x is smaller than the middle element we traverse through the left side 
### * each time we shift the L or R pointer towards the location of x
### * if r becomes < than l then the element is not in the array
`
l,r = 0, len(nums)-1
    if r >= l: # Check base case
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1
 
 
`
# Depth First Search
