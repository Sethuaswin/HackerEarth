# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

t = int(input())

while t !=0:
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    index = n - (k % n)
    for i in range(index, n):
        print(arr[i], end=" ")
    for i in range(index):
        print(arr[i], end=" ")
    print("")

    t -= 1
