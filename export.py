import pandas as pd
import os
import sqlite3
from utils import resource_path
from price import get_info
from user_input import update_watchlist

conn = sqlite3.connect("StockPortfolio.db")
cursor = conn.cursor()

def export_watchlist():
    output_file = os.path.join(os.getcwd(), "Watchlist.xlsx")
    df = pd.read_sql("SELECT * FROM Watchlist", conn)
    dfs = pd.read_csv(resource_path("Cleaned_Symbols.csv"))
    for company in df["Company"]:
        result = dfs[dfs['NAME OF COMPANY'].str.startswith(company.capitalize(), na=False)]["SYMBOL"]
        info = get_info(result.iloc[0])
        update_watchlist(info)
    df = pd.read_sql("SELECT * FROM Watchlist", conn)
    df.to_excel(output_file, index=False)
    print(f"Location: {output_file}")

def export_portfolio():
    output_file = os.path.join(os.getcwd(), "Portfolio.xlsx")
    df = pd.read_sql("SELECT * FROM Portfolio", conn)
    df.to_excel(output_file, index=False)
    print(f"Location: {output_file}")



