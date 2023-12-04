# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

from collections import Counter
n = int(input())
i = input()

def fav_singer(s):
    lis = [int(i) for i in i.split()]
    max_play = max([v for k,v in Counter(lis).items()])
    final_lis = [k for k,v in Counter(lis).items() if v==max_play]
    return len(final_lis)

print(fav_singer(i))