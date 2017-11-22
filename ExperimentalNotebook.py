# Getting Started  
# Calculating the inherent odds of winning an attack 

#%%
import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

def calculate_battle_winner(num_attacker_dice, num_defender_dice): 
    # This function figures calcutates how any dice roll will win 
    n = min(num_attacker_dice, num_defender_dice)
    num_attack_array = [] 
    num_defend_array = [] 
    battle_winner = 0 
    for i in range(num_attacker_dice): 
        num_attack_array.append(random.randint(1,6))
    for i in range(num_defender_dice): 
        num_defend_array.append(random.randint(1,6)) 
    num_attack_array.sort()
    num_attack_array.reverse()
    num_defend_array.sort()
    num_defend_array.reverse()
    for i in range(n):
        if num_attack_array[i] <= num_defend_array[i]: 
            battle_winner -= 1
        else: 
            battle_winner += 1 
    return battle_winner

def replay_attack(n, num_att, num_def):
    att_win = 0 
    def_win = 0 
    tie = 0 
    for i in range(n):
        battle_win = calculate_battle_winner(num_att, num_def)
        if battle_win == 0: 
            tie += 1 
        elif battle_win < 0: 
            def_win += 1
        else: 
            att_win += 1 
    return {'Attack':att_win, 'Defender':def_win, 'Tie':tie}

#%%
n = 1000000
# 3 attackers 2 defenders 
threeTwo = replay_attack(n, 3, 2)
print("3 att + 2 def")
print(threeTwo)

# 3 attackers 1 defender
threeOne = replay_attack(n, 3, 1)
print("3 att + 1 def")
print(threeOne)

# 2 attackers 2 defenders 
twoTwo = replay_attack(n, 2, 2) 
print("2 att + 2 def")
print(twoTwo)

# 2 attackers 1 defender 
twoOne = replay_attack(n, 2, 1) 
print("2 att + 1 def")
print(twoOne)

# 1 attackers 2 defender 
oneTwo = replay_attack(n, 1, 2) 
print("2 att + 1 def")
print(twoOne)

# 1 attacker 1 defender 
oneOne = replay_attack(n, 1, 1) 
print("1 att + 1 def")
print(oneOne)

#%%
df = pd.DataFrame([threeTwo, threeOne, twoTwo, twoOne, oneTwo, oneOne], columns=threeTwo.keys())
df = df.transpose()
df.columns = ['Three Two', 'Three One', 'Two Two', 'Two One', 'One Two', 'One One']
df
fig = plt.figure()
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)
df

sns.barplot(x=['Attack', 'Defender', 'Tie'], y=df['Three Two'], ax=ax1)
sns.barplot(x=['Attack', 'Defender', 'Tie'], y=df['Three One'], ax=ax2)
sns.barplot(x=['Attack', 'Defender', 'Tie'], y=df['Two Two'], ax=ax3)
sns.barplot(x=['Attack', 'Defender', 'Tie'], y=df['Two One'], ax=ax4)
sns.barplot(x=['Attack', 'Defender', 'Tie'], y=df['One Two'], ax=ax5)
sns.barplot(x=['Attack', 'Defender', 'Tie'], y=df['One One'], ax=ax6)

#%%
df['Three Two'] = df['Three Two']/n
df['Three One'] = df['Three One']/n
df['Two Two'] = df['Two Two']/n
df['Two One'] = df['Two One']/n
df['One Two'] = df['One Two']/n
df['One One'] = df['One One']/n
df 

#%% 
df