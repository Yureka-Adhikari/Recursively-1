def reverse(s):
    if len(s) == 1:
        return s[0]
    
    firstchar= s[0]
    
    return reverse(s[1:]) + firstchar

s = input("Enter a string : ")
print(f"Reversed string is = {reverse(s)}")