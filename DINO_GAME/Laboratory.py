from Minion_stats import *

from Minion_Emblem import minion1, Gru_emblem, Lucy_emblem, minion1_emblem, minion2_emblem, minion3_emblem, minion4_emblem, minion5_emblem, minion6_emblem, minion7_emblem, minion8_emblem, purple_minion_emblem, board1, board2, board3, board4, board5, board6, board7, board8, empty_board
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
    lb()
    while True:
        laboratory_choice=input("\n: ")
        if laboratory_choice==("gear"):
            print("Lets look at what you have unlocked")
            print(f"{inventory}")
            break            
        if laboratory_choice==("map"):
            print("You chose map")
        if laboratory_choice==("minions"):
            print("You chose minions")
        else:
            error()