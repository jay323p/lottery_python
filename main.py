from utils import initializer

def main():
    play_or_view = input("Would you like to play or view data/charts? (p/v): ")
    if (play_or_view.isalpha()):
        if (play_or_view.lower() == 'p'):
            return initializer.playGames()
        elif (play_or_view.lower() == 'v'):
            return initializer.viewData()
        else:
            print("ERROR: Invalid character selected. Please only select \'p\' or \'v\' | STATUS: 400")
            return main()
    else:
        print("ERROR: Please enter alphabetical character \'p\' or \'v\' only | STATUS: 400")
        return main()
    
main()
