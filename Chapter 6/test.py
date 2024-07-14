# age = int(input("Enter your age \n"))
# if age >= 18 and age <= 100:
#     print("You can drive ")
# elif age > 100:
#     print("Enter valid age")
# else:
#     print("You cannnot drive ")
def day_of_week(day_no):
    if(day_no==1):
        return "Monday"
    elif(day_no ==2):
        return "Tuesday"
    elif(day_no ==3):
        return "Wednesday"
    elif(day_no ==4):
        return "Thursday"
    elif(day_no ==5):
        return "Friday"
    elif(day_no ==6):
        return "Saturday"
    elif(day_no ==7):
        return "Sunday"
    else:
        return "Invalid date"
    
day_no = int(input("Enter day no. \n"))
print(day_of_week(day_no))