# encoding: utf-8
import pandas as pd
import numpy as np

import bank.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# M1同比增速、M2同比增速
source_m = ColumnDataSource(data=dict(date=[], m1=[], m2=[]))
def update_m():
    df = pd.read_excel(u'%s/M1同比增速.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/M2同比增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_m.data = {'date': df.index,
                     'm1': df[dic[u'M1同比增速']] / 100,
                     'm2': df[dic[u'M2同比增速']] / 100}

# 月度新增人民币贷款
source_loan = ColumnDataSource(data=dict(date=[], loan=[]))
def update_loan():
    df = pd.read_excel(u'%s/月度新增人民币贷款.xlsx'%(const.DATA_DIR))
    source_loan.data = {'date': df.index, 'loan': df[dic[u'月度新增人民币贷款']].pct_change(12)}

# 活期存款同比增速、定期存款同比增速
source_deposit = ColumnDataSource(data=dict(date=[], cur=[], dep=[]))
def update_deposit():
    df = pd.read_excel(u'%s/活期存款同比增速.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/定期存款同比增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_deposit.data = {'date': df.index,
                           'cur': df[dic[u'活期存款同比增速']].pct_change(4),
                           'dep': df[dic[u'定期存款同比增速']].pct_change(4)}

# 人民币贷款加权平均利率
source_rate = ColumnDataSource(data=dict(date=[], r=[]))
def update_rate():
    df = pd.read_excel(u'%s/人民币贷款加权平均利率.xlsx'%(const.DATA_DIR))
    source_rate.data = {'date': df.index, 'r': df[dic[u'人民币贷款加权平均利率']]}

# 1年期贷款基准利率
source_base = ColumnDataSource(data=dict(date=[], loan=[], dep=[]))
def update_base():
    df = pd.read_excel(u'%s/1年期贷款基准利率.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/1年期存款基准利率.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_base.data = {'date': df.index,
                        'loan': df[dic[u'1年期贷款基准利率']] / 100,
                        'dep': df[dic[u'1年期存款基准利率']] / 100}

# 商业银行不良贷款余额
source_bad = ColumnDataSource(data=dict(date=[], bad=[], r=[], bo=[]))
def update_bad():
    df = pd.read_excel(u'%s/商业银行不良贷款余额.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/商业银行不良贷款比例.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/商业银行拨备覆盖率.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_bad.data = {'date': df.index,
                       'bad': df[dic[u'商业银行不良贷款余额']].pct_change(4),
                       'r': df[dic[u'商业银行不良贷款比例']].pct_change(4),
                       'bo': df[dic[u'商业银行拨备覆盖率']].pct_change(4)}

# 企业家信心指数
source_conf = ColumnDataSource(data=dict(date=[], conf=[]))
def update_conf():
    df = pd.read_excel(u'%s/企业家信心指数.xlsx'%(const.DATA_DIR))
    source_conf.data = {'date': df.index, 'conf': df[dic[u'企业家信心指数']]}

# 城镇居民未来物价预期指数
source_price = ColumnDataSource(data=dict(date=[], p=[]))
def update_price():
    df = pd.read_excel(u'%s/城镇居民未来物价预期指数.xlsx'%(const.DATA_DIR))
    source_price.data = {'date': df.index, 'p': df[dic[u'城镇居民未来物价预期指数']]}

# 人民币存款同比增速
source_cny = ColumnDataSource(data=dict(date=[], dep=[], loan=[]))
def update_cny():
    df = pd.read_excel(u'%s/人民币存款同比增速.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/人民币贷款同比增速.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_cny.data = {'date': df.index,
                       'loan': df[dic[u'人民币存款同比增速']] / 100,
                       'dep': df[dic[u'人民币贷款同比增速']] / 100}

# 银行利润占产业利润的比例
source_profit = ColumnDataSource(data=dict(date=[], r=[], r1=[]))
def update_profit():
    df = pd.read_excel(u'%s/银行业金融机构税后利润.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/名义GDP.xlsx'%(const.DATA_DIR))
    tdf = tdf.rolling(window=4).sum()
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.dropna()
    r = df[dic[u'银行业金融机构税后利润']] / df[dic[u'名义GDP']]
    r = r[r.index >= '2006-01-01']
    source_profit.data = {'date': r.index, 'r': r, 'r1': r.pct_change()}

