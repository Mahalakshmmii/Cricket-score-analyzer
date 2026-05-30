import numpy as num
import csv#Comma Separated values
print("Numpy is imported successfully")
class Crickter:#for calsses names we should use Pascal case 
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
        if self.wickets==0:
            return 0
        self.calculated_value=self.balls_spelled/self.wickets
        #print(f"The Strike Rate of {self.player_name} is {self.calculated_value}")
        return self.calculated_value

class analyzer(Crickter):
    def __init__(self, player_name, player_field):
        super().__init__(player_name, player_field)
    def batstrikerate(self,balls,runs):
        return super().batsmen(balls,runs)
    def ballstrikerate(self,balls,wickets):
        return super().bowler(balls,wickets)
#n=int(input("Enter number of wickets of the match:"))
a=analyzer("Jasprit Bhumrah","Bowler")
b=analyzer("Virat Kohli","Batsmen")
c=analyzer("Sanju Samson","Batsmen")
d=analyzer("Rohit Sharma", "Batsmen")
e=analyzer("KL Rahul", "Batsmen")
f=analyzer("Hardik Pandya", "All Rounder")
g=analyzer("Ravindra Jadeja", "All Rounder")
h=analyzer("Mohammed Shami", "Bowler")
i=analyzer("Kuldeep Yadav", "Bowler")
j=analyzer("Suryakumar Yadav", "Batsmen")
k=analyzer("Rishabh Pant", "Batsmen")
all_players=[a,b,c,d,e,f,g,h,i,j,k]
bat_rate=[]
ball_rate=[]
total_runs=[]
total_wickets=[]


def batsmen_strikerate():
    for i in all_players:
        balls=int(input("Enter number of balls faced by the player:"))
        runs=int(input("Enter number of runs scored by the player:"))
        total_runs.append(runs)
        val=i.batstrikerate(balls,runs)
        bat_rate.append(val)
def bowler_consistency():
    for i in all_players:
        balls=int(input("Enter number of balls spelled by the player:"))
        wickets=int(input("Enter number of wickets done by the player:"))
        total_wickets.append(wickets)
        val=i.ballstrikerate(balls,wickets)
        ball_rate.append(val)




def average_rate(bat,ball):
    print("The average batting strike rate of the team is",num.mean(bat))
    #print("\n")
    print("The average bowling rate of the team is",num.mean(ball))
    #print("\n")

def maximum(all_runs,all_wickets):
    print("Highest runs scored by the player:",num.max(all_runs))
    #print("\n")
    print("Maximum wickets taken by the player:",num.max(all_wickets))
    #print("\n")

def consistency(bat_rate,ball_rate):
    bat_std=num.std(bat_rate)
    ball_std=num.std(ball_rate)
    #print("\n")
    print("Consistency of batting strike rate is:",bat_std)
    print("Consistency of bowling strike rate is:",ball_std)

    if (bat_std>=0 and bat_std<=10) and (ball_std>=0 and ball_std<=5):
         print("The team is highly consistent")
    elif (bat_std>=10 and bat_std<=20) and (ball_std>=5 and ball_std<=10):
         print("The team is moderately consistent")
    else:
        print("The team is very inconsistent")

def save_to_file():

    with open("cricket_stats.csv", mode="w", newline="") as file:#more professional way
        #file=open("cricket_stats.csv","w")-> it is also acceptable

        writer = csv.writer(file)

        writer.writerow(["Player Name", "Role", "Runs"])

        for i in all_players:

            writer.writerow([
                i.player_name,
                i.player_field,
                i.runs
            ])

    print("Data saved successfully!")


def menu():

    while True:

        choice = int(input("Enter your choice:"))

        if choice == 1:
            batsmen_strikerate()

        elif choice == 2:
            bowler_consistency()

        elif choice == 3:

            if len(bat_rate) == 0 and len(ball_rate) == 0:

                print("No player data entered yet!")

            else:

                bat=num.array(bat_rate)
                ball=num.array(ball_rate)
                all_runs=num.array(total_runs)
                all_wickets=num.array(total_wickets)

                average_rate(bat,ball)
                maximum(all_runs,all_wickets)
                consistency(bat_rate,ball_rate)

        elif choice == 4:

            if len(total_runs) == 0 and len(total_wickets) == 0:

                print("No data available to save!")

            else:

                save_to_file()

        elif choice == 5:

            print("Thank you for using Cricket Analyzer")

            break

        else:

            print("Invalid Choice")

print("\n-----CRICKET ANALYZER-----")
print("1. Enter Batting Data")
print("2. Enter Bowling Data")
print("3. Show Analysis")
print("4. Save Data")
print("5. Exit")

menu()

