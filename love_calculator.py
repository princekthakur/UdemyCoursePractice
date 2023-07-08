#checking length of the names and as per them showing them the message
#as per the length the message we need to show

def lov_cal(name1,name2):
    name4=int(len(name1))
    name3=int(len(name2))
    total=name3+name4

    if(total>=10 or total<=85):
        print(f"Your score is {total} and you like coke & pepsi.")
    elif(total>=40 and total<=70 ):
        print(f"You score is {total} and you are good to together.")
    else:
        print(f"Your Score is {total} nothing to say")


print("Welcome to Love Calculator !")
name1=input("Please Enter Your Names:")
name2=input("Please Enter him/her name:")
lov_cal(name1,name2)