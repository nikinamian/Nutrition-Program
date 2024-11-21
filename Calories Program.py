#Calories Program

print("Welcome to the Calorie Counting Program. Let's analyze your eating habits")

Foods = []
Calories = []
food = input("Enter a food or enter XXX to move on: ").strip()
#calorie = int(input("Based on the serving size you ate, please enter the number of calories: "))

while food.upper() != "XXX":
    Foods.append(food)
    #food = input("Enter a food or enter XXX to move on: ").strip()
    calorie = int(input("Based on the serving size you ate, please enter the number of calories: "))
    if calorie<0:
        print("invalid input")
        calorie = int(input("Based on the serving size you ate, please enter the number of calories: "))
    food = input("Enter a food or enter XXX to move on: ").strip()




print ("The highest calorie food you ate was",max(Foods))




