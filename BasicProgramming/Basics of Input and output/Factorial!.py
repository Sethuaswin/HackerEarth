# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

n = int(input())

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fact(n-1) * n

print(fact(n))