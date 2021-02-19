import random
player_name=input("Please enter your name")

rnum=random.randint(1,10);
count=0
flag=0
score=0
while count<3:
    gnum=int(input("Hello! "+ player_name+ " Please enter the number you guessed between 1 to 10\n"))
    
    print(rnum)
    if rnum==gnum:
        count=count+1;
        flag=1;   
        if count==1:
            print("Congratulations! " + player_name+ " You guessed it in " +str(count)+" chance")
        else:
            print("Congratulations! " + player_name+ " You guessed it in " +str(count)+" chances")
        break;
    elif gnum<rnum:
        count=count+1;
        print("Your guess is too low")
        if rnum%gnum==0:
            print("Hint!,Random number is divisible by the number you entered.")
        elif rnum%2==0:
             print("Hint!, Random number is a even number")
        else: 
            print("Hint!, Random number is a odd number")
    elif gnum>rnum:
        count=count+1;
        print("Your guess is too high")
        if gnum%rnum==0:
            print("Hint!,Random number is divisible by the number you entered.")
        elif rnum%2==0:
             print("Hint!, Random number is a even number")
        else: 
            print("Hint!, Random number is a odd number")
if count==1:
    score=score+30;
elif count==2:
    score=score+20;
elif count==3 and flag==1:
    score=score+10;
else:
    score=0
print("Your score is "+str(score))
    