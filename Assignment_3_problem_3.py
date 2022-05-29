def character(string):
    count_1=0
    count_2=0
    list=[]
    for i in string:
        char=ord(i)
        list.append(char)

    for i in list:
        if i <= 90 and i >= 65:
            count_1 +=1
            
        if i <= 123 and i >= 97:
            count_2 += 1
    print("NO. of Upper case character:",count_1)
    print("NO. of Lower case character:",count_2)
    


string=input("Enter your statement:")

character(string)