def update_all():
    update_m()
    update_loan()
    update_deposit()
    update_rate()
    update_base()
    update_bad()
    update_conf()
    update_price()
    update_cny()
    update_profit()

def get_plot(title, pct=False):
    tools = "pan,wheel_zoom,box_select,reset"
    plot = figure(plot_height=500, plot_width=1200, tools=tools, x_axis_type='datetime')
    plot.title.text_font_size = "15pt"
    plot.title.text_font = "Microsoft YaHei"
    plot.yaxis.minor_tick_line_color = None
    plot.title.text = title
    if pct:
        plot.yaxis.formatter = NumeralTickFormatter(format='0.00%')
    else:
        plot.yaxis.formatter = NumeralTickFormatter(format='0.00')
    return plot

plot_m = get_plot(u'M1、M2同比增速（月）', pct=True)
plot_m.line('date', 'm1', source=source_m, line_width=2, legend=u'M1同比增速')
plot_m.line('date', 'm2', source=source_m, line_width=2, color='green', legend=u'M2同比增速')

plot_loan = get_plot(u'月度新增人民币贷款（月）', pct=True)
plot_loan.line('date', 'loan', source=source_loan, line_width=2, legend=u'月度新增人民币贷款')

plot_deposit = get_plot(u'活期、定期存款同比增速（月）', pct=True)
plot_deposit.line('date', 'cur', source=source_deposit, line_width=2, legend=u'活期存款同比增速')
plot_deposit.line('date', 'dep', source=source_deposit, line_width=2, color='green', legend=u'定期存款同比增速')

plot_rate = get_plot(u'人民币贷款加权平均利率（季）', pct=True)
plot_rate.line('date', 'r', source=source_rate, line_width=2, legend=u'人民币贷款加权平均利率')

plot_base = get_plot(u'1年期贷款、存款基准利率（不定期）', pct=True)
plot_base.line('date', 'loan', source=source_base, line_width=2, legend=u'1年期贷款基准利率')
plot_base.line('date', 'dep', source=source_base, line_width=2, color='green', legend=u'1年期存款基准利率')

plot_bad = get_plot(u'商业银行不良贷款余额、比例与拨备覆盖率（季）', pct=True)
plot_bad.line('date', 'bad', source=source_bad, line_width=2, legend=u'商业银行不良贷款余额')
plot_bad.line('date', 'r', source=source_bad, line_width=2, color='green', legend=u'商业银行不良贷款比例')
plot_bad.line('date', 'bo', source=source_bad, line_width=2, color='red', legend=u'商业银行拨备覆盖率')

plot_conf = get_plot(u'企业家信心指数（季）')
plot_conf.line('date', 'conf', source=source_conf, line_width=2, legend=u'企业家信心指数')

plot_price = get_plot(u'城镇居民未来物价预期指数（季）')
plot_price.line('date', 'p', source=source_price, line_width=2, legend=u'城镇居民未来物价预期指数')

plot_cny = get_plot(u'人民币存款、贷款同比增速（月）', pct=True)
plot_cny.line('date', 'loan', source=source_cny, line_width=2, legend=u'人民币存款同比增速')
plot_cny.line('date', 'dep', source=source_cny, line_width=2, color='green', legend=u'人民币贷款同比增速')

plot_profit = get_plot(u'银行利润占产业利润的比例（季）', pct=True)
plot_profit.line('date', 'r', source=source_profit, line_width=2, legend=u'银行利润占产业利润的比例')
# plot_profit.line('date', 'r1', source=source_profit, line_width=2, color='green', legend=u'银行利润占产业利润的比例的一阶变化率')

update_all()

curdoc().add_root(column(plot_m, plot_loan, plot_deposit, plot_rate, plot_base, plot_bad, plot_conf, plot_price, plot_cny, plot_profit))
curdoc().title = u'银行中观数据库'
