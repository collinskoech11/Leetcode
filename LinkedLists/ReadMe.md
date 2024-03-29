# Linked Lists

A linked list is basically a data structure made up of nodes that are connected  to each other, each node can be thought of as a container of data 
THe difference between a linked list and an array is that an array must be stored contiguously in memory(next to each other) => Insertion has an O(n) runtime , while in a linked list youd create a new node which will exist anywhere in memory, and only adjus two pointers to accomondate the new node . 

## Types of Linked lists
- Singly Linked List
- Doubly LInked List

## Traverse through a Singly linked list 
- first we need a current variable, which will initially reffer to the head of the linked list .
- To go to the next node of the linked list we will refference current.next
- stop when curent is null
```
  (a) -> (b) -> (c) -> (d)
  |       |
current   |
      current.next
```
## Singly Linked List Implementation 
```javascript
class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}


const a = new Node('A');
const b = new Node('B');
const c = new Node('C');
const d = new Node('D');

a.next = b;
b.next = c;
c.next = d;

// (A) -> (B) -> (C) -> (D) -> NULL

```
## Traversal Algorithm
```javascript
const printLinkedList = (head) => {
    let current = head;
    while(current !== null){
        console.log(current.val)
        current = current.next;
    };
};
printLinkedList(a);
```
## Traversal Using recursion
```javascript
const printLInkedListRecursively = (head) => {
    if(haad === null) return;
    console.log(head.val);
    printLinkedLIstRecursively(head.next)
};
printLInkedLIstRecursively(a)
```
### Building an array with values from a linked list -> recursively
```javascript
const linkedList = (head) => {
    const values = []
    fillValues(head, values)
    return values;
}
const fillValues = (head, values) => {
    if(head === null){
        return;
    }
    values.push(head.val);
    fillValues(head.next, values);
}
```
### Getting the sum of values in a linked list
- for this case we are going to assume that the linked list we built earlier has integer values instead of letters , then we are going to compute the sum of the node values recursively
```javascript
const sumList = (head) => {
  if(head == null) return 0;
  const sum = head.val + sumList(head.next)
  return sum
}
console.log(sumList(a))
```
### find a target in a linked list
- traverse through the linked list 
- in each iteration check if the current.val is equal to the target => if so return true
- If we get to the end of the list => return false
```javascript
const findElem = (head, target) => {
    let current = head;
    while(current !== null){
        if(current.val == target){
            return true
        }
        current = current.next;
    }
    return false;
}
findElem(a, 3)
//returns false
```
#### recursive implementation
```javascript
const findElem = (head, target) => {
    if(head === null) return false;
    if(head.val == target) return true;
    findElem(head.next, 
}
```

## get the node value at a specific index 
- given a the head of a linked list and an index return the value at the index provided 
### Steps 
- create function that takes in a linked list and an index 
- return false if the head is null
- initialize a counter to keep track of what index we are currently at 
- initialize a var current to keep track of the the current node 
- create a while loop that only runs if current is not null
- Inside the while lop check if counter == index, if so return its val
- outside the if statement increment the counter and set the current to current.next

```javascript
const getNodeVal = (head, index) => {
  if(head == null) return null;
  let counter = 0;
  let current = head;
  while(current != null){
    if(counter == index) {
        return current.val
    }  
    counter += 1;
    current = current.next
  }
}
console.log(getNodeVal(a, 2))
```

### Recursive approach
```javascript
const getNodeVal = (head, index) => {
    if(head === null) return null;
    if(index === 0) return head.val; 
    return getNodeVal(head.next, index -1)
}
console.log(getNodeVal(a, 2))
```
## Reversing a linked list
- The solution to this problem is to shift all pointers to point backwards esentially reversing the linked list
```
Initial list = (a) -> (b) -> (c) -> (d)
reversed list = (a) <- (b) <- (c) <- (d) which is the same as (d) -> (c) -> (b) -> (a)
```
- for this we are going to ned three variables
    - prev : initially set to null
    - current : initially set to the head of the linked list
    - next :  set to current.next within the while loop
