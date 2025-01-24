def check_palindrome(words):
    """The function checks if the given words are palindrome."""
    try:
        words = words.lower()
        if " " in words:
            words = words.replace(" ", "") #deliting spaces
        if words == words[::-1]:
            return True
        else:
            return False
    except TypeError:
        return False
    except AttributeError:
        return False


print(check_palindrome("kajak"))
print(check_palindrome("Kobyła ma mały bok"))
print(check_palindrome("kamila"))
print(check_palindrome(""))
print(check_palindrome(0))
