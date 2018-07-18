# encoding: utf-8
import pandas as pd
import numpy as np

import steel.const as const

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.plotting import figure

col_df = pd.read_excel(const.LIST_FNAME)
dic = {k: v for k, v in zip(col_df[u'名称'], col_df[u'代码'])}

# 钢材产量
source_prod = ColumnDataSource(data=dict(date=[], st=[], cg=[], lwg=[], lz=[]))
def update_prod():
    df = pd.read_excel(u'%s/生铁产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/粗钢产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/螺纹钢产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/冷轧产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_prod.data = {'date': df.index,
                        'st': df[dic[u'生铁产量']] / 100,
                        'cg': df[dic[u'粗钢产量']] / 100,
                        'lwg': df[dic[u'螺纹钢产量']].pct_change(12),
                        'lz': df[dic[u'冷轧产量']] / 100}

# 钢材库存
source_inv = ColumnDataSource(data=dict(date=[], tot=[], lwg=[], rj=[], lz=[]))
def update_inv():
    df = pd.read_excel(u'%s/钢材总社会库存.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/螺纹钢社会库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/热卷社会库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/冷轧社会库存.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_inv.data = {'date': df.index,
                       'tot': df[dic[u'钢材总社会库存']].pct_change(50),
                       'lwg': df[dic[u'螺纹钢社会库存']].pct_change(50),
                       'rj': df[dic[u'热卷社会库存']].pct_change(50),
                       'lz': df[dic[u'冷轧社会库存']].pct_change(50)}

# 钢材价格
source_pri = ColumnDataSource(data=dict(date=[], lwg=[], rj=[], lz=[]))
def update_pri():
    df = pd.read_excel(u'%s/上海25毫米螺纹钢价格.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/上海5.5毫米热卷价格.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/上海1.0毫米冷轧价格.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_pri.data = {'date': df.index,
                       'lwg': df[dic[u'上海25毫米螺纹钢价格']],
                       'rj': df[dic[u'上海5.5毫米热卷价格']],
                       'lz': df[dic[u'上海1.0毫米冷轧价格']]}

# 钢材进出口量
source_inp = ColumnDataSource(data=dict(date=[], inp=[], out=[]))
def update_inp():
    df = pd.read_excel(u'%s/钢材进口量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/钢材出口量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_inp.data = {'date': df.index,
                       'inp': df[dic[u'钢材进口量']] / 100,
                       'out': df[dic[u'钢材出口量']] / 100}

# 钢材出厂价
source_fac = ColumnDataSource(data=dict(date=[], bg=[], ag=[], sg=[], hg=[]))
def update_fac():
    df = pd.read_excel(u'%s/宝钢出厂价格.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/鞍钢出厂价格.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/沙钢出厂价格.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/河北钢铁出厂价格.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_fac.data = {'date': df.index,
                       'bg': df[dic[u'宝钢出厂价格']],
                       'ag': df[dic[u'鞍钢出厂价格']],
                       'sg': df[dic[u'沙钢出厂价格']],
                       'hg': df[dic[u'河北钢铁出厂价格']]}

# 原材料价格
source_raw = ColumnDataSource(data=dict(date=[], tj=[], ts=[], ty=[], jz=[]))
def update_raw():
    df = pd.read_excel(u'%s/天津港港口63.5%%印度粉现汇车板平均价.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/唐山地区66%%酸性铁精粉含税出厂平均价.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/山西太原古交2#焦煤车板含税价.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/华北山西晋中二级冶金焦含税车板成交平均价.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_raw.data = {'date': df.index,
                       'tj': df[dic[u'天津港港口63.5%印度粉现汇车板平均价']],
                       'ts': df[dic[u'唐山地区66%酸性铁精粉含税出厂平均价']],
                       'ty': df[dic[u'山西太原古交2#焦煤车板含税价']],
                       'jz': df[dic[u'华北山西晋中二级冶金焦含税车板成交平均价']]}

# 高炉开工率
source_open = ColumnDataSource(data=dict(date=[], open=[]))
def update_open():
    df = pd.read_excel(u'%s/高炉开工率.xlsx'%(const.DATA_DIR))
    source_open.data = {'date': df.index, 'open': df[dic[u'高炉开工率']] / 100}

# 新加坡铁矿石掉期合同
source_st = ColumnDataSource(data=dict(date=[], p=[]))
def update_st():
    df = pd.read_excel(u'%s/新加坡铁矿石掉期合同.xlsx'%(const.DATA_DIR))
    source_st.data = {'date': df.index, 'p': df[dic[u'新加坡铁矿石掉期合同']]}

# 中国铁矿石价格指数
source_stp = ColumnDataSource(data=dict(date=[], p=[]))
def update_stp():
    df = pd.read_excel(u'%s/中国铁矿石价格指数.xlsx'%(const.DATA_DIR))
    source_stp.data = {'date': df.index, 'p': df[dic[u'中国铁矿石价格指数']]}

