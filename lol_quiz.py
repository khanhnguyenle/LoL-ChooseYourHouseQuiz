# ----------------------------------------------------------------------------
# Written by Khanh Nguyen Le
# May 4th 2019
# Discord: https://discord.io/skyrst
# ----------------------------------------------------------------------------
import operator
def validInput(x):
    if x=="a": return True
    elif x=="b": return True
    elif x=="c": return True
    elif x=="d": return True
    else: return False
    
def takeInput():
    x=input()
    while not validInput(x):
        print("Invalid input. Try another one:")
        x=input()
    return x
    
def main():
    stats = {'Council':0, 'United':0, 'Faceless': 0, 'Warband':0}
    print("Welcome to Skyrst's open-source recreation of League of Legends house entrance quiz.")
    print("Answer the the following questions by typing a, b, c or d.")
    print("1/8")
    print("I'd die without my...\na. Freedom\nb. Knowledge\nc. Talent\nd. Hope")
    x = takeInput()
    if x=="a":
        stats['Faceless'] += 1
    elif x=="b":
        stats['Council']+= 1
    elif x=="c":
        stats['Warband']+= 1
    else:
        stats['United']+= 1
    print("2/8")
    print("Pick an animal:\na. Owl\nb. Leopard\nc. Elepant\nd. Octopus")
    x = takeInput()
    if x=="a":
        stats['Warband'] += 1
    elif x=="b":
        stats['Faceless']+= 1
    elif x=="c":
        stats['United']+= 1
    else:
        stats['Council']+= 1
    print("3/8")
    print("Wars are won...\na. In the heat of battle\nb. In the planning room\nc. With unbreaking resolve\nd. By the unpredictable")
    x = takeInput()
    if x=="a":
        stats['Warband'] += 1
    elif x=="b":
        stats['Council']+= 1
    elif x=="c":
        stats['United']+= 1
    else:
        stats['Faceless']+= 1
    print("4/8")
    print("The perfect team would never...\na. Give up\nb. Lose focus\nc. Tell me what to do\nd. Feed my opponent")
    x = takeInput()
    if x=="a":
        stats['United'] += 1
    elif x=="b":
        stats['Council']+= 1
    elif x=="c":
        stats['Warband']+= 1
    else:
        stats['Faceless']+= 1
    print("5/8")
    print("The enemy team is winning on all fronts. What do you do?\na. Outmaneuver them to steal some objectives\nb. Rally my team for a final stand\nc. Go pentakill them, like I always do\nd. This is right where I want them--I'll explain later")
    x = takeInput()
    if x=="a":
        stats['Faceless'] += 1
    elif x=="b":
        stats['United']+= 1
    elif x=="c":
        stats['Warband']+= 1
    else:
        stats['Council']+= 1
    print("6/8")
    print("What's your favorite time of the day\na. Dawn\nb. Day\nc. Dusk\nd. Night")
    x = takeInput()
    if x=="a":
        stats['United'] += 1
    elif x=="b":
        stats['Council']+= 1
    elif x=="c":
        stats['Faceless']+= 1
    else:
        stats['Warband']+= 1
    print("7/8")
    print("Which of these sounds like you\na. \"Can we please group\"\nb. \"Trust me. I'm not trolling\"\nc. \"ez\"\nd. \"WINNABLE\"")
    x = takeInput()
    if x=="a":
        stats['Council'] += 1
    elif x=="b":
        stats['Faceless']+= 1
    elif x=="c":
        stats['Warband']+= 1
    else:
        stats['United']+= 1
    print("8/8")
    print("I want to be seen as a(n)...\na. Selfless leader\nb. Brilliant tactician\nc. Crafty wildcard\nd. Elite fighter")
    x = takeInput()
    if x=="a":
        stats['United'] += 1
    elif x=="b":
        stats['Council']+= 1
    elif x=="c":
        stats['Faceless']+= 1
    else:
        stats['Warband']+= 1
    print("\n")
    
    result = max(stats.items(), key=operator.itemgetter(1))[0]
    print("Congratulations! You are a " +result)


main()