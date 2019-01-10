# Time O(n)
# Space O(n)


def compress(string):
    compressed = ''
    has_repeats = False

    i = 0
    while i < len(string):
        repeats = 1
        j = i
        while j < len(string) - 1 and string[j] == string[j+1]:
            has_repeats = True
            repeats += 1
            j += 1
        compressed += string[i] + str(repeats)
        i = j + 1

    if has_repeats is False:
        return string

    return compressed


print compress('abcabc')
print compress('aabbbcccc')
print compress('aabcccccaaa')
print compress('abcdefg')
