import qrcode

PRODUCTS = []
bill = []


def QR_code():
    user = input('enter name or code:')
    for product in PRODUCTS:
        if product['name']==user or product['code']==user:
            img = qrcode.make(product)
            img.save('qrcode.png')
            print('QRcode was created')
                
    
    
def read_from_database():
    f = open('d:\my-projects\pylearn\homework_7\database.txt','r')
    
    for line in f:
        
        result = line.split(',')
        my_dict = {'code':result[0],'name':result[1],'price':result[2],'count':result[3]}
        
        PRODUCTS.append(my_dict)
        print(my_dict)
        
    f.close()
    
def write_to_database(data):
    data=open("database.txt","w")
    data=open("database.txt","a")
    for product in PRODUCTS:
        line=str(product["code"])+","+product["name"]+","+str(product["price"])+","+str(product["count"])
        data.write(line.strip()+"\n")
    data.close()
       
def show_menu():
    print('1) add')
    print('2) edit')
    print('3) remove')
    print('4) search')
    print('5) show list')
    print('6) buy')
    print('7) QR_code')
    print('8) write_to_database')    
    print('9) exit')
    
def add():
    code = input('enter code: ')
    name = input('enter name: ')
    price = input('enter price: ')
    count = input('enter count: ')
    new_product = {'code':code,'name':name,'price':price,'count':count}
    PRODUCTS.append(new_product)
    
def edit():
    user = input('enter code or name for product:')
    for product in PRODUCTS:
        if product['name']== user or product['code']==user:
            print('1) name')
            print('2) price')
            print('3) count')
            print('4) exit')
            number = int(input('enter your num:'))

            if number==1:
                product['name']= input('enter name: ')
                print('Information updated successfully')
            if number==2:
                product['price']= float(input('enter price: '))
                print('Information updated successfully')
            if number==3:
                product['count'] = int(input('enter count: '))
                print('Information updated successfully')
            if number==4:
                break
            
            
def remove():
    user = input('enter name or code:')
    for product in PRODUCTS:
        if product['name']==user or product['code']==user:
            PRODUCTS.remove(product)
            print('The desired product has been successfully removed')
            break           

    
def search():
    user_input = input('type your keyword: ')
    for product in PRODUCTS:
        if product['code']== user_input or product['name']== user_input:
            print(product['code'],'\t\t',product['name'],'\t\t',product['price'])
            break
    else:
        print('not found')
    
def show_list():
    print('code\t\tname\t\tprice')
    for product in PRODUCTS:
        print(product['code'],'\t\t',product['name'],'\t\t',product['price'])

def buy():
    continue_s = True
    found = False
    factor_name = []
    factor_count = []
    
    while continue_s:
        r_code = input("Enter product code: ")
        r_count = int(input("Enter product count: "))

        for product in PRODUCTS:
            if product["code"] == r_code and int(product["count"]) >= r_count:
                factor_name.append(product["name"])
                index = PRODUCTS.index(product)
                
                PRODUCTS[index]["count"] = str(int(PRODUCTS[index]["count"]) - int(r_count))
                write_to_database(PRODUCTS)
                
                print('SOld!')
                found = True
                
        if not found:
            print("Product not found or isn't available")
            
        
        if input("Do you want to continue shopping?(y/n): ") == "y" :  
            if found:
                factor_count.append(r_count)
            
            found = False
        else :
            if found:
                factor_count.append(r_count)
                                
                print("\nYou bought these items:")
                for i in range(len(factor_name)):
                    print(f"--You bought Product {factor_name[i]} , {factor_count[i]} of this item")
              
            continue_s = False
    
    
print('welcme to store')
print('loading...')
read_from_database()
print('data loaded.')

while True:
    show_menu()
    choice = int(input('enter your choice: '))


    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        QR_code()
    elif choice == 8:
        write_to_database()
    elif choice== 9:
        exit(0)
    else:
        print('please write again ✅')

    for product in PRODUCTS:
        print(product)