import pandas as pd
import openpyxl

df = pd.read_csv('linio_data-oct-date.csv')

df.to_excel("linio_date-oct-date.xlsx", encoding="utf-8")