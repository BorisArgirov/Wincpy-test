# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer1 + ' ' + str(goal_0) + ',' + ' ' + scorer2 + ' ' + str(goal_1)
report = f'Ruud Gullit scored in the {goal_0}nd minute\nMarco van Basten scored in the {goal_1}th minute'
print(report) 

player = 'Ruud Gullit'
first_name = player[player.find('Ruud'):4]

print(first_name)
last_name_len = len(player[4:10])
name_short = 'R. Gullit'
print(name_short)
chant = ((first_name + '!' + player[4]) * 3) + first_name + '!'
print(chant)
good_chant = chant[4] != player[ :3]
print(good_chant)
