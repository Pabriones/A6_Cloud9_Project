import random

def P_Ball():
    x = sorted(random.sample(range(1,70),5))
    y = random.randint(1,27)
    return x, y

print('Your Lucky Power Ball Numbers are',P_Ball())

##def five_ball(n):
##    F = P_Ball() * n
##    return F
##
##print(five_ball(5))
