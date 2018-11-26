A _queue_ is another ADT similar to a stack, which supports operations that add
items to the end of the queue (enqueue) and removes items from the front of the
queue (dequeue). A queue follows the first in first out (FIFO) order, like a
line of people waiting at Disneyland. Queues are typically implemented as
either a circular buffer or a linked list.

Complexity analysis:
Enqueue O(1)
Dequeue O(1)

Motivation:
* any time first come first serve is needed
* prioritize processes in an OS
* sending documents to a printer
* scheduling any kind of in order processing
