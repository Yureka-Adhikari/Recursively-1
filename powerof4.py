n = int(input("Enter a number : "))

def checkIfPower(n):
    
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return checkIfPower(n/4)
    
if checkIfPower(n):
    print(f"{n} is a power of 4")
    
else:
    print(f"{n} is not a power of 4")