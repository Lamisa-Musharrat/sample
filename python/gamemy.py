import random 
word_list=[]
for i in range (0,5):
    user_input=input("Enter a word: ")
    word_list.append(user_input)
    
user_choice=int(input("Enter 1 to guess first half.\nEnter 2 to guess second half."))
random_choice=random.choice(word_list)
half=len(random_choice)//2

if user_choice==1:

    if (len(random_choice)%2 !=0):
        print("_" *(half+1),random_choice[half+1:])
    else :
        print("_" *half,random_choice[half:])
              
elif user_choice==2:

    if (len(random_choice)%2 !=0):
        print(random_choice[:half+1],(half+1)* "_")
    else:
        print(random_choice[:half],half* "_")
else:
    print("Invalid input: ")
    
user_guess=input("Enter your guess: ")
if (user_guess==random_choice):
    print("correct!")
    
else:
    print("wrong")
    