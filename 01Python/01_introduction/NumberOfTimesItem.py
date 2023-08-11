myList = [1,4,6,7,4]

number = int(input("please enter the item: "))

check = myList.count(number) 
if check:
    print(f"the item {number} is repeated {check} times")
    
else:
    print("ite,m not found")    