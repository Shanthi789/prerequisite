def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    #print (True) if num % divisor == 0 else print (False)
    a = True if num % divisor == 0 else False
    print(a)
    return a



# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
resVal1=check_divisibility(10,2)
resVal2=check_divisibility(-7,3)