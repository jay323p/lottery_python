import random
import mappers
import print_styles
import rules

def mass_cash():
    # init vars
    print_styles.printBoxHeader("Mass Cash", rules.massCashRules)
    spots = 5
    userNums = getUserInputs(spots) # get user nums
    winNums = generateWinningNums() # generate winning nums
    gameData = determinePayout(spots, userNums, winNums)
    # return gameData

    # return object with all important data


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
    print_styles.printMassCashWinner(gameData)
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
