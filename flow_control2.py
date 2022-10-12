bowlers = ["Chahal","Bumrah","Shami"]
batsman = ["Dhoni","Kohli"]
all_rounders = ["Hardik Pandya","Yuvraj Singh"]
cricket=input("enter crickter name:")
if cricket in batsman:
    print("%s is a batsman"%(batsman[0]))
elif cricket in bowlers:
    print("{bowlers[2]} is a bowler".format(bowlers=bowlers))
else:
    print("{x[0]} is an all rounder".format(x=all_rounders))
