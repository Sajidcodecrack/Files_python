word="xlearning"
with open("practice2.txt","r")as f:
    d=f.read()
    new_data=d.replace("python","java")
    print(new_data)
    
with open("practice2.txt","w")as f:
    f.write(new_data)
def checkword():
    with open("practice2.txt","r")as f:
     data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not found ")

checkword()

def checkline():
    word="java"
    data= True
    lineno=1
    
    with open("practice2.txt","r")as f:
        while data:
            data=f.readline()
            if(word in data):
                print(lineno)
                return
                lineno+=1
            return-1

print(checkline())