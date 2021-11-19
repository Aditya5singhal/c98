#f=open("file2.txt")

#f2=f.readline()

#print(f2)

#introString="my , name , is , aditya"
#world=introString.split(",")


#print(world)

def wordcount():
    filename=input("what is your file name")
    f=open(filename,'r')
    count=0
    for i in f:
        word=i.split()
        print(f) 
        count=count+len(word)
    print(count)
    print(i)


wordcount()







