# O(n) time
# O(n) space
# how to do this without hash table?


def is_unique(string):
    if len(string) < 2:
        return True

    seen = {}
    for c in string:
        if c in seen:
            return False
        else:
            seen[c] = None
    return True


print is_unique('abc') is True
print is_unique('abca') is False
print is_unique('') is True
print is_unique('a') is True
print is_unique('aaaaaaaa') is False
