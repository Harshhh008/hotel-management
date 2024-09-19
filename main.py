menu = {
    "pasta" : 80,
    "cofee" : 400,
    "dhosa" : 150,
    "pizza" : 1000
}
i = 1;
print("CHOOSE your menu:")
for key,value in menu.items():
    print(f"{i}.{key} : {value}")   
    i += 1

count_price = 0
item = input("choose ur item:")
if item in menu:
    count_price += menu[item]
    print(f"yout {item} added in order.")
    print(f"your order total : {count_price}")
else:
    print("this {item} not avalable yet.please choose menu item.")

while 1:   
    another_item = input("do you want another item(Yes/No):")
    if another_item.lower() == "yes":
        item1 = input("enter what you want: ")
        if item1 in menu:
            count_price += menu[item1]
            print(f"yout {item1} added in order:")
            print(f"your order total : {count_price}")
        else:
            print("this {item} not avalable yet.please choose menu item.")
            
    else:
        print("Thank you for order.")
        exit()
        
    
    
    
    