```
null -> (a) -> (b) -> (c)
prev    curr    next       => first iteration
```

- outside the loop we need to declare prev and current using let key word since we are going to be continuallly update within the function 
- while the current is not equal to null set next to current.next 
- set curent.next to prev to actually reverse the pointer
- update prev to current 
- update current to next (then repeat the whole process till current = null)
- at this point the whole linked list is reversed

```javascript
const reverseLinkedList = (head) => {
    let prev = null;
    let current = head;
    while(current!==null){
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next
    }
}
```

### recursive approach
```javascript
const reverseLInkedList = (head, prev = null) => {
    if(head === null) return prev
    const next  = head.next;
    head.next = prev;
    return reverseLinkedList(next, head)
}
reverseLinkedList(a)
```

## Zipped Lists
for this problem we are given two linked lists and the solution is to merge the two lists in alternating order of nodes, Note that if one linked list is longer than the other all we do is continue with the longer list after reaching the end of the shorter list .
```
// example
(a) -> (b) -> (c) -> (d) and (v) -> (w) -> (x) -> (y)
returns 
(a) -> (v) -> (b) -> (w) -> (c) -> (x) -> (d) -> (y)
```
### steps 
- we are going to initialize two pointers current1, current2 starting at the head for both linked lists respecively 

```javascript
const zipperLists = (head1, head2) => {
    if (head1 === null &&  head2 == null) return null;
    if (head1 === null) return head2
    if (head2 === null) return head1

    const next1 = head1.next
    const next2 = head2.next;
    head1.next = head2

    head2.next = zipperLists(next1,next2)

    return head1
}
console.log(zipperLists(a, v))
```
## Linked List Cycle
Given the head of a linked list return true if the linked list links back  to itself and false if it doesnt
```
example of a linked list with a cycle
(a) -> (b) -> (c) -> (d)
               |      |
              (f) <- (e)

```
To solve this we are going to use floyds cycle detection algorithm(Hare and tortoise Algorithm) , think of it as just using fast and slow pointers
### Steps
- initialize fast and slow pointers
- while head && head.next are not null 
- set the next fast pointer as fast.next.next and slow as slow.next
- if fast and slow are pointing to the same node, return true
- if the while comes to an end return false as there is no cycle

### Implementation 
```javascript
var hasCycle = function(head) {
    let slow = head;
    let fast = head;
    while(head){
        fast = fast.next.next;
        slow = slow.next;
        if(fast == second){
            return true;
        }
    }
    return false;
}
```

## Doubly Liked List Implementation 
Ulinlike a singly linked list a doubly linked list points to the next node and the previous node,hence the name doubly linked
```
    ->      ->
(A)     (b)    (C)
    <-      <-    
```

```javascript
class Node {
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}
```
Now that weve defined the node class lets go ahead and create our doubly linked lits and add values to it
```javascript
class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    push(val) {
        let node = new Node(val)
        if(!this.head){
            this.head = node;
            this.tail = node;
        } else {
            let temp = this.tail;
            this.tail = node;
            node.prev = temp;
            temp.next = node;
        }
        this.length ++;
        return this;
    }
}
let list = new DoublyLinkedList;
```




| Problem | My Solution | Review status |
| :-- | :-- | :-- |
| **linked list cycle** | [Accepted](solutions/202.%20Happy%20Number.md) | Reviewed |
| **palindrome linked list** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **reverse linked list(Fast & Slow)** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **Insertion sort** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **merge sort** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **remove duplicates from a sorted list** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **remove duplicates from a sorted list two** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **remove linked list elements** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **remove nth node frrom end of a linked list** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **reverse a linked list** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
| **reverse a linked list ii** | [Accepted](solutions/202.%20Happy%20Number.md) | Not Reviewed |
