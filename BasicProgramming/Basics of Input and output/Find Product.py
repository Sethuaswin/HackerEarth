# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

n = int(input())
arr = [int(x) for x in input().split()]
ans = 1

for i in arr:
    ans = (ans * i) % (pow(10,9) + 7)

print(ans)
