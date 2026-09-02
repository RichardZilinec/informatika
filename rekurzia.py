# Rekurzia, musi tam byt IF, 
def fak(num:int)->int:
    output = 1
    for i in range (2, num+1):
        output *= i
    return output
#
#
#
def fak_2(num:int)->int:
    if num == 1:
        return 1
    else:
        return num*fak_2(num-1)
#
#
#
def fib(pos):
    if pos < 3:
        return 1
    else:
        return fib(pos-1) + fib(pos - 2)
print(fak(5))
print(fak_2(5))
print(fib(10))