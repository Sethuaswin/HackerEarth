# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    count = 0
    for i in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j <= q:
                        if arr[i][j] > arr[p][q]:
                            count += 1
    print(count)
