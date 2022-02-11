# Basic Concepts for Coding Interviews 
| Data Structures | Algorithms | Concepts |
| :-- | :-- | :-- |
| [Linked Lists](Linked%20Lists/) | [Breadth First Search](Searching/) | [Bit Manipulation](Searching/) |
| [Trees Tries & Graphs](Linked%20Lists/) | [Depth First Search](Searching/) | [Memory(Stack vs Heap)](Searching/) |
| [Stacks & Queues](Linked%20Lists/) | [Binary Search](Searching/) | [Recursion](Searching/) |
| [Heaps](Linked%20Lists/) | [Merge Sort](Searching/) | [Duynamic Progrmming](Searching/) |
| [Vectors/ArrayLists](Linked%20Lists/) | [Quick Sort](Searching/) | [Big O Time & Space](Searching/) |
| [Hash Tables](Linked%20Lists/) |  |  |
| [Arrays](Linked%20Lists/) |  |  |


# [Time and Space Complexity](https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/tutorial/)
### Time Complexity -> 
##### quanitfies the time taken by an algorithm to run as a function of the length of the input (not actual execution time of the machine on which the algorithms run on )

### assume constant time(c) is taken to run one operation [Ref](https://www.geeksforgeeks.org/time-complexity-and-space-complexity/)

| Length of input | Worst Accepted Algorithm | 
| :-- | :-- | 
| **<= [10..11]** | [O(N),O(N^6)] | 
| **<= [15..18]** | [O(2^N*N^2)] | 
| **<= [18..22]** | [O(2^N*N)] | 
| **<= [100]** | [O(N^4)] | 
| **<= [400]** | [O(N^3)] | 
| **<= [2000]** | [O(N^2*logN)] | 
| **<= 10k** | [O(N^2)] | 
| **<= [1M]** | [O(N*logN)] | 
| **<= [100M]** | [O(N),O(logN),O(1)] | 

### Space Complexity -> 

##### quantifies the amount of space or memory taken by an algorithm to run as a function of the length of the input


# Solution guidelines 
| Input Type | Category | Review status |
| :-- | :-- | :-- |
| **Input array is sorted** | [Binary Search, Two Pointers](Searching/) | :heavy_check_mark: |
| **asked for all permutations/subsets** | [Backtracking](Backtracking) | :x: |
| **Binary Tree** | [BFS, DFS](Searching/) | :white_check_mark: |
| **Graph** | [BFS, DFS](Searching/) | :x: |
| **Linked List** | [Two Pointers](Two_Pointers/) | :white_check_mark: |
| **If Recursion not allowed** | [Stack](Stacks/) | :white_check_mark: |
| **In Place Traversal** | [Swap corresponding values](Searching/BFS) | :heavy_check_mark: |
| **Mximum/MInimum subarray/subset/options** | [Dynamic Programing](DynamicPrograming/) | :white_check_mark: |
| **top/least k items** | [Heap](Sorting/) | :x: |
| **Common Strings** | [Map, Trie](Searching/) | :x: |
| **Otherwise** | [Map/Set](Searching/) | :white_check_mark: |

