def reverse(n):
    
    if n > 0:
        last = n%10
        if n//10 > 0:
            currentnumber = reverse((int)(n//10))
            return last*pow(10,len(str(currentnumber)))+ currentnumber
        return n
    
n = int(input("Enter a number : "))
print("Reversed number of the number is =", reverse(n))
    