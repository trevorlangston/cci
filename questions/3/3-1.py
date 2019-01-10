"""
To implement 3 stacks using an array we must accept that we will run of out
space at some point because of course arrays are fixed in size. A simple
implementation would be to simply divide the array in thirds, and allot one
third to each stack, with a pointer for each to keep track of the head. This is
not ideal however because stacks may have different space requirements.

Idea 1: Push and pop items for each stack starting at the beginning of the
array. When an item is pushed, store two extra fields: the stack it belongs to
and the index of the previous item. This is bad because we are increasing our
space usage. Also this is wrong because once an index is used by a given stack,
it can only ever be used by that stack.

Idea 2: One stack starts from the front growing towards the end, another starts
at the end and grows to the front, and the third starts in the middle and
alternates between growing towards either side. This does not require extra
space to implement, though creates unique and potentially confusing logic for
each stack. Also there may be wasted space between stacks.
"""
