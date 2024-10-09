import random
import mappers

def keno():
    # init vars
    print("Welcome to Keno! ---------------------------------------------------------------------")
    print("")
    spots = getUserSpotChoice() # get user spots
    userNums = getUserInputs(spots) # get user nums
    winNums = generateWinningNums() # generate winning nums
    gameData = determinePayout(spots, userNums, winNums)
    return gameData

    # return object with all important data

def getUserSpotChoice():
    spots = input("How many spots would you like to play (1-12): ")
    print("")
    # spots input validation
    if (spots.isdigit()):
        spots = int(spots)
        if (1 <= spots <= 12):
            return spots
        else:
            errorPrinter("Invalid choice for spots", 400)
            return getUserSpotChoice()
    else:
        errorPrinter("Please enter a number for spots", 400)
        return getUserSpotChoice()

def getUserInputs(spots):
    nums = {}
    for _ in range(spots):
        usr_num = numInput(nums)
    print("")
    return nums

def numInput(nums):
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

def generateWinningNums():
    winNums = {}
    for _ in range(20):
        rand_num = random.randint(1, 80)
        while (rand_num in winNums):
            rand_num = random.randint(1, 80)
        winNums[rand_num] = True
    return winNums

def determinePayout(spots, numsChosen, winNums):
    matches = 0
    payout = 0
    payoutMapper = mappers.kenoPayoutMapper

    for n in numsChosen.keys():
        if n in winNums:
            matches += 1
    payout = payoutMapper[spots][matches]
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
