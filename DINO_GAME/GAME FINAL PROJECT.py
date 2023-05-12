def lb():
  print(line_break)
  input()
line_break=("\n==================================================")
Health = 10
Coin = 5
minion1_health = 5
minion2_health = 10
minion3_health = 20
minion1_attack = 2
minion2_attack = 4
minion3_attack = 5
HasTranq = False
Hasminion1 = False
Hasminion2 = False
Hasminion3 = False



with open('Minion_emblem.py') as f:
  exec(f.read())
lb()
print("WELCOME TO ISLA NUBLO")
lb()
print("Your boat travels through rocky seas arriving on the coast of an abandoned, long forgotten island"
      )