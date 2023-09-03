ca_l=[];st_l=[];b=[];ex=[]
def AddCashier():
    C_Name=input("Enter a Cashier Name: ")
    C_Pwd=input("Enter Cashier Password: ")
    ca={'C_Name':C_Name,'C_Pwd':C_Pwd}
    ca_l.append(ca)
    print("Cashier Added Successfull...")
    print("Your Username: ",C_Name)
    print("Your Password: ",C_Pwd)
def ViewCashier():
    print(*ca_l)
def RemoveCashier():
    try:
        R_Cname=input("Enter a Remove Cashier Name: ")
        Cn_li = [e['C_Name'] for e in ca_l]
        i = Cn_li.index(R_Cname)
        ca_l[i]=""
    except:
        print("Invalid input!....")
def Owner():
    while True:
        try:
            n=int(input("1.AddCashier\n2.ViewCashier\n3.RemoveCashier\n4.Exit\n"))
            if n==4:
                break
            elif n==1:
                AddCashier()
            elif n==2:
                ViewCashier()
            elif n==3:
                RemoveCashier()
        except:
            print("Invalid input!....")
def Add_Stock():
    try:
        St_Name=input("Enter Stock Name: ")
        if St_Name not in ex:
            ex.append(St_Name)
            St_Count=int(input("Enter a Stock Count: "))
            St_SP=int(input("Enter a Stock Single Price: "))
            St_STax=int(input("Enter a stock Single Tax: "))
            s={'St_Name':St_Name,'St_Count':St_Count,'St_SP':St_SP,'St_STax':St_STax}
            st_l.append(s)
        else:
            Cn_li = [e['St_Name'] for e in st_l]
            i = Cn_li.index(St_Name)
            st_l[i]['St_Name']=St_Name
            St=int(input("Enter a Stock Count: "))
            st_l[i]['St_Count']+=St
            st_l[i]['St_SP']=int(input("Enter a Stock Single Price: "))
            st_l[i]['St_STax']=int(input("Enter a stock Single Tax: "))
    except:
        print("Invalid input!....")
def View_Stock():
    print(*st_l)
def Remove_Stock():
    try:
        R_Sname=input("Enter a Remove Stock Name: ")
        Cn_li = [e['St_Name'] for e in st_l]
        i = Cn_li.index(R_Sname)
        st_l[i]=""
    except:
        print("Invalid input!....")
def New_Bill():
    z=0
    while True:
        try:
            answer=input("if you want buy a things say (yes or no): ")
            if answer in 'yes':
                S_Name=input("Enter a Stock Name: ")
                count=int(input("Enter Count of Stock: "))
                Cn_li = [e['St_Name'] for e in st_l]
                i = Cn_li.index(S_Name)
                stock_Name=S_Name
                stock_Count=count
                st_l[i]['St_Count']-=count
                Stock_Price=count*st_l[i]['St_SP']
                Stock_Tax=(Stock_Price * st_l[i]['St_STax'])/100
                Stock_Total_Price=Stock_Price+Stock_Tax
                z+=Stock_Total_Price
                x={'stock_Name':S_Name,'stock_Count':stock_Count,'Stock_Price':Stock_Price,'Stock_Tax':Stock_Tax,'Stock_Total_Price':Stock_Total_Price}
                b.append(x)
            else:
                b.append({'Over_all_total':z})
                print("Thanks for Buying Items!...")
                break
        except:
            print("Invalid input!...")
def View_Bill():
    print(*b)
    #print("   stock_Name    stock_Count       Stock_Price         Stock_Tax            Stock_Total_Price       ")
    #print("----------------------------------------------------------------------------------------------------")
    #print(   b['stock_Name'],   b['stock_Count'],   b['Stock_Price'],   b['Stock_Tax'],    b['Stock_Total_Price'] )
def Cashier():
    C_Name=input("Enter Cashier Name: ")
    C_Pwd=input("Enter Cashier Pwd: ")
    Cn_li = [e['C_Name'] for e in ca_l]
    i = Cn_li.index(C_Name)
    if ca_l[i]['C_Name'] in C_Name and ca_l[i]['C_Pwd'] in C_Pwd:
        print("Log in Successfull...")
        while True:
            try:
                n=int(input("1.Add_Stock\n2.View_Stock\n3.Remove_Stock\n4.New_Bill\n5.View_Bill\n6.Exit\n"))
                if n==6:
                    break
                elif n==1:
                    Add_Stock()
                elif n==2:
                    View_Stock()
                elif n==3:
                    Remove_Stock()
                elif n==4:
                    New_Bill()
                elif n==5:
                    View_Bill()
            except:
                print("Invalid input!...")
    else:
        print("Invalid Log in...")
print("----Billing Module----")
while True:
   try:
       n=int(input("1.Owner\n2.Cashier\n3.Exit\n"))
       if n==3:
           print("Thanks for using...")
           break
       elif n==1:
           Owner()
       elif n==2:
           Cashier()
   except:
      print("\nINvalid input....\n")
    





