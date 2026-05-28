import numpy as num
print("Numpy is imported successfully")
class crickter:
    calculated_value=0
    def __init__(self,player_name,player_field):
        self.player_name=player_name
        self.player_field=player_field
    def batsmen(self,balls_faced,runs):
        self.balls_faced=balls_faced
        self.runs=runs
        self.calculated_value=(self.runs/self.balls_faced)*100
        #print(f"The Strike Rate of {self.player_name} is {self.calculated_value}")
        return self.calculated_value
    
    def bowler(self,balls_spelled,wickets):
        self.balls_spelled=balls_spelled
        self.wickets=wickets
        self.calculated_value=self.balls_spelled/self.wickets
        #print(f"The Strike Rate of {self.player_name} is {self.calculated_value}")
        return self.calculated_value

class analyzer(crickter):
    def __init__(self, player_name, player_field):
        super().__init__(player_name, player_field)
    def batstrikerate(self,balls,runs):
        return super().batsmen(balls,runs)
    def ballstrikerate(self,balls,wickets):
        return super().bowler(balls,wickets)

a=analyzer("Jasprit Bhumrah","Bowler")
b=analyzer("Virat Kohli","Batsmen")
c=analyzer("Sanju Samson","Batsmen")
"""d=analyzer("Rohit Sharma", "Batsmen")
e=analyzer("KL Rahul", "Batsmen")
f=analyzer("Hardik Pandya", "All Rounder")
g=analyzer("Ravindra Jadeja", "All Rounder")
h=analyzer("Mohammed Shami", "Bowler")
i=analyzer("Kuldeep Yadav", "Bowler")
j=analyzer("Suryakumar Yadav", "Batsmen")
k=analyzer("Rishabh Pant", "Batsmen")"""
all_players=[a,b,c]
bat_rate=[]
ball_rate=[]
total_runs=[]
total_wickets=[]
total=0
for i in all_players:
    balls=int(input("Enter number of balls faced by the player:"))
    runs=int(input("Enter number of runs scored by the player:"))
    total_runs.append(runs)
    val=i.batstrikerate(balls,runs)
    bat_rate.append(val)
for i in all_players:
    balls=int(input("Enter number of balls spelled by the player:"))
    wickets=int(input("Enter number of wickets done by the player:"))
    total_wickets.append(wickets)
    val=i.ballstrikerate(balls,wickets)
    ball_rate.append(val)
bat=num.array(bat_rate)
ball=num.array(ball_rate)
all_runs=num.array(total_runs)
all_wickets=num.array(total_wickets)
print("\n")

print("The average batting strike rate of the team is",num.mean(bat))
print("\n")
print("The average bowling rate of the team is",num.mean(ball))
print("\n")

print("The maximum score of the match by a player:",num.max(all_runs))
print("\n")
print("the maximum wickets taken by the player:",num.max(all_wickets))
print("\n")
bat_std=num.std(bat_rate)
ball_std=num.std(ball_rate)
print("\n")
print(bat_std,ball_std)

if (bat_std>0 and bat_std<10) and (ball_std>0 and ball_std<5):
    print("The team is highly consistent")
elif (bat_std>10 and bat_std<20) and (ball_std>5 and ball_std<10):
    print("The team is moderately consistent")
else:
    print("The team is very inconsistent")



