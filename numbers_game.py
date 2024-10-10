import mappers
import random
import print_styles
import rules

def numbers_game():
    # init vars
    print_styles.printBoxHeader("Numbers Game", rules.numbersRules)
    spots = 4
    userNums = getUserInputs(spots) # get user nums
    userBets = getUserBets() # {0: False, ...}
    # winNums = generateWinningNums() # generate winning nums
    winNums = [1,1,0,0] # generate winning nums
    payout_matcher = {}
    payout_matcher = determinePayout(spots, userBets, userNums, winNums) 
    payout = payout_matcher.get("payout")
    matcher = payout_matcher.get("matcher")
    gameData = {
        "userBets": userBets,
        "userNums": userNums,
        "winNums": winNums,
        "payout": payout,
        "matcher": matcher,
    }
    print_styles.printNumberGameWinner(gameData)
    print_styles.printCloser("NUMBER GAME")
    return gameData

    # return object with all important data


def getUserInputs(spots):
    nums = []
    for _ in range(spots):
        num = numInput(nums)
        nums.append(num)
    return nums

def numInput(nums):
    # input
    usr_num = input("Pick Number (0-9): ")
    # check is digit
    if (usr_num.isdigit() == False):
        errorPrinter("Please enter a numeric value 0-9", 400)
        return numInput(nums)
    usr_num = int(usr_num)
    # check is in range
    if (usr_num < 0 or usr_num > 9):
        errorPrinter(f"{usr_num} is out of bounds (0-9). Please enter a new number.", 400)
        return numInput(nums)
    return usr_num

def getUserBets():
    betsInfoPrinter()
    # init vars
    bets = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False,}
    tmp_bets = set()
    usrBets = getBets(bets, tmp_bets)
    return usrBets
    

def betsInfoPrinter():
    print("")
    print("")
    print("Please Enter Corresponding Number For Bet: ")
    print("")
    print("0: 1 Digit Exact")
    print("1: 2 Digit Exact")
    print("2: First 3 Exact")
    print("3: First 3 Any")
    print("4: Last 3 Exact")
    print("5: Last 3 Any")
    print("6: All 4 Any")
    print("7: All 4 Exact")
    print("8: Across The Board")
    print("")
    print("**PLEASE TYPE AND ENTER \"d\" TO FINISH BETTING**")
    print("")
    return

def getBets(bets, tmp_bets):
    isDoneBetting = False
    while (isDoneBetting == False):
        print("")
        usr_bet = input("Please Select A Bet Using Numbers 0-8: ")
        if (usr_bet == "d"): # user done betting
            if (len(tmp_bets) == 0): # bets made ? done betting : re-try bet input
                errorPrinter("Please Make At Least One Bet Before Continuing", 400)
                isDoneBetting = True
                return getBets(bets, tmp_bets)
            isDoneBetting = True 
            break
        if (usr_bet.isdigit()): # digit check
            usr_bet = int(usr_bet)
            if (0 <= usr_bet <= 7): # range 0-7 check
                if (usr_bet not in tmp_bets): # not repeat bet check
                    bets[usr_bet] = True
                    tmp_bets.add(usr_bet)
                    continue
                else:
                    errorPrinter("You have already made this bet. Please provide a new one or press d and enter to coninue", 400)
            elif (usr_bet == 8): # bet 8 made check
                for i in range(8):
                    if (i >= 2):
                        bets[i] = True
                    else:
                        continue
                bets[8] = True
                isDoneBetting = True
                break            
            else: # bet out of range check
                errorPrinter("Please Enter A Number Between 0 and 8", 400)
                isDoneBetting = True
                return getBets(bets, tmp_bets)
        else: # not digit check
            errorPrinter("Please Enter A Number Between 0 and 8", 400)
            isDoneBetting = True
            return getBets(bets, tmp_bets)
    return bets


def generateWinningNums():
    winNums = []
    for _ in range(4):
        rand_num = random.randint(0, 9)
        winNums.append(rand_num)
        
    return winNums

