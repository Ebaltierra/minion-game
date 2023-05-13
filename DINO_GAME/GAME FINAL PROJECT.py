from Minion_stats import *
from Minion_Emblem import minion1, Gru_emblem, Lucy_emblem, minion1_emblem, minion2_emblem, minion3_emblem, minion4_emblem, minion5_emblem, minion6_emblem, minion7_emblem, minion8_emblem, purple_minion_emblem
def lb(): 
    print("\n========================================================================")
    input()
    
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
purple_minion_emblem()
minion8_emblem()
minion1_emblem()
minion2_emblem()
minion3_emblem()
minion4_emblem()
minion5_emblem()
minion6_emblem()
minion7_emblem()