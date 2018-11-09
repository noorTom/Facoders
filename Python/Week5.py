h = input ('Enter student\'s name: ')
s1 = ['Ahmad',18,17,19.5,8,25]
s2 = ['Sami',20,20,19,9,28]
s3 = ['Faris',14.5,16,13,7,23]
mark = [s1,s2,s3]
for s in mark :
        i = s[0]
        x = s[1:]
        y = sum(x)
        if h==i :
            print (i,y)
            break
else :
        print ('Student is not recorded o ')
