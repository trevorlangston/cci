Linked lists are a _dynamic data structure_, implemented with pointers.

Complexity analysis:
Access O(n)
Search O(n)
Insert O(1)
Delete O(1)
Size O(n)

Advantages compared to array:
* constant time insertions and deletes
* dynamically allocated, no fixed size

Disadvantages compared to array:
* O(n) access
* more memory required to store each item

Single
* nodes have next pointer
* a single ll can serve as the tail to multiple other single ll, not
  possible in double ll

Double
* nodes have next and previous pointer
* can easy traverse forwards and backwards (e.g. browser history)
* insertions require more pointers to be updated
* deletions are simpler to implement with previous pointer

Motivation:
* memory management, e.g. heap
* linking in hash tables
* browser foward and back
* queues and stacks