# 下游产品产量
source_down = ColumnDataSource(data=dict(date=[], ice=[], mec=[], boat=[], car=[]))
def update_down():
    df = pd.read_excel(u'%s/机床产量.xlsx'%(const.DATA_DIR))
    tdf = pd.read_excel(u'%s/船舶产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/乘用车产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    tdf = pd.read_excel(u'%s/冰箱产量.xlsx'%(const.DATA_DIR))
    df = df.merge(tdf, how='outer', left_index=True, right_index=True)
    df = df.fillna(method='ffill')
    source_down.data = {'date': df.index,
                        'mec': df[dic[u'机床产量']] / 100,
                        'boat': df[dic[u'船舶产量']] / 100,
                        'car': df[dic[u'乘用车产量']] / 100,
                        'ice': df[dic[u'冰箱产量']] / 100}

def update_all():
    update_prod()
    update_inv()
    update_pri()
    update_inp()
    update_fac()
    update_raw()
    update_st()
    update_down()
    update_open()
    update_stp()

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

plot_prod = get_plot(u'钢材产量同比（月）', pct=True)
plot_prod.line('date', 'st', source=source_prod, line_width=2, legend=u'生铁产量')
plot_prod.line('date', 'cg', source=source_prod, line_width=2, color='green', legend=u'粗钢产量')
plot_prod.line('date', 'lwg', source=source_prod, line_width=2, color='red', legend=u'螺纹钢产量')
plot_prod.line('date', 'lz', source=source_prod, line_width=2, color='gray', legend=u'冷轧产量')

plot_inv = get_plot(u'钢材社会库存同比（周）', pct=True)
plot_inv.line('date', 'tot', source=source_inv, line_width=2, legend=u'钢材总社会库存')
plot_inv.line('date', 'lwg', source=source_inv, line_width=2, color='red', legend=u'螺纹钢社会库存')
plot_inv.line('date', 'rj', source=source_inv, line_width=2, color='green', legend=u'热卷社会库存')
plot_inv.line('date', 'lz', source=source_inv, line_width=2, color='gray', legend=u'冷轧社会库存')

plot_pri = get_plot(u'钢材价格（周）')
plot_pri.line('date', 'lwg', source=source_pri, line_width=2, legend=u'上海25毫米螺纹钢价格')
plot_pri.line('date', 'rj', source=source_pri, line_width=2, color='green', legend=u'上海5.5毫米热卷价格')
plot_pri.line('date', 'lz', source=source_pri, line_width=2, color='red', legend=u'上海1.0毫米冷轧价格')

plot_inp = get_plot(u'钢材进出口量同比（月）', pct=True)
plot_inp.line('date', 'inp', source=source_inp, line_width=2, legend=u'钢材进口量')
plot_inp.line('date', 'out', source=source_inp, line_width=2, color='green', legend=u'钢材出口量')

plot_fac = get_plot(u'钢材出厂价格（周）')
plot_fac.line('date', 'bg', source=source_fac, line_width=2, legend=u'宝钢出厂价格')
plot_fac.line('date', 'ag', source=source_fac, line_width=2, color='green', legend=u'鞍钢出厂价格')
plot_fac.line('date', 'sg', source=source_fac, line_width=2, color='red', legend=u'沙钢出厂价格')
plot_fac.line('date', 'hg', source=source_fac, line_width=2, color='gray', legend=u'河北钢铁出厂价格')

plot_raw = get_plot(u'原材料价格（周）')
plot_raw.line('date', 'tj', source=source_raw, line_width=2, legend=u'天津港港口63.5%印度粉现汇车板平均价')
plot_raw.line('date', 'ts', source=source_raw, line_width=2, color='green', legend=u'唐山地区66%酸性铁精粉含税出厂平均价')
plot_raw.line('date', 'ty', source=source_raw, line_width=2, color='red', legend=u'山西太原古交2#焦煤车板含税价')
plot_raw.line('date', 'jz', source=source_raw, line_width=2, color='gray', legend=u'华北山西晋中二级冶金焦含税车板成交平均价')

plot_st = get_plot(u'新加坡铁矿石掉期合同（日）')
plot_st.line('date', 'p', source=source_st, line_width=2, legend=u'新加坡铁矿石掉期合同')

plot_down = get_plot(u'下游产品产量（月）', pct=True)
plot_down.line('date', 'mec', source=source_down, line_width=2, legend=u'机床产量')
plot_down.line('date', 'boat', source=source_down, line_width=2, color='green', legend=u'船舶产量')
plot_down.line('date', 'car', source=source_down, line_width=2, color='red', legend=u'乘用车产量')
plot_down.line('date', 'ice', source=source_down, line_width=2, color='gray', legend=u'冰箱产量')

plot_open = get_plot(u'高炉开工率（周）', pct=True)
plot_open.line('date', 'open', source=source_open, line_width=2, legend=u'高炉开工率')

plot_stp = get_plot(u'中国铁矿石价格指数（日）')
plot_stp.line('date', 'p', source=source_stp, line_width=2, legend=u'中国铁矿石价格指数')

update_all()

curdoc().add_root(column(plot_prod, plot_inv, plot_pri, plot_inp, plot_fac, plot_raw, plot_open, plot_stp, plot_st, plot_down))
curdoc().title = u'钢铁中观数据库'
