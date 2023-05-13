def lb(): 
    print("\n========================================================================")
    input()
def error():
    print("\nThat's not an answer silly, try again")
def Laboratory():
    lb()
    print("\nYou are in your laboratory" + "\nA wall of gear appears in front of you, yet you don't have the ability to use them all"
          +"\nYou also see a map to your left detailing minlandia" +"\nTo your right you see the current minions you control"
          +"\nDo you want to view your gear, the map, or your minions? (gear/map/minions)")
    while True:
        laboratory_choice=input("\n: ")
        if laboratory_choice==("gear"):
            print("You chose gear")
        if laboratory_choice==("map"):
            print("You chose map")
        if laboratory_choice==("minions"):
            print("You chose minions")
        else:
            error()