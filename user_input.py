from price import get_info, confirm_stock
import sqlite3

conn = sqlite3.connect("StockPortfolio.db")
cursor = conn.cursor()

def get_stock():
    stock = input("Enter the name of the Stock or the Ticker: ").strip()
    print("\n")
    try:
        return confirm_stock(stock.capitalize())
    except:
        try:
            return get_info(stock.upper())

        except:
            raise ValueError
        

def add_to_watchlist(stock):
    decision = input("What do you plan on doing with this stock? (Buy, Sell, Hold)\n").strip().capitalize()
    cursor.execute("INSERT INTO Watchlist VALUES(?,?,?,?,?,?,?)", (stock.get("Company"),stock.get("Price"),stock.get("Market Cap"),stock.get("P/E"),stock.get("52 Week High"),stock.get("52 Week Low"),decision))
    conn.commit()
    print("\n")
    print("The stock has succesfully been added to the watchlist!")

def update_watchlist(stock):
    cursor.execute("UPDATE Watchlist SET Price = ?, Market = ?, P_E=?,High_52_Week =?,Low_52_Week=? WHERE Company =?", (stock.get("Price"),stock.get("Market Cap"),stock.get("P/E"),stock.get("52 Week High"),stock.get("52 Week Low"),stock.get("Company")))
    conn.commit()
