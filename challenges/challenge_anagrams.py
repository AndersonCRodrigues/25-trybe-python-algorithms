def quick_sort(string):
    if len(string) <= 1:
        return string
    pivot = string[0]
    smaller = [char for char in string if char < pivot]
    equal = [char for char in string if char == pivot]
    larger = [char for char in string if char > pivot]
    return (
        quick_sort("".join(smaller))
        + "".join(equal)
        + quick_sort("".join(larger))
    )


def is_anagram(first_string, second_string):
    str1 = quick_sort(first_string.lower())
    str2 = quick_sort(second_string.lower())
    if len(str1) < 1 or len(str2) < 1:
        return (str1, str2, False)
    return (str1, str2, str1 == str2)
