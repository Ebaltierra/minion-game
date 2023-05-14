from Minion_stats import *
from Laboratory import Laboratory
from Minion_Emblem import minion1, Gru_emblem, Lucy_emblem, minion1_emblem, minion2_emblem, minion3_emblem, minion4_emblem, minion5_emblem, minion6_emblem, minion7_emblem, minion8_emblem, purple_minion_emblem, board1, board2, board3, board4, board5, board6, board7, board8, empty_board
def lb(): 
    print("\n========================================================================")
    input()
def error():
    print("\nThat's not an answer silly, try again")
    
lb()
minion1()
print("\nHELLO, WELCOME TO MINLANDIA SIMULATION CREATED BY MARGO, AGNES, AND EDITH ")
lb()
print("\nWho is playing in this simulation? (gru/lucy)")
lb()
while True:
    character=input("\n: ")
    if character==str("gru"):
        Gru_emblem()
        print("\nGreat, lets continue with our simulation")
        break
    elif character==str("lucy"):
        Lucy_emblem()
        print("\nGreat, lets continue with our simulation")
        break
    else:
        print("\nThat's not a character silly, try again.")
lb()
print("\nWould you like to put on the headset and enter minlandia? (y/n)")
lb()
while True:
    play=input("\n: ")
    if play==str("y"):
        print("\nGREAT, LETS ENTER MINLANDIA!!!")
        break
    elif play==str("n"):
        print("\nOkay, maybe some other time!!")
        quit()
    else: 
        error()
lb()
print("\nPixels fly around you, your head spins as your reality dissapears and is replaced"
      +"\n" +"\nYou watch as minlandia loads before your eyes. As you take in what appears around you"
      +"\nyou notice yellow, pill shaped creatures MINIONS running around green hills." + "\nRolling clouds of white cotton candy fly around your head"
      +"\nYou spot on the top of a mountain, A FLUFFY UNICORN" +"\n" +"\n...ahem" +"\n" 
      +"\nYou stand before the doors to your laboratory, and as you enter you take hold of all of your surroundings.")

Laboratory()
inventory.append(HasBanana)
print(f"{inventory}")