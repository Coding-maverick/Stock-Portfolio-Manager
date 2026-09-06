from user_input import get_stock, add_to_watchlist
from insights import insights, portfolio_analysis
from export import export_watchlist, export_portfolio

def main():
    while True:
        wish = int(input("""What do you wish to perform: 
1. Trade
2. View portfolio
3. Get Insights on a stock
4. View Watchlist
5. Get Portfolio Analysis 
6. Exit\n"""))
        print("*"*30)
    
        if wish == 1:
            pass

        elif wish == 2:
            export_portfolio()

        elif wish == 3:
            try:
                a = get_stock()
                for key, value in a.items():
                    print(f"{key}: {value}")

                print("\n")
                response = insights(a)
                print(response)
                print("\n")

                watchlist = input("Do you wish to add this stock to your watchlist? (Y/N)\n").upper().strip()
                if watchlist == "Y":
                    add_to_watchlist(a)
                elif watchlist == "N":
                    print("Okay!")
                else:
                    raise ValueError
            except Exception as e:
                print(e)

        elif wish == 4:
            export_watchlist()

        elif wish == 5:
            portfolio_analysis()

        elif wish == 6:
            quit()


if __name__ == "__main__":
    main()
