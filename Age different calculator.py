from datetime import date
date_of_birth=int(input("Enter the year of you birth:"))
today_date=date.today().strftime("%Y")
print("Your current age is: ",int(today_date)-date_of_birth)
