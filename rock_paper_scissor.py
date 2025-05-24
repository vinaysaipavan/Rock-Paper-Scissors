import random

a="Tie"
b="Botwin"
c="You win"

data = {
    "options": ["rock", "paper", "scissor"]
}

win = {
    "do": ["Hug me!", "Kiss me!", "Love me!"]
}

def botopt(data):
    botoption=random.choice(data["options"])
    return botoption
def botwin():
    botfavour=random.choice(win["do"])
    return botfavour

def bot(data,option):
    botoption=botopt(data)
    if option == 1:
        option="rock"
    elif option==2:
        option="paper"
    else:
        option="scissor" 
    if botoption==option:
        display(botoption,a)   
    elif (botoption=="rock" and option=="scissor")  or (botoption=="paper" and option=="rock") or (botoption=="scissor" and option=="paper"):
        display(botoption,b)
    else:
        display(botoption,c)    
        
def display(botoption,win):
    if win=="Tie":
        print(f"Bot option:{botoption}")
        print("Game tie!")
    elif win=="Botwin":
        d=botwin()
        print(f"Bot option:{botoption}")
        print("Bot win!")
        print(f"Bot Favour:{d}")
        input("Enter your feeling:")
        print("Bot:Thank you so much! Love you")
    else:
        print(f"Bot option:{botoption}")   
        print("You win!") 
               

#Game starts
print("----Enter to Rock paper scissor game!----\n")
while(True):
    print("\n1.Start\n2.End")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("Rock! Paper! Scissor!")
        option=int(input("Enter option(1-3):"))
        if option in range(1,4):
            bot(data,option)
        else:
            print("Invalid option!")    
    elif choice==2:
        print("Game over! Bye 👋")
        break
    else:
        print("Invalid choice!\n")        