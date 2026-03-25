

to_do_list = []

while True:
    
    cmd = input("What do you wanna do? : View / Add / Quit").lower()

    if cmd=="add":
        item = input("Sure! What do you wanna add?")
        to_do_list.append(item)
        print("Item added successfully!!")
    elif cmd=="view":
        if len(to_do_list)==0:
            print("Sorry! Your to do list is empty..")
        else:
            for i in to_do_list:
                print(i)
    elif cmd=="quit":
        print("Exiting..")
        break
    else :
        print("Choose from the provided options only!")
