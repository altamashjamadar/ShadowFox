'''#1 Variables
pi = 22 / 7
print(type(pi))

#for = 4  INvalid Syntax
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
'''

#4 if else
