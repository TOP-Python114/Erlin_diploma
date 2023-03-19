lst = [0,1,2,3,4,5,6,7,8,9,10,11]

a=[(lst[x],lst[x+1]) for x in range(0,len(lst),2)]

print(a)



