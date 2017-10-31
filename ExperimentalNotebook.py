# Getting Started  
# Calculating the inherent odds of winning an attack 

#%%
import random

def calculate_battle_winner(num_attacker_dice, num_defender_dice): 
    # This function figures calcutates how any dice roll will win 
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
    for i in range(num_defender_dice):
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
    return att_win, def_win, tie

n = 1000000000
# 3 attackers 2 defenders 
att_win_3_2, def_win_3_2, tie_win_3_2 = replay_attack(n, 3, 2)
print(att_win_3_2)

# 3 attackers 1 defender
att_win_3_1, def_win_3_1, _ = replay_attack(n, 3, 1)

print(att_win_3_1)
# 2 attackers 2 defenders 
att_win_2_2, def_win_2_2, _= replay_attack(n, 2, 2) 

print(att_win_2_2)
# 2 attackers 1 defender 
att_win_2_1, def_win_2_1, _ = replay_attack(n, 2, 1) 
print(att_win_2_1)

# 1 attacker 1 defender 
att_win_1_1, def_win_1_1, _ = replay_attack(n, 1, 1) 
print(att_win_1_1)