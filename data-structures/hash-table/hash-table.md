A _hash table_ is a data structure that maps keys to values. It uses a hash
function to compute an index for a key corresponding to buckets. Hash tables
map an infinite set of keys to a finite space and so collisions are guaranteed
to occur. One method to deal with collisions is to use chaining where each
bucket contains a linked list. Another method is to use open addressing with
probing. In this method, the algorithm 'probes' for an empty bucket by stepping
through different hash functions until it finds one.

The load factor of a hash table is the ratio of buckets to keys. A hash table
uses table doubling to expand and contract to maintain an ideal load factor.
Hash tables have extremely fast lookups, inserts and deletes, and for this
reason are heavily used. There is no concept of ordering amongst items in a
hash table. E.g. it's not possible to find the next largest element, or no
concept of finding the previous element.

Complexity analysis:
Lookup O(1)
Insert O(1)
Delete O(1)

Motivation:
* caching
* tables
* sets
* objects
