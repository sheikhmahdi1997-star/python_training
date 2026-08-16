players={}

class Player:
    def __init__(self , name):
        while not name:
            print("Name can not be empty.")
            name= input("Enter your name: ")

        self.name=name

       

    def add_player(self ):
        players[self.name]= None


    def set_chioce(self , choice):
        c=["sang", "gheychi","kaghaz"]
        while choice not in c:
            print("Invalid input.")
            choice=input("Try again ( You can only enter sang or kaghaz or gheychi).").lower()
        players[self.name]= choice
        print(f"{choice} is selected for '{self.name}'. ✅")



class Game:
    def __init__(self):
        pass

    def set_winner(self , playername_1 , playername_2):
        if players[playername_1] == players[playername_2]:
            print("Tie! 🤝")
            return

        rules={
            "gheychi":"kaghaz",
            "sang":"gheychi",
            "kaghaz":"sang"
        }
        if rules [players[playername_1]] == players[playername_2]:
            print(f"{playername_1} wins. 🏆")
        else:
            print(f"{playername_2} wins. 🏆")


    




name_1= input("Player 1 enter your name: ")
player_1=Player(name_1)
player_1.add_player()
player_1.set_chioce(input("Please choice sang/kaghaz/gheychi: ").lower())




name_2= input("Player 2 enter your name: ")
player_2=Player(name_2)
player_2.add_player()
player_2.set_chioce(input("Please choice sang/kaghaz/gheychi: ").lower())


player_name= list(players.keys())
Game().set_winner(player_name[0], player_name[1])
