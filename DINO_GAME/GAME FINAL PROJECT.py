from Minion_stats import *
from Minion_Emblem import minion1
from Minion_Emblem import Gru_emblem
from Minion_Emblem import Lucy_emblem
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
        Gru_emblem
        print("\nGreat, lets continue with our simulation")
        break
    elif character==str("lucy"):
        Lucy_emblem
        print("\nGreat, lets continue with our simulation")
        break
    else:
        print("\nThat's not a character silly, try again.")

