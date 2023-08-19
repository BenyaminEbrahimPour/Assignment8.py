products = []
buy_basket=[]
def read_data():
    f = open("text.txt","r")
    for l in f:
        dic ={}
        product = l.split(",")
        dic = {"id":product[0],"name":product[1],"price":product[2],"count":product[3]}
        products.append(dic)
def show_menu():
    print("1 - add")
    print("2 - delete")
    print("3 - search")
    print("4 - buy")
    print("5 - edit")
    print("6- exit")
    print("7 - show products")
def add():
    id = input("Enter id:")
    name = input("Enten name: ")
    price = input("Enter price: ")
    count = input("Enter count: ")
    dic = {"id":id,"name":name,"price":price,"count":count}
    products.append(dic)
    print(products)
def delete():
    id=int(input("Enter id"))
    products.pop(id-1)
    print(products)
    print("The informations were updated")
def search():
    key = input("Enter your key: ")
    for product in products:
        if key==product["id"]or key==product["name"]:
            print(product)
            break
    else:                         
            print("Not found")
    
def buy():
    i=0;sum=0
    while True:
        
        space = input("if you want to carry on your buying or start your buying,press space keyboard :")
        if space==" ":
            id=int(input("Enter id:"))
            buy_basket.append(products[id-1])
            if products[id-1]["count"]==0:
                print("There is no good !!! ")
            else:
                count=int(input("Enter the count:"))
                x=products[id-1]["count"]
                z=products[id-1]["price"]
                z=int(z)
                x=int(x)
                if count <= x:
                    x=x-count
                    products[id-1]["count"]=x
                    buy_basket[i]["count"]=count
                    total_price=count*z
                    buy_basket[i]["Total price"]=total_price
                    i=i+1
                else:
                    print("stocks can not provide which you want !!!")
        else:
            print("id \t name \t price \t count \t total price")
            for i in buy_basket:
                print(i["id"] , "\t" , i["name"]  , i["price"], "\t", i["count"],"\t",i["Total price"])
                sum=sum+i["Total price"]
            print(buy_basket)
            print("*************")
            print("Total price of buying :",sum)
            break    
def edit():
    id=int(input("Enter id"))
    print("1-name")
    print("2-price")
    print("3-count")
    choice2=int(input("Enter yor choice"))
    if choice2==1:
        name=str(input("Enter new name:"))
        products[id-1]["name"]=name
        print("The informations were updated")
        print(products)
    elif choice2==2:
        price=int(input("Enter new price:"))
        products[id-1]["price"]=price
        print("The informations were updated")
        print(products)
    else:
        count=int(input("Enter new count:"))
        products[id-1]["count"]=count
        print("The informations were updated")
        print(products)
def exit():
    pass
def show_products():
    print("id \t name \t price \t count")                 
    for product in products:
        print(product["id"],"\t",product["name"],product["price"],"\t",product["count"])
        
read_data() 
show_menu()
user_choice = int(input("Enter your choice: "))
if user_choice ==1:
    add()
elif user_choice ==2:
    delete()
elif user_choice == 3:
    search()
elif user_choice==4:
    buy()
elif user_choice==5:
    edit()
elif user_choice ==6:
    exit()
    pass
elif user_choice ==7:
    show_products()
d = open("text 3.txt","a")
for u in products:
    count=str(u["count"])

    d.write(u["id"])
    d.write("/")
    name = str(u["name"])
    d.write(u["name"])
    d.write("/")
    price = str(u["price"])
    d.write(price)
    d.write("/")
    d.write(count)
    d.write("\n")



