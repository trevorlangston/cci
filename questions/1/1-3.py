# O(n) time
# O(1) space


def urlify(string):
    out = ''
    for i in range(len(string)):
        if string[i] == ' ':
            out += '%20'
        else:
            out += string[i]

    return out


print urlify('here and now')
print urlify('allthingsconsidered')
