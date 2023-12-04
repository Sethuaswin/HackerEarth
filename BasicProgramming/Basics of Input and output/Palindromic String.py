# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

s = input().lower()

if s == s[::-1]:
    print("YES")
else:
    print("NO")