def calc(file):
    a=[]
    for z in file:  #This loop is used to calculate the value for each line
        temp=""
        sum=0
        for i in z[1:4]:  #Calculating the first digit
            if(i=='r'):
                sum+=4
            elif(i=='w'):
                sum+=2
            elif(i in ['x','s']):
                sum+=1
        temp+=str(sum)
        sum=0
        for i in z[4:7]:   #Calculating the second digit
            if(i=='r'):
                sum+=4
            elif(i=='w'):
                sum+=2
            elif(i in ['x','s']):
                sum+=1
        temp+=str(sum)
        sum=0
        for i in z[7:10]:  #Calculating the third digit
            if(i=='r'):
                sum+=4
            elif(i=='w'):
                sum+=2
            elif(i in ['x','s']):
                sum+=1
        temp+=str(sum)
        a.append(temp)  
    return a    #Returns the list of values
a = list(open("file_name.txt"))  #Opening and converting the txt file into list
b=a
c=0
a = calc(a)  
for i in a:
    print(i,end=" ")     #Printing the output
    print(b[c],end="")
    c+=1
