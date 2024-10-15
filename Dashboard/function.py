import pandas as pd

def load_data():
    df = pd.read_csv('Data/PRSA_Data_Guanyuan_20130301-20170228.csv')
    df.drop(columns=['No'], inplace=True)
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df.drop(columns=['year', 'month', 'day', 'hour'], inplace=True)
    df.set_index('datetime', inplace=True)
    return df

def categorize_hour(hour):
    if 7 <= hour <= 9 or 17 <= hour <= 19:
        return 'Busy'
    else:
        return 'Non-Busy'

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'