quote = input()
l = quote[2]
f_set = (int(quote[0]) + int(quote[1])) % 2
s_set = (int(quote[3]) + int(quote[4])) % 2
t_set = (int(quote[4]) + int(quote[5])) % 2
fo_set = (int(quote[7]) + int(quote[8])) % 2
if (l in "AEIOUY"):
    print('invalid')
elif (f_set == 0) and (s_set== 0) and (t_set== 0) and (fo_set ==0):
    print('valid')
else:
    print('invalid')