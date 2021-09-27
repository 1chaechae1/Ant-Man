i = 3
sum = 1
for i in range(1, 99):
    if(i % 2 == 1):
        sum += i
    else:
        i += i
    
print("14번 - 1+3+5+..+95+97+99의 합은: %d" % sum)
       
