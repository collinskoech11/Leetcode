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
## Linked Listt Implementation 
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
