from GAME_FINAL_PROJECT import HasBanana, HasBubblegum_grenade, HasFartGun, HasFlamethrower, HasFreeze_ray, Hasglock19, HasKeytar, HasPirahnaGun, Gru_health, Lucy_health, Gru_Max_health, minion1_health, minion2_health, minion3_health, minion4_health, minion5_health, minion6_health, minion7_health, minion8_health, Lucy_Max_health, minion1_max_health, minion2_max_health, minion3_max_health, minion4_max_health, minion5_max_health, minion6_max_health, minion7_max_health, minion8_max_health, purpleminion_health, purpleminion_max_health, Gru_Attack, Lucy_Attack, minion1_attack, minion2_attack, minion3_attack, minion4_attack, minion5_attack, minion6_attack, minion7_attack, minion8_attack, purpleminion_attack
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
            print("Lets look at what you have unlocked" +f"{HasFreeze_ray}")
            if HasFreeze_ray==True:
                board1()
                print("Would you like to know more?")
            elif HasKeytar==True:
                board2()
                print("Would you like to know more?")
            elif HasBubblegum_grenade==True:
                board3()
                print("Would you like to know more?")
            elif HasPirahnaGun==True:
                board4()
                print("Would you like to know more?")
            elif HasBanana==True:
                board5()
                print("Would you like to know more?")
            elif HasFlamethrower==True:
                board6()
                print("Would you like to know more?")
            elif HasFartGun==True:
                board7()
                print("Would you like to know more?")
            elif Hasglock19==True:
                board8()
                print("Would you like to know more?")
            else:
                empty_board()          
        if laboratory_choice==("map"):
            print("You chose map")
        if laboratory_choice==("minions"):
            print("You chose minions")
        else:
            error()