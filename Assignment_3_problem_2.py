def reverse_string(string):
    string2 = ""
    for i in string:
            string2 = i + string2
    print("Reverse string is:", string2)


string= input("Enter your string:")
reverse_string(string)