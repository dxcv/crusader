# encoding: utf-8
import pandas as pd
import datetime
import os

import utils
import const

def update():
    df = pd.read_excel(const.LIST_FNAME)
    df = df.dropna()
    for name, code in zip(df[u'名称'], df[u'代码']):
        print name, code
        fname = '%s/%s.xlsx'%(const.DATA_DIR, name)
        end_date = datetime.date.today()
        if not os.path.exists(fname):
            start_date = const.START_DATE
            df = utils.download_wind_data(code, start_date, end_date)
        else:
            df = pd.read_excel(fname)
            start_date = df.index[-1] + datetime.timedelta(1)
            app_df = utils.download_wind_data(code, start_date, end_date)
            if pd.to_datetime(app_df.index[0]) >= start_date:
                df = df.append(app_df)
        df.to_excel(fname)

if __name__ == '__main__':
    update()
