import csv
import os
import random

def save_file(gameData, f_name_single_game, f_name_simulation, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f_name_single_game)
    if (isinstance(gameData, dict)): # user played single game
        if (os.path.isdir(folder_path)): # is file created already
            with open(file_path, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=gameData.keys())
                writer.writerow(gameData)
        else: # is file not created yet
            with open(file_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=gameData.keys())
                writer.writeheader()
                writer.writerow(gameData)
        return
    elif (isinstance(gameData, list)): # user ran simulations
        # 1*
        rand_file_saver_num = ""
        sims = str(len(gameData))
        f_name_simulation += sims
        f_name_simulation += "_"
        for i in range(8):
            rn = str(random.randint(0, 9))
            rand_file_saver_num += rn
            rand_file_saver_num += str(i)
        f_name_simulation += rand_file_saver_num
        f_name_simulation += ".csv"
        file_path_simulations = os.path.join(folder_path, f_name_simulation)
        with open(file_path_simulations, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=gameData[0].keys())
            writer.writeheader()
            writer.writerows(gameData)
        return

# .csv file_ending validation must be done prior to this function call
def read_csv_file(fp):
    try:
        with open(fp, 'r') as f:
            csv_reader = csv.DictReader(f)
            data = [row for row in csv_reader]
            return data
    except Exception as e:
        print(e)

# 1* Create random file name to store each simulation session separately for easier data processing and graphing
