import keno
import numbers_game
import powerball
import mass_cash
# get user inputs [gameChoice]

def main():
    print("Games Available: Keno, Numbers, Powerball, Mass Cash")
    games_validation = {"keno", "numbers", "powerball", "mass cash"}
    game_chosen = input("Please Select A Game: ").lower()
    if (game_chosen in games_validation):
        if (game_chosen == "keno"):
            keno.keno()
        elif (game_chosen == "numbers"):
            numbers_game.numbers_game()
        elif (game_chosen == "powerball"):
            powerball.powerball()
        elif (game_chosen == "mass cash"):
            mass_cash.mass_cash()
    else:
        print("Error: Invalid game choice | Status Code: 400")
        return main()

main()
