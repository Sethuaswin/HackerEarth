# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
mi = min(a)
i = 0
count = 0

while i < n:
    if a[i] >= b[i]:
        while a[i] > mi:
            a[i] -= b[i]
            count += 1
        
    if a[i] < mi:
        mi = a[i]
        i = 0
    if a[i] != mi:
        count = -1
        break
    i += 1

print(count)