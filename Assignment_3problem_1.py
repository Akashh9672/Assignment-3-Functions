def summation(number_list):
    sum=0
    for i in number_list:
        sum = i + sum
    print("Summation of total no. is:", sum)
size=int(input("Enter size of list:"))
number_list=[]
for i in range(size):
    number=int(input("Enter the number:"))
    number_list.append(number)
print("Your list:", number_list)
summation(number_list)    
