def palindrome_number():
    _range = range(100, 1000)
    palindrome = 0
    for i in _range:
        for j in _range:
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                if prod > palindrome:
                    palindrome = prod
    return palindrome

print(palindrome_number())