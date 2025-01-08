num=input("enter number")
res=""
for i in num:
    if(i=='0'):
        res+='1'
    elif(i=='1'):
        res+='0'
    else:
        res+=i
print("after replaced"+res)
