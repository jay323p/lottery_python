import constants
import file_functions
import keno
import mass_cash
import numbers_game
import powerball
# get user inputs [gameChoice]

def main():
    print("Games Available: Keno, Numbers, Powerball, Mass Cash")
    game_chosen = input("Please Select A Game: ").lower()
    
    if (game_chosen in constants.GAMES_VALIDATORS):
        if (game_chosen == "keno"):             # keno route
            gameData = keno.keno()
            try:
                file_functions.save_file(gameData, constants.KENO_SINGLE_GAME_FILE_NAME, constants.KENO_SIMULATIONS_FILE_NAME, constants.KENO_FOLDER_PATH)
            except Exception as e:
                return keno.errorPrinter(f"UNABLE TO SAVE TO CSV FILE | MESSAGE: {e}", 400)
        elif (game_chosen == "numbers"):        # numbers game route
            gameData = numbers_game.numbers_game()
            try:
                file_functions.save_file(gameData, constants.NUMBERS_SINGLE_GAME_FILE_NAME, constants.NUMBERS_SIMULATIONS_FILE_NAME, constants.NUMBERS_FOLDER_PATH)
            except Exception as e:
                return keno.errorPrinter(f"UNABLE TO SAVE TO CSV FILE | MESSAGE: {e}", 400)
        elif (game_chosen == "powerball"):      # powerball route
            gameData = powerball.powerball()
            try:
                file_functions.save_file(gameData, constants.POWERBALL_SINGLE_GAME_FILE_NAME, constants.POWERBALL_SIMULATIONS_FILE_NAME, constants.POWERBALL_FOLDER_PATH)
            except Exception as e:
                return keno.errorPrinter(f"UNABLE TO SAVE TO CSV FILE | MESSAGE: {e}", 400)
        elif (game_chosen == "mass cash"):      # mass cash route
            gameData = mass_cash.mass_cash()
            try:
                file_functions.save_file(gameData, constants.MASS_CASH_SINGLE_GAME_FILE_NAME, constants.MASS_CASH_SIMULATIONS_FILE_NAME, constants.MASS_CASH_FOLDER_PATH)
            except Exception as e:
                return keno.errorPrinter(f"UNABLE TO SAVE TO CSV FILE | MESSAGE: {e}", 400)
    else:
        keno.errorPrinter("Invalid game choice", 400)
        return main()

main()
