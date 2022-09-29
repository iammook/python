# print("I am \\Ptyhon\\"+"\nGPA =","4.0")


# d = 123456.65
# print("%-8s%15d" % ("%15d",d))
# print("%-8s%15f" % ("%15f",d))
# print("%-8s%15.2f" % ("%15.2f",d))
# print("%-8s%-15d" % ("%-15d",d))
# print("%-8s%-15f" % ("%-15f",d))
# print("%-8s%-15.2f" % ("%-15.2f",d))


# mydata = ["mook","view","Idea"]
# print(mydata[0],mydata[1],mydata[2],end=" -> ",sep=":")
# print("SEE YOU LATER")


# x = "python"
# y = "Programming"
# a = 1070.999
# b = 6.97

# print("{}".format(x))
# print("{:s}".format(y))
# print("{} {}".format(x,y))
# # print("{0} {1}".format(x,y))
# print("{1:s} by {0:s}".format(x,y))
# print("{0:*>10s} {0:+^10s} {1:*^15}".format(x,y))
# print("{0:*>10,.1f} {1:*>10,.2f}".format(a,b))
# print("{0:>10,.1f} {1:*^10,.2f}".format(a,b))


# name = input("Enter your name >>> ")
# age = int(input("Enter your age >>> "))
# weight = float(input("Enter your weight >>> "))
# print("\nName:",name,"\nAge:",age,"years","\nWeight:",weight,"KG")


# sc1, sc2 = input("Enter your score:").split()
# avg = (int(sc1) + int(sc2))/2
# print("Score avarage is: {:.2f}".format(avg))


# cal = input("Calculate score please enter number 1 >>> ")
# if cal == "1":
#     score = float(input("Enter your score: "))
#     cal_score = (float(score)/35)*100
#     print("score = {:.1f} score \nis {:.1f} %".format(score,cal_score))
# print("see you later")


# ****count 1 to (number)
# number = int(input("Enter your number -> "))
# run = 1
# count = 0
# while run <= number:
#     count = count + run
#     run += 1
# print("Total from 1 to {} = {}".format(number,count))

# ****Mini Random Game 
# import random

# guess = random.randint(0,9)
# count = 1
# while True:
#     rannum = int(input("Enter number you want to guess: "))
#     if rannum == guess:
#         print("!!!!That's right!!!")
#         print("random number is",guess)
#         break
#     else:
#         count += 1
#         if count < 4:
#             print("try a gain")
#         else:
#             print("You wong more than 3 times")
#             print("random number is",guess)
#             break


# ****find avg score of all students
# student = int(input("Total student: "))
# total = 0
# for i in range(1,student+1):
#     score = int(input("Socre of student number {} >>> ".format(i)))
#     total += score
# avg = float(total/student)
# print("Avarage score =",avg)


# ****Check password
# password = ["1234","1111"]
# pw = input("Your pasword => ")
# for data in password:
#     if data != pw:
#         pass
#     else:
#         print("found this password")
# print("See you later")


# *****enter sub-password
# password = "87654321"
# # password = input("Enter password ")
# checkpw = password[0:len(password):2]
# while True:
#     pwin = input("Enter the password again")
#     if pwin == checkpw:
#         print("Login success")
#         break
#     else:
#         print("It's incorrect, Try again") 



# ***count string
# text = input("Enter size of number you want to count: ")
# print("Len of number is {}".format(len(text)))


# ***Decode password
# pw = input("Enter your password: ")
# encode = pw[0::2]
# print("Encode password is:",encode)


# *** Check pass test and score test 
# student_dic = {1:17,2:19,5:18,7:17,8:17,10:19}
# get_number = int(input("Enter toue number: "))
# for i in student_dic.keys():
#     if i == get_number:
#         print("Congrat you pass the test. you're score =",student_dic.get(i))
#         break
# else: 
#     print("Sorry you arn't pass the test")


import datetime 
from datetime import date,datetime
from datetime import *

checkday = (2019,7,25)
dayno = checkday.weekday()

day = {0:'Mon',1:"Thu",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
print(dayno)
print(checkday.strftime("%a"))