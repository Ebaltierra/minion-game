from Minion_Emblem import minion1, Gru_emblem, Lucy_emblem, minion1_emblem, minion2_emblem, minion3_emblem, minion4_emblem, minion5_emblem, minion6_emblem, minion7_emblem, minion8_emblem, purple_minion_emblem, board1, board2, board3, board4, board5, board6, board7, board8, empty_board
Gru_health=int(20)
Gru_Max_health=int(20)
Gru_Attack=int(3)
Lucy_health=int(30)
Lucy_Max_health=int(30)
Lucy_Attack=int(2)
minion1_health=int(2)
minion2_health=int(4)
minion3_health=int(5)
minion4_health=int(7)
minion5_health=int(10)
minion6_health=int(14)
minion7_health=int(16)
minion8_health=int(20)
minion1_max_health=int(2)
minion2_max_health=int(4)
minion3_max_health=int(5)
minion4_max_health=int(7)
minion5_max_health=int(10)
minion6_max_health=int(14)
minion7_max_health=int(16)
minion8_max_health=int(20)
minion1_attack=int(1)
minion2_attack=int(2)
minion3_attack=int(3)
minion4_attack=int(3)
minion5_attack=int(5)
minion6_attack=int(8)
minion7_attack=int(8)
minion8_attack=int(9)
purpleminion_health=(30)
purpleminion_max_health=int(30)
purpleminion_attack=int(10)
HasFreeze_ray=False
HasBubblegum_grenade=False
HasKeytar=False
Hasglock19=True
HasFlamethrower=False
HasPirahnaGun=False
HasFartGun=False
HasBanana=False
inventory=[]
Know_more=str("")
break_laboratory_fork=False
lb1="\n=========================================================================="
freezeraydef=("\nFreeze Ray - Freeze ray deals 1 damage, and freezes enemy for 1 turn: 2 turn cooldown.")
keytardef=("\nKeytar - Keytar blasts enemy with music notes, dealing 2 damage.")
bubblegumdef=("\nBubble Gum Grenade - Deals 3 damages and allows you to move first next turn.")
pirahnagun=("\nPirahna Gun - Spawn pirahna to attack alongside you: Pirahna has 3 health and 1 attack")
bananadef=("\nBanana - Shoots a banana projectile dealing 2 damage and healing you for 2 health")
flamethrowerdef=("\nFlamethrower - Shoots massive flames that deal 2 damage per turn for 3 turns: 4 turn cooldown")
Fartgundef=("\nFart Gun - Shoots the smelliest fart known to man, dealing 2 damage, and knocking out minion for 2 turns: 4 turn cooldown.")
Glock19def=("\nGlock 19 - Kills minion.")
def lb(): 
    print("\n========================================================================")
    input()
def error():
    print("\nThat's not an answer silly, try again")
def laboratory_scene():
    print("\nYou are in your laboratory" + "\nA wall of gear appears in front of you, yet you don't have the ability to use them all"
          +"\nYou also see a map to your left detailing minlandia" +"\nTo your right you see the current minions you control"
          +"\nDo you want to view your gear, the map, or your minions? (gear/map/minions)" + lb1)    
def Knowmore():
    if HasFreeze_ray==True:
                print(freezeraydef)
                lb()
    elif HasKeytar==True:
                print(freezeraydef, keytardef)
                lb()
    elif HasBubblegum_grenade==True:
                print(freezeraydef, keytardef, bubblegumdef)
                lb()
    elif HasPirahnaGun==True:
                print(freezeraydef, keytardef, bubblegumdef, pirahnagun)
                lb()
    elif HasBanana==True:
                print(freezeraydef, keytardef, bubblegumdef, pirahnagun, bananadef,)
                lb()
    elif HasFlamethrower==True:
                print(freezeraydef, keytardef, bubblegumdef, pirahnagun, bananadef, flamethrowerdef)
                lb()
    elif HasFartGun==True:
                print(freezeraydef, keytardef, bubblegumdef, pirahnagun, bananadef, flamethrowerdef, Fartgundef)
                lb()
    elif Hasglock19==True:
                print(freezeraydef, keytardef, bubblegumdef, pirahnagun, bananadef, flamethrowerdef, Fartgundef, Glock19def)
                lb()
def Knowmorequestion():
    lb()
    print("\nWould you like to know more?")
    print(lb1)
    while True:
        Know_more=str(input("(\ny/n: )"))
        if Know_more==("y"):
            Knowmore()
            laboratory_scene()
            break
        elif Know_more==("n"):
            print("\nNo problem")
            laboratory_scene()
            break
        else: 
            error()
def Laboratory():
    lb()
    laboratory_scene()
    input()
    while True:
        laboratory_choice=input("\n: ")
        if laboratory_choice==("gear"):
            print("\nLets look at what you have unlocked")
            if HasFreeze_ray==True:
                board1()
                Knowmorequestion()
            elif HasKeytar==True:
                board2()
                Knowmorequestion()
            elif HasBubblegum_grenade==True:
                board3()
            elif HasPirahnaGun==True:
                board4()
                Knowmorequestion()
            elif HasBanana==True:
                board5()
                Knowmorequestion()
            elif HasFlamethrower==True:
                board6()
                Knowmorequestion()
            elif HasFartGun==True:
                board7()
                Knowmorequestion()
            elif Hasglock19==True:
                board8()
                Knowmorequestion()
            else:
                empty_board()
                lb()
                laboratory_scene()
                continue          
        if laboratory_choice==("map"):
            print("You chose map")
        if laboratory_choice==("minions"):
            print("You chose minions")
        else:
            error()
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