A _heap_ is an implementation of an ADT called a priority queue. Heaps are a
tree-based data structure and can be  either min-heaps or max-heaps. In a max
heap, every parent node is greater than it's children, and vice versa for
min-heaps. Note that there is no ordering amoungst child nodes.

Complexity analysis:
Extract Max O(lgn)
Insert O(lgn)

Buliding a heap from n elements: O(n)
Heap sort: O(nlgn)

Motivation:
* prioritizing network traffic, processes, jobs, etc.
* Dijkstra's shortest path algorithm
* heap sort
