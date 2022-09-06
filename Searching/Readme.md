# Binary Search
### Efficient algorithm for finding an item in a sorted list of items . it works by repeatedly dividing in half the partitionof the list that could contain the item , until you,ve narrowed down the possible locations to just one
### we basically ignore half of the elements afer just one iteration
### i) Compare x with the middle element 
### ii) if x matches the middle element, we retuen the mid index.
### iii) If  x is greater than the middle element, then can only lie in the right half subaray after the middle element. so we only recurr in the right half 
### iv) if x is smaller than the middle element we traverse through the left side 
### * each time we shift the L or R pointer towards the location of x
### * if r becomes < than l then the element is not in the array
```python
    l,r = 0, len(nums)-1
    if r >= l:
 
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
```
### Complexity analysis for Binary Search
`Sorted Array of 10 elements: 2, 5, 8, 12, 16, 23, 38, 56, 72, 91`

`Let us say we want to search for 23.`
#### Finding the given element: 

#### Now to find 23, there will be many iterations with each having steps as mentioned in the figure above: 

 

### Iteration 1: 
 

`Array: 2, 5, 8, 12, 16, 23, 38, 56, 72, 91`
`Select the middle element. (here 16)`

#### Since 23 is greater than 16, so we divide the array into two halves and consider the sub-array after element 16.

#### Now this subarray with the elements after 16 will be taken into next iteration.

### Iteration 2: 
 

`Array: 23, 38, 56, 72, 91`
`Select the middle element. (now 56)`

#### Since 23 is smaller than 56, so we divide the array into two halves and consider the sub-array before element 56.

#### Now this subarray with the elements before 56 will be taken into next iteration.
### Iteration 3: 
 

`Array: 23, 38`
`Select the middle element. (now 23)`

#### Since 23 is the middle element. So the iterations will now stop.

#### Let say the iteration in Binary Search terminates after k iterations. In the above example, it terminates after 3 iterations, so here k = 3

#### At each iteration, the array is divided by half. So let’s say the length of array at any iteration is n
### At Iteration 1, 
 
`Length of array = n`

#### At Iteration 2, 
 
`Length of array = n⁄2`

#### At Iteration 3, 
 
`Length of array = (n⁄2)⁄2 = n⁄22`

#### Therefore, after Iteration k, 
 
`Length of array = n⁄2k`

 

#### After k iterations, the length of array becomes 1

#### Therefore 
 
`Length of array = n⁄2k=1`
`=> n = 2k`

#### Applying log function on both sides: 
 
`=> log2 (n) = log2 (2k)`
`=> log2 (n) = k log2 (2)`
 

`as (loga (a) = 1) `

#### therefore, 
 
`=> k = log2 (n)`
####  Binary Search Algorithm whose complexity is O(log n). 
# Depth First Search
#### DFS is technique used for traversing tree or graph. Here backtracking is used for traversal. In this traversal first the deepest node is visited and then backtracks to it’s parent node if no sibling of that node exist. 

## Declaring a binary tree
```javascript
class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}


const a = new Node('a');
const b = new NOde('b');
const c = new NOde('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b
a.right = c
b.left = d
b.right = e;
c.right = f;

                 (a)
               /     \
             (b)     (c)
            /   \       \
          (d)   (e)     (f)
```

## DFS Traversal of a Graph vs Tree -> Typically Recursive requires  function called overhead 
Dfs uses a stack data structure 
a stack is a data structure that only allows us to pop from or append to the top of the stack
```javascript
const depthFirstSearch = (root) => {
    const stack = [root]
    while (stack.length > 0) {
        const current = stack.pop()
        console.log(current.val);
        
        if(current.left) stack.push(current.left)
        if(current.right) stack.push(current.right)
    }
}
```
#### DFS using recursion
```javascript
                 (1)
               /     \
             (2)     (3)
            /   \    
          (4)   (5)
```
```javascript
const depthFirstSearch = (root) => {
    if(root === null) return []
    const leftValues = depthFirstSearch(root.left)
    const rightValues = depthFirstSearch(root.right)
    return [root.val, ...leftValues, ...rightValues]
}
```
### Depth first traversals 
#### Inorder TRaversal(left-root-right)
```javascript
const depthFirstSearch = (root) => {
    if(root === null) return []
    const leftValues = depthFirstSearch(root.left)
    const rightValues = depthFirstSearch(root.right)
    return [...leftValues, root.val, ...rightValues]
}
// a) inOrder(left, root, right): 4 2 5 1 3
```
#### Preorder Traversal(Right-Root-Left)
```javascript
const depthFirstSearch = (root) => {
    if(root === null) return []
    const leftValues = depthFirstSearch(root.left)
    const rightValues = depthFirstSearch(root.right)
    return [...rightValues, root.val, ...leftValues]
}
//  b) preOrder(Root, left, right): 1 2 4 5 3
```
#### PostOrder TRaversal(Left-Right-Root)
```javascript
const depthFirstSearch = (root) => {
    if(root === null) return []
    const leftValues = depthFirstSearch(root.left)
    const rightValues = depthFirstSearch(root.right)
    return [...leftValues,...rightValues, root.val ]
}
// c) PostOrder(left, right, root): 4 5 2 3 1
```


###### In graph, there might be cycles and dis-connectivity. Unlike graph, tree does not contain cycle and always connected. So DFS of a tree is relatively easier. We can simply begin from a node, then traverse its adjacent (or children) without caring about cycles. And if we begin from a single node (root), and traverse this way, it is guaranteed that we traverse the whole tree as there is no dis-connectivity,

 
 ## Time Complexity: O(n) -> where n is the depth of the tree or graph
#### Auxiliary Space: If we don’t consider size of stack for function calls then O(1) otherwise O(n)

## BFS Traversal of a Graph vs Tree

In breadth first search we make use of the queue data structure which allows us to add elements to the back and leave from the front 
```javascript
                 (1)
               /     \
             (2)     (3)
            /   \    
          (4)   (5)
```
#### for Breadth First traversal of the tree above :
#### BFS: 1 2 3 4 5
### Implementation (Iteratively)
```javascript
const breadthFirstSearch = (root) => {
    if(root === null) return [];
    const queue = [root]
    const values = [];
    while(queue.length > 0) {
        const current = queue.shift()
        values.push(current)
        if(current.left !== null) queue.push(current.left);
        if(current.right == null) queue.push(current.right);
    }
    return values
}
```
### Recursive Implementation
```javascript
const treeIncludes = (root, target) => {
    if(root == null) return false;
    if(root.val === target) return true
    treeInculdes(root.left, target) || treeIncludes(root.right, target);
}
treeIncludes(a, "e") // check if the tree a includes "e"
```
## Time & Space complexity 

### Time Complexity * (four) traversal methods require O(n) time as they visit each node once 
### Space Complexity 
#### Extra space is required for level order traversal  is O(w) where w is the maximum width of the binary tree
#### Extra space is required for Depth first traversal  is O(H) where H is the maximum height of the binary tree

