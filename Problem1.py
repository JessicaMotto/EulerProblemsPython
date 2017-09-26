i = 0
j = 0
for i in range (1,1000) :
    if i % 3 == 0 and i % 5 == 0 :
        print(i)
        j += i
    else :
        if i % 3 == 0 :
            print(i)
            j += i
        if i % 5 == 0 :
            print(i)
            j += i
print (j)