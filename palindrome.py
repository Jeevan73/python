#palindrome
text=input("enter text:")
palindrome=text[::-1]
if text==palindrome:
    print("it's palindrome")
else:
    print("it's not! palindrome")