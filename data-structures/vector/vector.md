A _vector_ is a dynamic array, meaning it can grow and shink in size as opposed
to a normal array. Arrays are implemented as vectors in higher level languages.
Despite resizing, appending and popping elements from the tail is still O(1)
amortized. This makes them a great implementation for dynamically sized
stacks.

Complexity analysis:
Access O(1)
Search O(n)
Insert O(n)
Delete O(n)

Motivation:
* any array whose size is not known at compile time
* stacks
