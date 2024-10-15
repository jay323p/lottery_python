import random
from utils import mappers
from static import print_styles
from static import rules
from utils import simulations

def powerball():
    # init vars
    print_styles.printBoxHeader("Powerball", rules.powerballRules)
    shouldSimulate = simulations.simulateGames(errorPrinter)
    if (shouldSimulate):
        game_data_collection = simulatePowerball()
        return game_data_collection
    else:
        gameData = playSinglePowerball()
        return gameData

def simulatePowerball():
    sims = simulations.getSimulationCount(errorPrinter)
    total_payout = 0
    game_data_collection = []
    userNums = []
    non_pb_checker = {}
    getUserInputs(userNums, non_pb_checker) # get user nums
    x = []
    y = []
    for i in range(sims):
        print(f"****************************************************************** SIMULATION-[{i + 1}] ******************************************************************")
        winNums = generateWinningNums() # generate winning nums
        gameData = determinePayout(userNums, non_pb_checker, winNums)
        payout = gameData.get("payout")
        total_payout += payout
        x.append(i)
        y.append(payout)
        game_data_collection.append(gameData)
        print_styles.printPowerballWinner(gameData)
        print(f"**********************************************************************************************************************************************************")
    
    mappers.mapLinePlot(x, y, f"Powerball {sims} Simulations", "Game Number #", "Payout $")
    printSimulationReport(sims, total_payout)
    return game_data_collection

def playSinglePowerball():
    userNums = []
    non_pb_checker = {}
    getUserInputs(userNums, non_pb_checker) # get user nums
    winNums = generateWinningNums() # generate winning nums
    gameData = determinePayout(userNums, non_pb_checker, winNums)
    print_styles.printPowerballWinner(gameData)
    print_styles.printCloser("POWERBALL")
    return gameData

def getUserInputs(userNums, non_pb_checker):
    # get non-powerball nums
    getNonPowerballNums(userNums, non_pb_checker)
    getPowerballNum(userNums)
    # get powerball num
    return 
# check if playth
def getNonPowerballNums(userNums, non_pb_checker):
    for i in range(5):
        num = numInput(False, non_pb_checker)
        userNums.append(num)
        non_pb_checker[num] = True
    
       
def getPowerballNum(userNums):
    num = numInput(True, None)
    userNums.append(num)

def numInput(isPowerball, non_pb_checker):
    if (isPowerball):
        pb_num = input("Please Choose A Powerball Number 1-26: ")
        if (pb_num.isdigit()):
            pb_num = int(pb_num)
            if (1 <= pb_num <= 26):
                return pb_num
            else:
                errorPrinter("Please enter a numeric value 1 to 26 for the powerball number", 400)
                return numInput(isPowerball, non_pb_checker)
        else:
            errorPrinter("Please enter a numeric value 1 to 26 for the powerball number", 400)
            return numInput(isPowerball, non_pb_checker)
    else:
        usr_num = input("Please Choose Number 1-69: ")
        if (usr_num.isdigit()):
            usr_num = int(usr_num)
            if (1 <= usr_num <= 69):
                if (usr_num not in non_pb_checker):
                    return usr_num
                else:
                    errorPrinter("You have already chosen that number. You must choose 5 unique non-powerball numbers", 400)
                    return numInput(isPowerball, non_pb_checker)
            else:
                errorPrinter("Please enter a numeric value 1 to 69 only.", 400)
                return numInput(isPowerball, non_pb_checker)
        else:
            errorPrinter("Please enter a numeric value 1 to 69 only.", 400)
            return numInput(isPowerball, non_pb_checker)



def generateWinningNums():
    winNums = {} # init dict for checks
    res = []
    # insert non-pb
    for _ in range(5):
        rand_num = random.randint(1, 69)
        while (rand_num in winNums):
            rand_num = random.randint(1, 69)
        res.append(rand_num)
        winNums[rand_num] = True
    # insert pb
    rand_pb_num = random.randint(1, 26)
    res.append(rand_pb_num)
    return res

def determinePayout(numsChosen, non_pb_checker, winNums):
    # pb num at end of both user and win arrs
    pb_payout_mapper = mappers.powerballPayoutMapper
    payout = 0
    match_pb_num = False
    if (numsChosen[5] == winNums[5]):
        match_pb_num = True
    non_pb_matches = 0
    for i in range(len(winNums) - 1):
        if (winNums[i] in non_pb_checker):
            non_pb_matches += 1
    
    if (match_pb_num):
        payout = pb_payout_mapper.get("True").get(non_pb_matches)
    else:
        payout = pb_payout_mapper.get("False").get(non_pb_matches)
    
    gameData = {
        "userNums": numsChosen,
        "winNums": winNums,
        "match_pb_num": match_pb_num,
        "non_pb_matches": non_pb_matches,
        "payout": payout
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

def printSimulationReport(simulations, total_payout):
        cost = simulations * 2
        avg_return = (total_payout / cost) * 100
        avg_loss = 100 - avg_return
        print("")
        print("")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++       RESULTS OF SIMULATION      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
        print("")
        print(f"-----------------------------------------------------  TOTAL COST: ${cost} --------------------------------------------------------------------")
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