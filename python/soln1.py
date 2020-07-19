import random as rd 

input_list=[]

for i in range (0,5):
    x=input("please enter a word: ")
    input_list.append(x)


choice=int(input("enter 1 to guess the first half \nenter 2 to guess the second half"))
             
random_value=rd.choice(input_list)

half=len(random_value)//2
if choice==1
    #water,half=2
    print("guess the word - \n")
    print("_"(half+1),random_value[half+1:])
     
           
