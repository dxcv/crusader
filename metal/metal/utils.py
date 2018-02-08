# encoding: utf-8

from WindPy import w
import pandas as pd

w.start()

def wind2df(raw_data):
    dic = {}
    if len(raw_data.Times) == 1:
        Data = raw_data.Data[0]
    else:
        Data = raw_data.Data
    for data, code in zip(Data, raw_data.Codes):
        dic[str(code)] = data
    return pd.DataFrame(dic, index=raw_data.Times)

def download_wind_data(codes, start_date, end_date):
    '''
    返回dataframe
    '''
    data = w.edb(codes, start_date, end_date)
    df = wind2df(data)
    return df
