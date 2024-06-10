# write a script to evalute student performance  based on there grades
# 0-39 -fail
# 40-44 -poor
# 45-49-credit
# 50-59-good
# 60-69-verygood
# 70-100-excellent

print("welcome")
grades=input("kindly enter your grades")
grades=int(grades)
if 0 <= grades <=39 :
  print("fail")
elif 40 <= grades <=44:
   print("poor")
elif 45 <= grades <=49:
   print("credit")
elif 50 <= grades <=59:
   print("good")
elif 60 <= grades <=69:
   print("verygood")
elif 70 <= grades <=100:
   print("excellent")
else :
   print("thank you")
  
