# this program is to help you known no of passengers  and types of vechiles 
# 1-2 = bike
# 3-4 = tricycle
# 5-6 = car
# 7-8 = keke
# 9-14 = Danfo



         
    
print("welcome") 
passengers = input("enter your no of passengers ")
passengers =int(passengers)
if 1 <=  passengers <=2:
    print("bike")
elif 3 <= passengers <= 4 :
    print("tricycle")
elif 5<=  passengers  <= 6 :
     print("car")
elif 7 <=  passengers <= 8 :
     print("keke")
elif 9 <=  passengers <= 14:
     print("danfo")


else :
     print("thank you")



