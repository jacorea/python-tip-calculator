#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
bill = input("what is your total bill: $")
tip = input("What percentage tip would you like to give? 10,12, or 15? ")
party_size = input("How many people to the split the bill? ")

# bill_adjusted = (bill + (bill*tip))/party_size 
bill_adjusted = (float(bill) + (float(bill) *(float(tip)/100)))/float(party_size)

# round bill to 2 decimal places 
bill_adjusted = round( bill_adjusted,2)
print(f"Each person should pay: ${bill_adjusted}")


