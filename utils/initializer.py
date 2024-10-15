from static import constants
from utils import file_functions
from games import keno
from games import mass_cash
from games import numbers_game
import os
from games import powerball
from utils import plotter
from static import print_styles

def playGames():
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
        return playGames()

def viewData():
    print("Please provide CSV file path from data folder below (i.e: data/keno/keno_sims_1_6031327354759697.csv)")
    fp = input("File Path: ")
    fp = os.path.normpath(fp)
    groups = fp.split(os.sep)
    data_folder = groups[0]
    game_folder = groups[1]
    csv_file = groups[2]
    file_name_length = len(csv_file)
    file_ending = csv_file[file_name_length - 4:]
    
    if (file_ending == ".csv"):
        if (data_folder == "data"):
            if (game_folder == "keno" or game_folder == "numbers_game" or game_folder == "powerball" or game_folder == "mass_cash"):
                data = file_functions.read_csv_file(fp, game_folder)
                print_styles.print_file_extraction_success(f"********** Successful extraction of data from {csv_file} **********")
                plot = plotter.getPlotChoice()
                return plotter.generate_plot_data(plot, game_folder, data)
            else:
                print("ERROR: Invalid game folder provided. Only options are keno, numbers_game, powerball, and mass_cash | STATUS: 400")
                return viewData()
        else:
            print("ERROR: Please provide a file path that starts from the data folder (case-sensitive) | STATUS: 400")
            return viewData()
    else:
        print("ERROR: Please provide only CSV files in directory matching \"data\\[game_folder]\\file.csv\" | STATUS: 500")
        return viewData()