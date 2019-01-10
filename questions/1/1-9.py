# Time O(n)
# Space O(1)


# WRONG
def is_rotation(a, b):
    i = 0

    while a[0] != b[i]:
        if i == len(b) - 1:
            break
        i += 1

    if a[0] != b[i]:
        return False

    return a == b[i:] + b[:i]


print is_rotation('waterbottle', 'erbottlerat')
print is_rotation('waterbottle', 'erbottlewat')
