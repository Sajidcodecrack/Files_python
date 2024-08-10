c=0
with open("practice2.txt","r")as f:
    data=f.read()
    print(data)
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            if(int(num)%2==0):
                c+=1
            num=""
        else:
            num+=data[i]
print("Even numbers :",c)