import yfinance as yf
import pandas as pd
from utils import resource_path

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)


def get_info(stock):
    ticker = yf.Ticker(f"{stock}.NS")
    info = ticker.info
    return{"Company": info["longName"],
        "Price": info["currentPrice"],
        "Market Cap": info["marketCap"],
        "P/E": info["trailingPE"],
        "52 Week High" : info["fiftyTwoWeekHigh"],
        "52 Week Low": info["fiftyTwoWeekLow"]}
         

def confirm_stock(stock):
    df = pd.read_csv(resource_path("Cleaned_Symbols.csv"))
    result = df[df['NAME OF COMPANY'].str.startswith(stock, na=False)]
    if result.shape[0] == 1:
        print(result)
        ask = input("Does this match your desired stock? (Y/N)\n").upper().strip()
        if ask == "Y":
            col = df[df['NAME OF COMPANY'].str.startswith(stock, na=False)]["SYMBOL"]
            return get_info(col.iloc[0])

        elif ask == "N":
            pass

        else:
            raise ValueError
        
    elif result.shape[0] == 0:
        raise Exception("The stock either doesn't exist or wrong input!")
    
    elif result.shape[0] >1:
        get_ticker(stock)
        print("*" *20)
        print("\n")
        stock = input("Please find the correct Symbol against the desired stock: ").upper().strip()
        return get_info(stock)

    else:
        raise Exception("The Stock doesnt exist!")


def get_ticker(stock):
    df = pd.read_csv(resource_path("Cleaned_Symbols.csv"))
    result = df[df['NAME OF COMPANY'].str.startswith(stock, na=False)]
    for symbol,company in zip(result["SYMBOL"], result["NAME OF COMPANY"]):
        print(f"{symbol} - {company}")
    print("\n")