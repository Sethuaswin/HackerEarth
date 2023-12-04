# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

l = int(input())
n = int(input())

for i in range(n):
    lis = input().split()
    w = int(lis[0])
    h = int(lis[1])

    if l > w or l > h:
        print("UPLOAD ANOTHER")
    elif w == h and l <= w and l <= h:
        print("ACCEPTED")
    else:
        print("CROP IT")