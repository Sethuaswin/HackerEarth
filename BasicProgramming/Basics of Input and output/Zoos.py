# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

z = input()

if len(z) <= 20 and z.count('o') == 2* z.count('z'):
    print('Yes')
else:
    print('No')