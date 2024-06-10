# write a script to handle user' s age and print their category
# 0 - 4  =infant
# 5 - 12 =kids
# 13 -20 =teenagers
# 21 -29 =younger adult
# 30 _69 =adult
# 70 _100 =old man

print("welcome") 
age = input("kindly enter your age ")
age =int(age)
if 0 <= age <=4:
    print("infant")
elif 5 <= age <= 12 :
    print("kids")
elif 13 <= age <= 20 :
     print("teenagers")
elif 21 <= age <= 29 :
     print("younger adult")
elif 30 <= age <= 69 :
     print("aduit")
elif 70 <= age <= 100 :
     print ("old man")
else :
     print("thank you")
     