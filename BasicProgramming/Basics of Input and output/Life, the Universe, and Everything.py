# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
lis = []

while True:
    m = int(input())
    lis.append(m)
    if m == 42:
        break

for i in lis[:-1]:
    print(i)