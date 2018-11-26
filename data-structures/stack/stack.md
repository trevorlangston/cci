A _stack_ is an ADT that supports push and pop operations. It is
implemented as a linear data structure that follows the FILO (first in, last
out) rule. A stack of plates follows this ordering - the last plate placed on
the stack is the first one removed. A stack may be implemented as an array if
it is fixed in size. For dynamically sized stacks, either a dynamic array or
singly linked list are used.

Complexity analysis:
Pop O(1)
Push O(1)

Motivation:
* memory management of a program, i.e. the call stack
* syntax parsing, e.g. balancing parentheses
* backtracking, e.g. undo in text editor
* reverse a string

