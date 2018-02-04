#Version 1.1 Game name "Gate of Isthar" magical door to different world.
#Created by Shikha Kumari
#Company Segula Technologies, Gothenburg Sweden 
from datetime import datetime

#for checking champion category
def invincible_champion(champion):
    if champion == 'Wizard' or champion ==  'Spirit':
        print ("\tChampion is Invinicble: No Health damage")
        return True
    if champion == 'Human' or champion == 'Giant' or champion == 'Vampire':
        print ("\tChampion is not Invinicble:Health loss while passing gates!! ")
        return False

#for checking holydays tues & thurs 
def holly_day(day):
    if (day == 'Tuesday' or day == 'Thursday'):
        print "\n\t!!!Hurray!! No one is Guarding the Gate!!!"
        return True
    else:
        print "\n\t!!Be Aware,Guard on the Gate!!"
        return False
    
#passing different time intervals inputs for passing gate
date_string_intervals = ['2017-12-31 15:33','2018-01-01 07:09','2018-01-01 08:00','2018-02-01 08:18']
# Suggeston: can get current date alternatively!

#calculating champion health
def calculate_champion_health(champion,date_string_intervals):
    print "\t\tAmount of Health:-",hp
                  
#assign total damage to 0 and update value after each loop cycle
    total_damage = 0
    for i, date_string in enumerate(date_string_intervals):
            date = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
            day=date.strftime("%A")
            print "\n Date and Day:", date,day
            try:
                date_next = datetime.strptime(date_string_intervals[i+1], "%Y-%m-%d %H:%M")
            except IndexError:
                date_next = date
            
            next_damage = calculate_damage_taken(day,date,champion)
            
            interval = (date_next - date).total_seconds()
            
            if (interval >= 3600 or i == len(date_string_intervals) -1):
                total_damage += next_damage
                print "\nHealth loses By Champion: ",total_damage
            else:
                print "\n\"Clause: Champion should only lose HP once every hour,so you saved your health\""
    return total_damage

#calculate total health damage of champion while passing gates             
def calculate_damage_taken(day,date,champion):
#checking if the day is tuesday or thursday or the champion is invncible i.e. no guards can harm
    if (holly_day(day) or invincible_champion(champion)):
        return 0
    # "Janna" demon of Wind spawned
    if (date.hour == 6 and date.minute >= 0 and date.minute <= 29):
        print "/tYou loses 7 HP!!"
        return 7
    # "Tiamat" goddess of Oceans spawned
    elif (date.hour == 6 and date.minute >= 30 and date.minute <= 59):
        print "/tYou loses 18 HP!!"
        return 18
    # "Mithra" goddess of sun spawned
    elif (date.hour == 7 and date.minute >= 0 and date.minute <= 59):
        print "\tPowerful goddess \"Mithra\" guarding the gate,You loses 25 HP!!"
        return 25
    # "Warwick" God of war spawned
    elif (date.hour == 8 and date.minute >= 0 and date.minute <= 29):
        print "\tYou loses 18 HP"
        return 18
    # "Kalista" demon of agony spawned
    elif (date.hour >= 8 and date.hour <= 14 and date.minute >= 30 and date.minute <= 59):
        print "\tYou loses 7 HP"
        return 7
    # "Ahri" goddess of wisdom spawned
    elif (date.hour == 15 and date.minute >= 0 and date.minute <= 29):
        print "\tYou loses 13 HP"
        return 13
    # "Brand" god of fire spawned
    elif (date.hour == 15 and date.minute >= 0 or date.hour == 16 and date.minute <= 59):
        print "\tPowerful god \"Brand\" guarding the gate,You loses 25 HP!!"
        return 25
    # "Rumble" god of lightning spawned
    elif (date.hour == 17 and date.minute >= 0 and date.minute <= 59):
        print "\tYou loses 18 HP"
        return 18
    # "Skarner" the scorpion demon spawned
    elif (date.hour >= 18 and date.hour <= 19 and date.minute >= 0 and date.minute <= 59):
        print "\tYou loses 7 HP"
        return 7
    # "Luna" The goddess of the moon spawned
    elif (date.hour == 20 and date.minute <=59):
        print "\tYou loses 13 HP"
        return 13
    else:
        return 0

# printing option for choosing champion by the user. 
print("\t\t\a!!!WELCOME TO GATE OF ISHTHAR!!!\a")
print ("\tCreated by Shikha Kumari || Company Segula Technologies, Gothenburg Sweden")
print "Some basic Rules:\n1. Select Champion and take dare to pass the gate and meet Council of Wise"
print "2. Different Guards are guarding Gate some are Gods and some are Demons! Be Aware!!"
print "3. Their are two holy days tuesday & thursday, means no guard on Gate!!"
print "4. Champion loses Health while passing the gate between 7 to 25"
print("\nSelect champion.")
print "1.\tHuman"
print "2.\tWizard"    
print "3.\tGiant"
print "4.\tSpirit"
print "5.\tVampire"
print "0: \tQUIT"
# CHOOSE FROM 5 CHAMPION

#while True: // this can be implemented in further modification where user get option of playing multiple times.
    
CHOICE = int(raw_input("\nEnter any one choice (1/2/3/4/5/0):"))
#prinitng and selecting choosen champion and their Amount of Health i.e hp,it show hp a/c to user's champion selection
if CHOICE == 1:
    print("\t\tChampion selected: HUMAN")
    champion='Human'
    hp=100
elif CHOICE == 2:
    print("\t\tChampion selected: WIZARD")
    print("\t!!!Great you selected Magical Champion,Now Dont worry about guards!!!")
    champion='Wizard'
    hp=100
elif CHOICE == 3:
    print("\t\tChampion selected: GIANT")
    champion='Giant'
    hp=150
elif CHOICE == 4:
    print("\t\tChampion selected: SPIRIT")
    print("\t!!!Great you selected Magical Champion,Now Dont worry about guards!!!")
    champion='Spirit'
    hp=100
elif CHOICE == 5:
    print("\t\tChampion selected: VAMPIRE")
    champion='Vampire'
    hp=110
elif CHOICE == 0:
    exit()
else:
    print("\tPlease try between Given champions choices!!")
    exit()

hp = hp-calculate_champion_health(champion,date_string_intervals)
print "\nAmount Of Health remanied in Last of Day:",hp 
