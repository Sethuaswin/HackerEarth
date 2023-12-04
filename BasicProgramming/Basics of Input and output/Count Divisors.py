# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

s = input().split()

l = int(s[0])
r = int(s[1])
k = int(s[2])

if l-r == 0:
    print(0)
else:
    out = len([i for i in range(l,r+1,k)])
    print(out)