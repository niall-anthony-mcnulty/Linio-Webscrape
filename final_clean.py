import pandas as pd
import openpyxl
from datetime import datetime

df = pd.read_csv('linio_data-oct-date.csv')


def date_correction(col):

    # split the string to erase weird symbol
    if "º." in col:
        new_date =  str(col).split("º.")
        new_date_2 = ",".join(new_date)
    elif "º" in col:
        new_date =  str(col).split("º")
        new_date_2 = ",".join(new_date)
    elif "." in col:
        new_date =  str(col).split(".")
        new_date_2 = ",".join(new_date)

    # join them back together
    new_date_2 = ",".join(new_date)
    # return without trailing white space
    return new_date_2.rstrip()
                                                    

# ----------------------------------------------------------------------------------- #
# ---------------------------- Translate Month Sring -------------------------------- # 
def month_translation(col):
    if 'ene' in col:
        return col.replace('ene','January')
    elif 'feb' in col:
        return col.replace('feb','February')
    elif 'mar' in col:
        return col.replace('mar','March')
    elif 'abr' in col:
        return col.replace('abr','April')
    elif 'may' in col:
        return col.replace('may', 'May')
    elif 'jun' in col:
        return col.replace('jun','June')
    elif 'jul' in col:
        return col.replace('jul','July')
    elif 'ago' in col:
        return col.replace('ago','August')
    elif 'sep' in col:
        return col.replace('sep','September')
    elif 'oct' in col:
        return col.replace('oct', 'October')
    elif 'nov' in col:
        return col.replace('nov','November')
    elif 'dic' in col:
        return col.replace('dic','December')
    else:
        return str(col)


# ----------------------------------------------------------------------------------- #
# ------------------------ Change String to Datetime -------------------------------- # 
def date_time(col):
    try:
        return datetime.strptime(col, "%B %d, %Y")
    except:
        return pd.NaT

# ----------------------------------------------------------------------------------- #
# ------------------------ Call Functions & Save to Excel --------------------------- # 


# fix date
try:
    df['Dates'] = df['Dates'].apply(date_correction)
    

# translate month
    df['Dates'] = df['Dates'].apply(month_translation)
    

# apply datetime format
    df['Dates'] = df['Dates'].apply(date_time)

except:
    print('could not convert data')



df.to_excel("linio_date-oct-date.xlsx", encoding="utf-8")