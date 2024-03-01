def is_palindrome_recursive(word, low_index, high_index):
    for _ in word:
        if low_index == len(word) - 1:
            return True
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
