my_list = [1,2,3,4,5]
user_input= int(input("Pls enter the number"))

#1st way
for num in my_list: 
    if (num == user_input):
        print (f"{user_input} is found in my_list")


#2nd way
if (user_input in my_list):
    print (f"{user_input} is found in the list")