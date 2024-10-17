import random

#generate the number
num = random.randint(1, 100)

while True:
    #take input
    in_string_num= input("Guess the number from 1 to 100 : ")
    in_num=int(in_string_num)
    #if input equals to num , print you win
    if(in_num == num):
        print("Congratulations! You guessed the right number!")
        break
    #if input  minus num equals more than 10, it's far guess than num
    elif(in_num - num > 10):
        print("Sorry, you guessed too high!")
    #if input minus num equal  less than 10, it's more than num
    elif( in_num - num > 0):
        print("Sorry, you guessed high but close ! ")
    #if input minus num equal  more than -10, it's less than num
    elif(in_num - num >= -10):
        print("Sorry, you guessed less but close!")
    #if input minus num equal  less than -10, it's far less than guess
    elif(in_num - num <= -10):
        print("Sorry, you guessed too less than the number!")
    else:
        print("invalid input, try 1 to 100 .")


