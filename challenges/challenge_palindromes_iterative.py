def is_palindrome_iterative(word):
    reverse_word = word[::-1]
    if word != reverse_word or not word:
        return False
    return True
