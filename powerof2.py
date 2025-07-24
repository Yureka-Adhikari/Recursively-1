n = int(input("Enter a number : "))

def checkIfPower(n):
    
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return checkIfPower(n/2)
    
if checkIfPower(n):
    print(f"{n} is a power of 2")
    
else:
    print(f"{n} is not a power of 2")