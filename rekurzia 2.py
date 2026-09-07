def abeceda ():
    for i in range(97, 123):
        for y in range(97, 123):
            for o in range(97, 123):  
                print(chr(i) + chr(y) + chr(o))   # alebo print(chr(i), end='')
#
#
#
output = []
#
#
#
def prep(n):
    global output
    output = ['-'] * n
    print(output)
#
#
#
def abeceda_2 (num:int):
    prep(num)
    schr(num)
#
#
#
def schr (n):
    global output
    if n == -1:
        print(''.join(output))
    else:
        for i in range (97, 123):
            output[n-1] = chr(i)
            schr(n-1)
#abeceda()
abeceda_2(4)