def determinePayout(spots, userBets, numsChosen, winNums):
    # bools
    matchOneDigit = False
    matchTwoDigit = False
    matchFirstThreeExact = False
    matchFirstThreeAny = False
    matchLastThreeExact = False
    matchLastThreeAny = False
    matchFourAny = False
    matchFourExact = False
    payoutMapper = mappers.numbersPayoutMapper
    # in numbers game, you only win highest winning bet
    # ex: if you win all-four-exact bet, you dont win 1 digit exact, 2 digit exact, etc.. even if such bets were placed
    # hence we start with the highest winning conditional and return accordingly if bet placed and won
    if (userBets[7] == True):
        matchFourExact = didMatchFourExact(numsChosen, winNums)
        if (matchFourExact):
            payout = payoutMapper[8]
            matcher = 8
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[6] == True):
        matchFourAny = didMatchFourAny(numsChosen, winNums)
        if (matchFourAny):
            payout = payoutMapper[7]
            matcher = 7
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[4] == True):
        matchLastThreeExact = didMatchLastThreeExact(numsChosen, winNums)
        if (matchLastThreeExact):
            payout = payoutMapper[5]
            matcher = 5
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[5] == True):
        matchLastThreeAny = didMatchLastThreeAny(numsChosen, winNums)
        if (matchLastThreeAny):
            payout = payoutMapper[6]
            matcher = 6
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[2] == True):
        matchFirstThreeExact = didMatchFirstThreeExact(numsChosen, winNums)
        if (matchFirstThreeExact):
            payout = payoutMapper[3]
            matcher = 3
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[3] == True):
        matchFirstThreeAny = didMatchFirstThreeAny(numsChosen, winNums)
        if (matchFirstThreeAny):
            payout = payoutMapper[4]
            matcher = 4
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[1] == True):
        matchTwoDigit = didMatchTwoDigit(spots, numsChosen, winNums)
        if (matchTwoDigit):
            payout = payoutMapper[2]
            matcher = 2
            return {
                "payout": payout,
                "matcher": matcher,
            }
    if (userBets[0] == True):
        matchOneDigit = didMatchOneDigit(spots, numsChosen, winNums)
        if (matchOneDigit):
            payout = payoutMapper[1]
            matcher = 1
            return {
                "payout": payout,
                "matcher": matcher,
            }
    return {
        "payout": 0,
        "matcher": 0,
    }



def errorPrinter(message, status):
    print("")
    print("")
    print("*" * len(message) * 2)
    print(f"Error: {message} | Status Code: {status if (status != None) else 400}")
    print("*" * len(message) * 2)
    print("")
    print("")

# ONE EXACT
def didMatchOneDigit(spots, numsChosen, winNums):
    for i in range(spots):
        if numsChosen[i] == winNums[i]:
            return True
    return False

# TWO EXACT 
def didMatchTwoDigit(spots, numsChosen, winNums):
    for i in range(spots - 1):
        if ((numsChosen[i] == winNums[i]) and (numsChosen[i+1] == winNums[i+1])):
            print("Two Matches Found ------------------------------")
            return True
    return False

# FIRST THREE EXACT
def didMatchFirstThreeExact(numsChosen, winNums):
    return (
        (numsChosen[0] == winNums[0]) and 
        (numsChosen[1] == winNums[1]) and 
        (numsChosen[2] == winNums[2])
        )

# FIRST THREE ANY
def didMatchFirstThreeAny(numsChosen, winNums):
    match_first_any = ((numsChosen[0] == winNums[0] or numsChosen[0] == winNums[1] or numsChosen[0] == winNums[2]))
    match_second_any = ((numsChosen[1] == winNums[0] or numsChosen[1] == winNums[1] or numsChosen[1] == winNums[2]))
    match_third_any = ((numsChosen[2] == winNums[0] or numsChosen[2] == winNums[1] or numsChosen[2] == winNums[2]))
    return match_first_any and match_second_any and match_third_any

# LAST THREE EXACT
def didMatchLastThreeExact(numsChosen, winNums):
    return (
        (numsChosen[3] == winNums[3]) and 
        (numsChosen[2] == winNums[2]) and 
        (numsChosen[1] == winNums[1])
        )

# LAST THREE ANY
def didMatchLastThreeAny(numsChosen, winNums):
    match_last_any = ((numsChosen[3] == winNums[3] or numsChosen[3] == winNums[2] or numsChosen[3] == winNums[1]))
    match_second_last_any = ((numsChosen[2] == winNums[3] or numsChosen[2] == winNums[2] or numsChosen[2] == winNums[1]))
    match_third_last_any = ((numsChosen[1] == winNums[3] or numsChosen[1] == winNums[2] or numsChosen[1] == winNums[1]))
    return match_last_any and match_second_last_any and match_third_last_any

# ALL FOUR EXACT
def didMatchFourExact(numsChosen, winNums):
    return (
        (numsChosen[0] == winNums[0]) and 
        (numsChosen[1] == winNums[1]) and 
        (numsChosen[2] == winNums[2]) and
        (numsChosen[3] == winNums[3])
        )

# ALL FOUR ANY
def didMatchFourAny(numsChosen, winNums):
    match_first_any = ((numsChosen[0] == winNums[0] or numsChosen[0] == winNums[1] or numsChosen[0] == winNums[2] or numsChosen[0] == winNums[3]))
    match_second_any = ((numsChosen[1] == winNums[0] or numsChosen[1] == winNums[1] or numsChosen[1] == winNums[2] or numsChosen[1] == winNums[3]))
    match_third_any = ((numsChosen[2] == winNums[0] or numsChosen[2] == winNums[1] or numsChosen[2] == winNums[2] or numsChosen[2] == winNums[3]))
    match_last_any = ((numsChosen[3] == winNums[0] or numsChosen[3] == winNums[1] or numsChosen[3] == winNums[2] or numsChosen[3] == winNums[3]))
    return match_first_any and match_second_any and match_third_any and match_last_any