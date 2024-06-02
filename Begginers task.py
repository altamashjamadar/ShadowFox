'''#1 Variables
pi = 22 / 7
print(type(pi))

<<<<<<< HEAD
#for = 4  #Invalid Syntax
=======
#for = 4  INvalid Syntax
>>>>>>> origin/main
P=int(input("enter principal amount"))
R=int(input("Enter Rate"))
T=2
simple_Interest=P*R*T/100
print(simple_Interest)
'''
#2Numbers
'''
def format_values(number,character):
    formatted_string=f"{number}{character}"
    return formatted_string

result=format_values(145,'o')
print(result)


radius=84
pi=3.14
area_of_pond=pi*radius*radius
print(area_of_pond)
water_per_squaremeter=1.4
total_water=area_of_pond*water_per_squaremeter
print(int(total_water))


distance=490
time=7*60
speed=distance/time
print(int(speed))



#3 Lists
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

number_of_members=len(justice_league)
print("Number of members :",number_of_members)

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing :",justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print("After making Wonder Woman the leader :",justice_league)

justice_league.remove("Green Lantern")
flash_index=justice_league.index("Flash")
justice_league.insert(flash_index,"Green Lantern")
print("After separating Aquaman and Flash :",justice_league)

justice_league=["Cyborg","Shazam","Hawkgirl","Marian Manhunter","Green Arrow"]
print("New team :",justice_league)

justice_league.sort()
print("Sorted Justice League :",justice_league)

new_leader=justice_league[0]
print("New Leader :",new_leader)
<<<<<<< HEAD


#4 if else

def calculate_bmi():


        height = float(input("Enter height in meters: "))
        weight = float(input("Enter weight in kilograms: "))


        bmi = weight / (height ** 2)


        if bmi >= 30:
            category = "Obesity"
        elif 25 <= bmi < 30:
            category = "Overweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        else:
            category = "Underweight"


        print(category)


calculate_bmi()


def find_country():

    city = input("Enter a city name: ")


    if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
        print(f"{city} is in Australia")
    elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
        print(f"{city} is in UAE")
    elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
        print(f"{city} is in India")
    else:
        print(f"{city} is not in the list of known cities")


find_country()

def find_country(city):

    if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
        return "Australia"
    elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
        return "UAE"
    elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
        return "India"
    else:
        return None

def check_same_country():

    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")


    country1 = find_country(city1)
    country2 = find_country(city2)



    if country1 == country2:
         print(f"Both cities are in {country1}")
    else:
         print("They don't belong to the same country")



check_same_country()


import random


num_rolls = 20
count_6 = 0
count_1 = 0
count_two_6_in_row = 0


previous_roll = None
for _ in range(num_rolls):
    roll = random.randint(1, 6)


    if roll == 6:
        count_6 += 1
    elif roll == 1:
        count_1 += 1


    if roll == 6 and previous_roll == 6:
        count_two_6_in_row += 1


    previous_roll = roll


print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times rolled two 6s in a row:", count_two_6_in_row)


def main():
    total_jacks = 100
    jacks_per_set = 10
    remaining_jacks = total_jacks

    for _ in range(total_jacks // jacks_per_set):
        print(f"You have {remaining_jacks} jumping jacks remaining.")
        tired = input("Are you tired? (yes/no): ").lower()
        if tired == "yes" or tired == "y":
            skip_remaining = input("Do you want to skip the remaining sets? (yes/no): ").lower()
            if skip_remaining == "yes" or skip_remaining == "y":
                print(f"You completed a total of {total_jacks - remaining_jacks} jumping jacks.")
                break
        remaining_jacks -= jacks_per_set
    else:
        print("Congratulations! You completed the workout.")

if __name__ == "__main__":
    main()
'''

