# Program to find if the given string is a palindrome or not

def is_palindrome(s):
    """Return True if the given string is a palindrome"""
    return s == s[::-1]

if __name__ == "__main__":
    _string_ = input("Enter a string: ")
    if(is_palindrome(_string_)):
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")
        
