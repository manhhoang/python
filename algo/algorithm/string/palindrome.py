def palindrome(s: str):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


print(palindrome("abba"))
print(palindrome("abbaa"))


