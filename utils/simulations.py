def simulateGames(errorPrinter):
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
    
def getSimulationCount(errorPrinter):
    sc = input("Please enter numeric value, under 100000, for how many simulations desired: ")
    limit = 100000
    if (sc.isdigit()):
        sc = int(sc)
        if (1 <= sc <= limit):
            return sc
        else:
            errorPrinter("Please enter a numeric value under 100000", 400)
            return getSimulationCount()
    else:
        errorPrinter("Please enter a numeric value under 100000", 400)
        return getSimulationCount()