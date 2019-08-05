def is_palindrome(str, length):
    is_pali = True
    length -= 1
    for i in range (0, length//2):
        if (str[i] != str[length - i]):
            is_pali = False
            break
    return is_pali

str = input('please enter a string\n')
message = "Palindrome!" if is_palindrome(str, len(str)) else "not pali"
print (message)