def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
word1=(input("Enter a word to check whether it's palindrome or not-")).lower()
result=palindrome(word1)
print(result)