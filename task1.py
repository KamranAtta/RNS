s,t = 7,10
# ball_range = [s,t]
position_a, position_b = 4 , 12
# position_b = 12
num_red_balls = 3
num_blue_balls = 3

count_a = 0 # number of blue balls
count_b = 0 # number of red balls

# distance_list_a = []

# distance_from_a = [None] * num_blue_balls
# distance_from_b = [None] * num_red_balls
distance_from_a=[3,-2,-4]
distance_from_b=[3,-2,-4]

for distance in distance_from_a:
    if position_a + distance >= s and position_a + distance <= t:
        count_a+= 1

for distance in distance_from_b:
    if position_b + distance >= s and position_b + distance <= t:
        count_b+= 1

print(count_a,'\n',count_b)
print('Working fine!!')