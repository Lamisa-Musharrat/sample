li=[]
i=1
while i<=5:
    user_input=input("Enter 5 words: ")
    li.append(user_input)
    guess=int(input("Enter 1 if you want to guess the first half. \nEnter 2 if you want to guess the last half.\n"))
    if guess==1:
        y=input("Enter your guess : ")
        if y==random.choice(li):
            print("Congrats!You have won!")
    else: 
        print("Sorry!You LOST!")

else:
    z=input("Enter your guess : ")
    if z==random.choice(li):
        print("Congrats!You have won!")
    else: 
        print("Sorry!You LOST!") 
i=i+1                  