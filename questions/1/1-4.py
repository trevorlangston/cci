# O(n) time
# O(n) space


def palindrome_permutation(string):
    string = string.lower().replace(' ', '')
    char = {}
    count_odd = 0

    for c in string:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1

    for v in char.values():
        if v % 2 != 0:
            count_odd += 1

    if count_odd >= 2:
        return False
    return True


print palindrome_permutation('Tact Coa')
print palindrome_permutation('Able was I ere I saw Elba')
print palindrome_permutation('Never odd or even')
print palindrome_permutation('not a palindrome')
