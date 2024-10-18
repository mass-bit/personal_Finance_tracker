# importing all require module
import pandas as pd 
import csv
from datetime import datetime

# Creating a Class "CSV" for creating csv file and initialization

class CSV:
    CSV_file= "finance_data.csv"
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df= pd.DataFrame(columns=["date", "amoun", "category", "description"])
            df.to_csv(cls.CSV_file, index=False)

CSV.initialize_csv()