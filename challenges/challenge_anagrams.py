def partition(str, start, end):
    delimiter = start - 1

    for index in range(start, end):
        if str[index] <= str[end]:
            delimiter = delimiter + 1
            str[index], str[delimiter] = (
                str[delimiter],
                str[index],
            )

    str[delimiter + 1], str[end] = str[end], str[delimiter + 1]

    return delimiter + 1


def quick_sort(str, start, end):
    if start < end:
        part = partition(str, start, end)
        quick_sort(str, start, part - 1)
        quick_sort(str, part + 1, end)


def is_anagram(first_string, second_string):
    str_first_sorted = list(first_string.lower())
    str_second_sorted = list(second_string.lower())
    quick_sort(str_first_sorted, 0, len(str_first_sorted) - 1)
    quick_sort(str_second_sorted, 0, len(str_second_sorted) - 1)

    return str_first_sorted == str_second_sorted
