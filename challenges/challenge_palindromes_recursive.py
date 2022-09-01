def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    while low_index <= high_index:
        if word[high_index] == word[low_index]:
            high_index -= 1
            low_index += 1
            is_palindrome_recursive(word, low_index, high_index)
        else:
            return False
    return True
