import random
import mappers
import print_styles
import rules
import simulations

def mass_cash():
    # init vars
    print_styles.printBoxHeader("Mass Cash", rules.massCashRules)
    shouldSimulate = simulations.simulateGames(errorPrinter)
    if (shouldSimulate):
        sims = simulations.getSimulationCount(errorPrinter)
        spots = 5
        userNums = getUserInputs(spots) # get user nums
        total_matches = 0
        total_payout = 0
        game_data_collection = []
        for i in range(sims):
            print(f"****************************************************************** SIMULATION-[{i + 1}] ******************************************************************")
            winNums = generateWinningNums() # generate winning nums
            gameData = determinePayout(spots, userNums, winNums)
            payout = gameData.get("payout")
            matches = gameData.get("matches")
            total_payout += payout
            total_matches += matches
            game_data_collection.append(gameData)
            print_styles.printMassCashWinner(gameData)
            print(f"**********************************************************************************************************************************************************")
        printSimulationReport(sims, total_matches, total_payout)
        return game_data_collection
    else:
        spots = 5
        userNums = getUserInputs(spots) # get user nums
        winNums = generateWinningNums() # generate winning nums
        gameData = determinePayout(spots, userNums, winNums)
        return gameData
    

def getUserInputs(spots):
    nums = {}
    for _ in range(spots):
        numInput(nums)
    print("")
    return nums

def numInput(nums):
    # input
    usr_num = input("Pick Un-Chosen Number (1-35): ")
    # check is digit
    if (usr_num.isdigit() == False):
        errorPrinter("Please enter a numeric value 1-35", 400)
        return numInput(nums)
    usr_num = int(usr_num)
    # check is unique
    if (usr_num in nums):
        errorPrinter(f"You have already chosen {usr_num}. Please enter a new number.", 400)
        return numInput(nums)
    # check is in range
    if (usr_num < 1 or usr_num > 35):
        errorPrinter(f"{usr_num} is out of bounds (1-35). Please enter a new number.", 400)
        return numInput(nums)
    # append to user_nums arr
    nums[usr_num] = True
    return usr_num

def generateWinningNums():
    winNums = {}
    for _ in range(5):
        rand_num = random.randint(1, 35)
        while (rand_num in winNums):
            rand_num = random.randint(1, 35)
        winNums[rand_num] = True
    return winNums

def determinePayout(spots, numsChosen, winNums):
    matches = 0
    payout = 0
    payoutMapper = mappers.massCashPayoutMapper

    for n in numsChosen.keys():
        if n in winNums:
            matches += 1
    payout = payoutMapper[matches]
    gameData = {
        "spots": spots,
        "matches": matches,
        "payout": payout,
        "numsChosen": numsChosen,
        "winNums": winNums
    }
    print_styles.printCloser("MASS CASH")
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