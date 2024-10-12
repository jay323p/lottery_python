import random
import mappers
import rules
import print_styles
import csv

def keno(): # -> dict : {spots, matches, payout, numsChosen, winNums}
    print_styles.printBoxHeader("Welcome to Keno!", rules.kenoRules) # header
    shouldSimulate = simulateGames()
    if (shouldSimulate):
        simulations = getSimulationCount()
        spots = getUserSpotChoice() # get user spots
        userNums = getUserInputs(spots) # get user nums
        total_payout = 0
        total_matches = 0
        game_data_collection = []
        for i in range(simulations):
            print(f"****************************************************************** SIMULATION-[{i + 1}] ******************************************************************")
            winNums = generateWinningNums() # generate winning nums
            gameData = determinePayout(spots, userNums, winNums) # {spots, matches, payout, numsChosen, winNums}
            total_payout += gameData.get("payout")
            total_matches += gameData.get("matches")
            game_data_collection.append(gameData)
            print_styles.printKenoWinner(gameData)
            print(f"**********************************************************************************************************************************************************")

        printSimulationReport(simulations, total_matches, total_payout)
        print_styles.printCloser("KENO")
        return game_data_collection
    else:
        spots = getUserSpotChoice() # get user spots
        userNums = getUserInputs(spots) # get user nums
        winNums = generateWinningNums() # generate winning nums
        gameData = determinePayout(spots, userNums, winNums) # {spots, matches, payout, numsChosen, winNums}
        # print/return data
        print_styles.printKenoWinner(gameData)
        print_styles.printCloser("KENO")
        return gameData

def simulateGames():
    q = input("Would you like to simulate your games played (y/n): ")
    if (q.isalpha()):
        q = q.lower()
        if (q == "y" or q == "yes"):
            return True
        elif (q == "n" or q == "no"):
            return False
        else:
            errorPrinter("Invalid response provided. Please enter \"y\" or \"n\" only.", 400)
            return simulateGames()
    else:
        errorPrinter("Please enter alphabetical characters only", 400)
        return simulateGames()


def getSimulationCount():
    sc = input("Please enter numeric value, under 100, for how many simulations desired: ")
    limit = 1000
    if (sc.isdigit()):
        sc = int(sc)
        if (1 <= sc <= limit):
            return sc
        else:
            errorPrinter("Please enter a numeric value under 100", 400)
            return getSimulationCount()
    else:
        errorPrinter("Please enter a numeric value under 100", 400)
        return getSimulationCount()


def getUserSpotChoice(): # -> int : range[1-12]
    spots = input("How many spots would you like to play (1-12): ")
    print("") # inp + spacer
    if (spots.isdigit()): # inp:str is digit check
        spots = int(spots)
        if (1 <= spots <= 12): # inp:int in range[1-12] check
            return spots
        else:
            errorPrinter("Invalid choice for spots", 400)
            return getUserSpotChoice()
    else:
        errorPrinter("Please enter a number for spots", 400)
        return getUserSpotChoice()

def getUserInputs(spots): # -> dict: {1: True, ...} : len(spots)
    nums = {}
    for _ in range(spots): # updating nums in helper fxn
        numInput(nums)
    return nums

def numInput(nums): # -> int : range[1-80]
    # input
    usr_num = input("Pick Un-Chosen Number (1-80): ")
    # check is digit
    if (usr_num.isdigit() == False):
        errorPrinter("Please enter a numeric value 1-80", 400)
        return numInput(nums)
    usr_num = int(usr_num)
    # check is unique
    if (usr_num in nums):
        errorPrinter(f"You have already chosen {usr_num}. Please enter a new number.", 400)
        return numInput(nums)
    # check is in range
    if (usr_num < 1 or usr_num > 80):
        errorPrinter(f"{usr_num} is out of bounds (1-80). Please enter a new number.", 400)
        return numInput(nums)
    # append to user_nums arr
    nums[usr_num] = True
    return usr_num

def generateWinningNums(): # -> dict : {1: True, ...} : len(20)
    winNums = {}
    for _ in range(20): # random, unique number required each iteration
        rand_num = random.randint(1, 80)
        while (rand_num in winNums): # unique check
            rand_num = random.randint(1, 80)
        winNums[rand_num] = True
    return winNums

def determinePayout(spots, numsChosen, winNums): # -> dict : {spots, matches, payout, numsChosen, winNums}
    # init vars
    matches = 0
    payout = 0
    payoutMapper = mappers.kenoPayoutMapper

    for n in numsChosen.keys(): # increment match if found
        if n in winNums:
            matches += 1

    payout = payoutMapper[spots][matches] # ex-access: {5-spot: {0-match: $0, 1-match: $0, ...}, ...}
    gameData = {
        "spots": spots,
        "matches": matches,
        "payout": payout,
        "numsChosen": numsChosen,
        "winNums": winNums
    }
    return gameData


def errorPrinter(message, status):
    print("")
    print("")
    print("*" * len(message) * 2)
    print(f"Error: {message} | Status Code: {status if (status != None) else 400}")
    print("*" * len(message) * 2)
    print("")
    print("")

def printSimulationReport(simulations, total_matches, total_payout):
        avg_matches = total_matches / simulations
        avg_return = (total_payout / simulations) * 100
        avg_loss = 100 - avg_return
        print("")
        print("")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++       RESULTS OF SIMULATION      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
        print("")
        print(f"-------------------------------------------  TOTAL MATCHES: {total_matches} matches in {simulations} simulations   -------------------------------------------------")
        print(f"-------------------------------------------  AVERAGE MATCHES PER SIMULATION: {avg_matches} matches   ---------------------------------------------------------------")
        print(f"-------------------------------------------  TOTAL PAYOUT: ${total_payout} winnings in {simulations} simulations   --------------------------------------------------")
        print(f"-------------------------------------------  AVERAGE RETURN PERCENT PER SIMULATION: {avg_return}% per game  ---------------------------------------------------------")
        print(f"-------------------------------------------  AVERAGE LOSS PERCENT PER SIMULATION: {avg_loss}% per game  ---------------------------------------------------------")
        if (avg_loss < 0):
            print(f"-------------------------------------------  CONGRATS, YOU ACTUALLY MADE MORE MONEY THAN YOU BET THIS TIME  ---------------------------------------------------------")
        else:
            print(f"------------------------------------------- YEAH, GAMBLING IS TOUGH INNIT. ITS ALL ABOUT LUCK.  ---------------------------------------------------------")
        print("")
        print("")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++       RESULTS OF SIMULATION      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")