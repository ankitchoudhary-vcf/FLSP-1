list1 = [13,1,2,13,2,1,13]
sum =0
for index, item in enumerate(list1):
    if(item == 13):
            list1.remove(item)
    else:
        sum=sum +item
print(sum)