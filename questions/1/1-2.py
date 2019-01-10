# O(n) time
# O(n) space


def is_permutation(str_a, str_b):
    if len(str_a) != len(str_b):
        return False

    if len(str_a) < 2:
        return True

    char_map = {}
    for c in str_a:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1

    is_perm = True
    for c in str_b:
        if c not in char_map:
            is_perm = False
            break
        elif char_map[c] == 0:
            is_perm = False
            break
        else:
            char_map[c] -= 1

    if sum(char_map.values()) != 0:
        is_perm = False

    return is_perm


print is_permutation('abc', 'bca') is True
print is_permutation('abc', 'ABC') is False
print is_permutation('abc', 'bcab') is False
print is_permutation('abcb', 'bcd') is False
print is_permutation('a', 'a') is True
print is_permutation('dddd', 'ddddd') is False
print is_permutation('ddddddd', 'dddd') is False
