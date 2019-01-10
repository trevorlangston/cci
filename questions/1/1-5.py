# O(n) time
# O(n) space


def one_away(str_a, str_b):
    if abs(len(str_a) - len(str_b) > 1):
        return False

    # ensure str_a is always the shorter
    if len(str_a) > len(str_b):
        temp = str_a
        str_a = str_b
        str_b = temp

    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            if safe_get_tail(str_a, i+1) == safe_get_tail(str_b, i+1):
                return True
            elif str_a[i:] == safe_get_tail(str_b, i+1):
                return True
            else:
                return False

    return True


def safe_get_tail(str, idx):
    if idx > len(str) - 1:
        return ""
    return str[idx:]


print one_away('pale', 'ple') is True
print one_away('pales', 'pale') is True
print one_away('ddd', 'dddd') is True
print one_away('pale', 'bale') is True
print one_away('pale', 'bake') is False
print one_away('pale', 'pax') is False
print one_away('ddddd', 'dd') is False
