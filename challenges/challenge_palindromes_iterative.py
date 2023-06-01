def is_palindrome_iterative(word=None):
    return (
        False if word is None or len(word) < 1 else word == "".join(word[::-1])
    )
