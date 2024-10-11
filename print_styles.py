# general -----------------------------------------------------------------------------------------------------------------------------------
def printBoxHeader(message: str, rules: list):
    print("  ________________________________________________________________________")
    print(f"||                                                                       ||")
    print(f"||                         [{message.upper()}]                            ||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||                                                                       ||")
    print(f"||                             **RULES**                                 ||")
    print("||_______________________________________________________________________||")
    for i in range(len(rules)):
        print(f"{i + 1}: {rules[i]}.")
    for _ in range(1):
        print("")
    print("||---------------------------LETS GET STARTED-----------------------------||")
    print("||------------------------------------------------------------------------||")
    for _ in range(3):
        print("")

def printCloser(game):
    for _ in range(2):
        print("")
    print(f"                        THANK YOU FOR PLAYING {game}                           ")
    print(f"                        HOPEFULLY YOU STOP GAMBLING                           ")
    print(f"                                PLEASE MOM                                     ")

# keno specific ------------------------------------------------------------------------------------------------------------------------------
def printKenoWinner(gameData: dict):
    print("  ________________________________________________________________________")
    print(f"||                                                                       ||")
    print(f"||                            [GAME DATA]                                ||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||                                                                       ||")
    for k,v in gameData.items():
        v: dict
        if (k == "spots"):
            print(f"                           **SPOTS CHOSEN**                            ")
            print(f"                                **{v}**                                ")
            print(f"                                                                       ")
        elif (k == "matches"):
            print(f"                              **MATCHES**                              ")
            print(f"                                **{v}**                                ")
            print(f"                                                                       ")

        elif (k == "payout"):
            print(f"                               **PAYOUT**                               ")
            print(f"                                **${v}**                                ")
            print(f"                                                                        ")

        elif (k == "numsChosen"):
            print(f"                            **NUMS CHOSEN**                             ")
            num_list = list(v.keys())
            num_list = str(num_list)
            spacer = (75 - len(num_list)) // 2
            print(" " * spacer + f"{"".join(num_list)}" + " " * spacer)
            print(f"                                                                        ")
        elif (k == "winNums"):
            print(f"                            **WIN NUMBERS**                             ")
            num_list = list(v.keys())
            num_list = str(num_list)
            spacer = (75 - len(num_list)) // 2
            print(" " * spacer + f"{"".join(num_list)}" + " " * spacer)
            print(f"                                                                        ")

# number game specific ------------------------------------------------------------------------------------------------------------------------------
def printNumberGameWinner(gameData: dict):
    betMapper = {
        0: "No Winner",
        1: "1 Digit",
        2: "2 Digit",
        3: "First 3 Exact",
        4: "First 3 Any",
        5: "Last 3 Exact",
        6: "Last 3 Any",
        7: "4 Any",
        8: "4 Exact",
    }
    print("  ________________________________________________________________________")
    print(f"||                                                                       ||")
    print(f"||                            [GAME DATA]                                ||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||                                                                       ||")
    for k,v in gameData.items():
        v: dict
        if (k == "userBets"):
            bets = ""
            for ky,va in v.items():
                if (ky == 8): continue
                if (va == True):
                    bets += f"{betMapper[ky]}, "
            print(f"                           **BETS CHOSEN**                            ")
            print(f"**{bets}**")
            print(f"                                                                       ")
        elif (k == "userNums"):
            print(f"                              **USER NUMBERS**                            ")
            print(f"                           **{"".join(str(v))}**                          ")
            print(f"                                                                       ")
        elif (k == "winNums"):
            print(f"                              **WIN NUMBERS**                            ")
            print(f"                           **{"".join(str(v))}**                          ")
            print(f"                                                                        ")
        elif (k == "matcher"):
            print(f"                              **MATCHER**                               ")
            if (v == 8):
                print(f"                               **Across The Board**                                ")
            else:
                print(f"                               **{betMapper[v]}**                                ")
            print(f"                                                                        ")
        elif (k == "payout"):
            print(f"                              **PAYOUT**                               ")
            print(f"                               **${v}**                                ")
            print(f"                                                                        ")

# powerball specific ------------------------------------------------------------------------------------------------------------------------------
def printPowerballWinner(gameData: dict):
    print("  ________________________________________________________________________")
    print(f"||                                                                       ||")
    print(f"||                            [GAME DATA]                                ||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||                                                                       ||")
    for k,v in gameData.items():
        v: dict
        if (k == "userNums"):
            print(f"                              **USER NUMBERS**                            ")
            print(f"                           **{"".join(str(v))}**                          ")
            print(f"                                                                       ")
        elif (k == "winNums"):
            print(f"                              **WIN NUMBERS**                            ")
            print(f"                           **{"".join(str(v))}**                          ")
            print(f"                                                                        ")
        elif (k == "match_pb_num"):
            print(f"                              **MATCHED PB**                               ")
            print(f"                               **{v}**                                ")
            print(f"                                                                        ")
        elif (k == "payout"):
            print(f"                              **PAYOUT**                               ")
            print(f"                               **${v}**                                ")
            print(f"                                                                        ")

# mass cash specific ------------------------------------------------------------------------------------------------------------------------------
def printMassCashWinner(gameData: dict):
    print("  ________________________________________________________________________")
    print(f"||                                                                       ||")
    print(f"||                            [GAME DATA]                                ||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||-----------------------------------------------------------------------||")
    print(f"||                                                                       ||")
    for k,v in gameData.items():
        v: dict
        if (k == "spots"):
            print(f"                           **SPOTS CHOSEN**                            ")
            print(f"                                **{v}**                                ")
            print(f"                                                                       ")
        elif (k == "matches"):
            print(f"                              **MATCHES**                              ")
            print(f"                                **{v}**                                ")
            print(f"                                                                       ")

        elif (k == "payout"):
            print(f"                               **PAYOUT**                               ")
            print(f"                                **${v}**                                ")
            print(f"                                                                        ")

        elif (k == "numsChosen"):
            print(f"                            **NUMS CHOSEN**                             ")
            num_list = list(v.keys())
            num_list = str(num_list)
            spacer = (75 - len(num_list)) // 2
            print(" " * spacer + f"{"".join(num_list)}" + " " * spacer)
            print(f"                                                                        ")
        elif (k == "winNums"):
            print(f"                            **WIN NUMBERS**                             ")
            num_list = list(v.keys())
            num_list = str(num_list)
            spacer = (75 - len(num_list)) // 2
            print(" " * spacer + f"{"".join(num_list)}" + " " * spacer)
            print(f"                                                                        ")

