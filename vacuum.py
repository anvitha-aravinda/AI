choice=int(input("vacuum world,1 for model based, 2 for simple reflex based"))
print("room A and B")
print("dirty 1, clean 0")
pos=input("enter the position of vacuum cleaner")
cost=0

if choice==1:
    astatus=int(input("enter status of room A"))
    bstatus=int(input("enter status of room B"))
    status={"A":astatus,"B":bstatus}
    switchoff="n"
    while(switchoff=="n"):
        if status[pos]==1:
            print(pos +" dirty")
            print("suck")
            status[pos]=0
            cost+=1
            print("cost="+str(cost))
        
        if status["A"]==0 and status["B"]==0:
            print("both rooms cleaned")
            switchoff="y"
        else:
            if pos=="A":
                print("Move right")
                pos="B"
            else:
                print("Move left")
                pos="A"
            cost+=1
            print("cost="+str(cost))
            
elif choice==2:
    switchoff="n"
    while(switchoff=="n"):
        status=int(input("enter status of room "+pos))
        if status==1:
            print(pos +" dirty")
            print("suck")
            cost+=1
            print("cost="+str(cost))
        if pos=="A":
            print("Move right")
            pos="B"
        else:
            print("Move left")
            pos="A"
        cost+=1
        print("cost="+str(cost))
        switchoff=input("Do you want to switch off the vacuum? y/n")
print("performance measure cost ="+str(cost))