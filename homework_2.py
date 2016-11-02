
str = '((((((((((((((2, 3)))))))))))))'

count1 = str.count ('(')
count2 = str.count (')')
dif=count1 - count2
if count1 > count2 :
    str= str[dif:]
    print (str)
elif count1 < count2:
    str = str[:dif]
    print (str)
else:
    print (str)
